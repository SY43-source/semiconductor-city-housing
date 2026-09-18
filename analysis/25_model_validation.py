"""[EN] Transferability test of the design model across cities.
#P3-검증 — transferability(이식 가능성) 테스트.
평택에서 캘리브레이션한 ρₐ·P(h|a)를 대조도시(안성·화성) 연령구조에 적용 →
그 도시 가구원수 분포를 예측 → DT_1JC1516 실측과 비교(MAPE). 모델의 실제 용도(신도시 이식) 검증.
+ 평택 자기일관성(≈0 기대).
데이터: 연령=DT_1B04005N(표준코드), 실측가구원수=DT_1JC1516(레거시코드), 파라미터=P1 CSV(평택).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import os,sys,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
from kosis_client import kosis_get
EMP='/Users/Shared/seoyeon_research/employment'; HH=['1인','2인','3인','4인','5인+']
YEAR='2024'
# (표준코드 DT_1B04005N, 레거시코드 DT_1JC1516)
CITIES={'평택':('41220','31070'),'안성':('41550','31220'),'화성':('41590','31240')}
BANDS=[('20~24세','20 - 24세'),('25~29세','25 - 29세'),('30~34세','30 - 34세'),('35~39세','35 - 39세'),
       ('40~44세','40 - 44세'),('45~49세','45 - 49세'),('50~54세','50 - 54세'),('55~59세','55 - 59세'),
       ('60~64세','60 - 64세'),('65~69세','65 - 69세'),('70~74세','70 - 74세'),('75~79세','75 - 79세'),
       ('80~84세','80 - 84세'),('85+','85세이상')]
# 평택 캘리브 파라미터
rho={r['age_band']:float(r['headship']) for r in csv.DictReader(open(f'{EMP}/pyeongtaek_headship_2024.csv'))}
rho['85+']=rho.get('85+',0) or 0.56
Pha={}
for r in csv.DictReader(open(f'{EMP}/pyeongtaek_head_age_hhsize_2024.csv')):
    a=r['age'].replace(' ',''); v=np.array([float(r[h]) for h in HH]); Pha[a]=v/v.sum() if v.sum() else v

def age_pop(std):
    p={}
    for x in kosis_get({'method':'getList','orgId':'101','tblId':'DT_1B04005N','objL1':std,'objL2':'ALL','itmId':'T2','prdSe':'Y','startPrdDe':YEAR,'endPrdDe':YEAR}):
        if isinstance(x,dict) and x.get('DT') is not None: p[x['C2_NM']]=int(x['DT'])
    return p
def observed_hhsize(legacy):
    itm={'T21':'1인','T22':'2인','T23':'3인','T24':'4인','T25':'5인+','T26':'5인+','T27':'5인+'}
    o={h:0 for h in HH}
    for code,h in itm.items():
        d=kosis_get({'method':'getList','orgId':'101','tblId':'DT_1JC1516','objL1':legacy,'objL2':'00','itmId':code,'prdSe':'Y','startPrdDe':YEAR,'endPrdDe':YEAR})
        if isinstance(d,list) and d and d[0].get('DT') not in (None,'X'): o[h]+=int(float(d[0]['DT']))
    tot=sum(o.values()); return np.array([o[h]/tot*100 for h in HH]) if tot else None
def predict(std):
    pop=age_pop(std); H=np.zeros(len(HH))
    for b,pl in BANDS:
        key=b.replace(' ','')
        if key in Pha: H+=pop.get(pl,0)*rho.get(b,0)*Pha[key]
    return H/H.sum()*100

rows=[]
for city,(std,leg) in CITIES.items():
    pred=predict(std); obs=observed_hhsize(leg)
    mape=np.mean(np.abs(pred-obs)/obs)*100
    rows.append((city,pred,obs,mape))
    print(f"\n[{city}] MAPE={mape:.1f}%  (예측 vs 실측, %)")
    for i,h in enumerate(HH): print(f"  {h}: 예측 {pred[i]:.1f} | 실측 {obs[i]:.1f} | Δ{pred[i]-obs[i]:+.1f}")

fig,axes=plt.subplots(1,len(rows),figsize=(5.2*len(rows),5.2),sharey=True)
fig.suptitle('모델 검증 — 평택 캘리브 파라미터로 타 도시 가구원수 예측 (transferability)',fontsize=13,fontweight='bold')
for ax,(city,pred,obs,mape) in zip(axes,rows):
    x=np.arange(len(HH)); w=0.4
    ax.bar(x-w/2,pred,w,label='예측',color='#39c'); ax.bar(x+w/2,obs,w,label='실측',color='#c73')
    ax.set_xticks(x); ax.set_xticklabels(HH,fontsize=8); ax.set_title(f'{city} (MAPE {mape:.1f}%)')
    ax.grid(alpha=0.3,axis='y'); ax.legend(fontsize=8)
axes[0].set_ylabel('가구 비중 (%)')
plt.tight_layout(rect=[0,0,1,0.94])
out=REPO + '/analysis/25_model_validation.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
print(f"\n요약: 평택 자기일관성 MAPE {rows[0][3]:.1f}% (≈0 기대) · 타도시 평균 MAPE {np.mean([r[3] for r in rows[1:]]):.1f}%")
