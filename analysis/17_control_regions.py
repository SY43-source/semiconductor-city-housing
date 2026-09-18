"""[EN] Robustness: population inflow vs non-semiconductor control regions.
#로버스트니스 — 평택 인구 유입 vs 비반도체(안성 인접 / 안동 정체). ※진천 제외.

+ 평택 총인구 400→500천 vs 500→600천 돌파 기울기 비교(반도체 가속).
데이터: control_regions_pop_2000_2025.csv (진천 제거 후 재기록).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
CSV='/Users/Shared/seoyeon_research/population/control_regions_pop_2000_2025.csv'
DROP='진천'
rows=[r for r in csv.DictReader(open(CSV,encoding='utf-8-sig')) if DROP not in r['region']]
# 원천 CSV에서 진천 제거하여 재기록
with open(CSV,'w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['year','region','population'])
    for r in rows: w.writerow([r['year'],r['region'],r['population']])
data={}
for r in rows: data.setdefault(r['region'],{})[int(r['year'])]=int(r['population'])
STY={'평택시(반도체)':('#e33','o','-'),'안성시(인접대조)':('#38a','s','--'),'안동시(비반도체정체)':('#c93','D',':')}
YEARS=list(range(2000,2026))

# 평택 돌파연도(선형보간) + 구간 기울기
pt=data['평택시(반도체)']
ys=sorted(pt)
def cross(level):
    for i in range(1,len(ys)):
        a,b=ys[i-1],ys[i]
        if pt[a]<level<=pt[b]:
            return a+(level-pt[a])/(pt[b]-pt[a])*(b-a)
    return None
t400,t500,t600=cross(400000),cross(500000),cross(600000)
s45=100/(t500-t400)   # 천명/년
s56=100/(t600-t500)
print(f"평택 400천 돌파 ~{t400:.1f} / 500천 ~{t500:.1f} / 600천 ~{t600:.1f}")
print(f"400→500천: {t500-t400:.1f}년, 기울기 {s45:.1f} 천명/년")
print(f"500→600천: {t600-t500:.1f}년, 기울기 {s56:.1f} 천명/년  (×{s56/s45:.1f} 가속)")

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('평택 인구 유입 vs 비반도체 지역(안성·안동) + 평택 돌파 기울기',fontsize=13.5,fontweight='bold')
# 절대 + 돌파선
for nm,(c,m,ls) in STY.items():
    yy=[y for y in YEARS if y in data[nm]]
    a1.plot(yy,[data[nm][y]/1000 for y in yy],marker=m,ls=ls,color=c,lw=2,ms=4,label=nm)
for lv,t in [(400,t400),(500,t500),(600,t600)]:
    a1.axhline(lv,color='#e33',ls=':',lw=0.8,alpha=0.5)
    a1.plot([t],[lv],'*',color='#900',ms=13,zorder=5)
    a1.annotate(f'{lv}천\n~{t:.0f}',(t,lv),fontsize=8,color='#900',ha='right',va='bottom')
a1.axvline(2017,color='gray',ls=':',lw=1.2); a1.text(2017.2,150,'삼성 P1',fontsize=8,color='gray')
a1.set_title('총인구(천명) 2000~2025'); a1.set_xlabel('연도'); a1.set_ylabel('총인구(천명)'); a1.legend(fontsize=8.5,loc='center left'); a1.grid(alpha=0.3)
# 기울기 비교 bar
a2.bar(['400→500천\n(반도체 前~초기)','500→600천\n(P2~AI붐)'],[s45,s56],color=['#88a','#e33'])
for i,(v,dt) in enumerate([(s45,t500-t400),(s56,t600-t500)]):
    a2.text(i,v+0.3,f'{v:.1f} 천명/년\n({dt:.1f}년 소요)',ha='center',fontsize=10,fontweight='bold')
a2.set_ylabel('연평균 인구 증가 (천명/년)'); a2.set_title(f'평택 100천명 돌파 기울기\n반도체 확장기 ×{s56/s45:.1f} 가속'); a2.grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/17_control_regions.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
