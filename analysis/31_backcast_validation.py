"""[EN] Rolling-origin backcast validation of the annual forecast model.
#P2 — v7 연도별 예측모델 + rolling-origin backcast 검증(게이트).
모델: P(t) = P0 + (K - P0)/(1 + exp(-γ(t - t0))),  K = 144,173(고덕 계획 수용인구, 고정)
      P0 = 2018 저점(신도시 前 고덕면 기저), γ·t0만 추정 → 과적합 억제.
검증: rolling-origin — origin년까지 데이터로 적합 → 이후 연도 예측 → 실측 MAPE.
게이트: MAPE 양호 시 v7에 연도별 점추정 게재, 나쁘면 밴드만 게재.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import os,sys,csv
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
POP='/Users/Shared/seoyeon_research/population/godeok_age_year_matrix.csv'
K_POP=144173.0          # 고덕국제신도시 계획 수용인구(공시)
rows=list(csv.DictReader(open(POP)))
year=np.array([int(r['year']) for r in rows])
tot=np.array([int(r['계']) for r in rows],float)
P0=float(tot[year==2018][0])       # 2018 저점 = 신도시 前 기저
print(f"기저 P0(2018)={P0:,.0f} · 계획 K={K_POP:,.0f} · 2025 실측={tot[-1]:,.0f} ({tot[-1]/K_POP*100:.1f}%)")

def logistic(t, gamma, t0):
    return P0 + (K_POP-P0)/(1.0+np.exp(-gamma*(t-t0)))

def fit(mask):
    p,_=curve_fit(logistic, year[mask], tot[mask], p0=[0.35,2027.0], maxfev=20000)
    return p

# ── rolling-origin backcast ──
print("\n=== rolling-origin backcast (origin까지 적합 → 이후 예측) ===")
val=[]
for origin in [2021,2022,2023]:
    m=(year>=2018)&(year<=origin)
    try: g,t0=fit(m)
    except Exception as e: print(f"  origin {origin}: 적합실패 {e}"); continue
    fut=year>origin
    pred=logistic(year[fut],g,t0); act=tot[fut]
    ape=np.abs(pred-act)/act*100
    val.append((origin,g,t0,ape.mean()))
    det=' · '.join(f"{y}:{p:,.0f}vs{a:,.0f}({e:.0f}%)" for y,p,a,e in zip(year[fut],pred,act,ape))
    print(f"  origin {origin} (n={m.sum()}) → MAPE {ape.mean():5.1f}%  [{det}]")
mape_all=np.mean([v[3] for v in val]) if val else float('nan')
print(f"\n★ 평균 MAPE = {mape_all:.1f}%  → 게이트: {'통과(점추정 게재 가능)' if mape_all<20 else '미달(밴드만 게재)'}")

# ── 모델 비교: 로지스틱 vs 선형 vs 감쇠선형 (동일 rolling-origin) ──
print("\n=== 모델 비교 (rolling-origin MAPE, %) ===")
def pred_logistic(mask, tfut):
    g_,t0_=fit(mask); return logistic(tfut,g_,t0_)
def pred_linear(mask, tfut):
    """최근 3년 평균 증가율 선형 외삽 (K 상한 clip)"""
    yy,tt=year[mask],tot[mask]
    k=min(3,len(yy)-1); slope=(tt[-1]-tt[-1-k])/k
    return np.clip(tt[-1]+slope*(tfut-yy[-1]), None, K_POP)
def pred_damped(mask, tfut, phi=0.8):
    """감쇠 선형: 증가폭이 매년 phi배로 축소 (신도시 완공 접근 반영)"""
    yy,tt=year[mask],tot[mask]
    k=min(3,len(yy)-1); slope=(tt[-1]-tt[-1-k])/k
    out=[]; cur=tt[-1]; s=slope
    for _ in range(int(tfut[-1]-yy[-1])):
        s*=phi; cur=min(cur+s,K_POP); out.append(cur)
    idx=[int(t-yy[-1])-1 for t in tfut]
    return np.array([out[i] for i in idx])
MODELS={'로지스틱(K고정)':pred_logistic,'선형(최근3년)':pred_linear,'감쇠선형(φ=0.8)':pred_damped}
cmp={}
for nm,fn in MODELS.items():
    es=[]
    for origin in [2021,2022,2023]:
        m=(year>=2018)&(year<=origin); fu=year>origin
        try: p=fn(m,year[fu])
        except Exception: continue
        es.append((np.abs(p-tot[fu])/tot[fu]*100).mean())
    cmp[nm]=float(np.mean(es)) if es else float('nan')
    print(f"  {nm:<16} MAPE {cmp[nm]:5.1f}%")
best=min(cmp,key=lambda k:cmp[k]); print(f"★ 최적 모델 = {best} (MAPE {cmp[best]:.1f}%) → 게이트 {'통과' if cmp[best]<20 else '미달(밴드 제시)'}")

# ── 전체 적합 + 2026~2035 예측 ──
m_all=year>=2018
g,t0=fit(m_all)
print(f"\n전체적합: γ={g:.3f}, t0={t0:.1f} (변곡점 {t0:.0f}년)")
fut=np.arange(2026,2036)
pred=logistic(fut,g,t0)
# 잔차 기반 불확실성 밴드(±1.96·RMSE, 예측연차 비례 확대)
resid=tot[m_all]-logistic(year[m_all],g,t0); rmse=float(np.sqrt((resid**2).mean()))
band=np.array([1.96*rmse*np.sqrt(1+i*0.5) for i in range(1,len(fut)+1)])
print("연도  예측인구      밴드(±)     계획대비")
out=[]
for y,p,b in zip(fut,pred,band):
    print(f"{y}  {p:9,.0f}  ±{b:7,.0f}   {p/K_POP*100:5.1f}%")
    out.append((y,p,b))
os.makedirs('/Users/Shared/seoyeon_research/population',exist_ok=True)
with open('/Users/Shared/seoyeon_research/population/godeok_pop_forecast_annual.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['year','pred_pop','band','share_of_K'])
    for y,p,b in out: w.writerow([y,f'{p:.0f}',f'{b:.0f}',f'{p/K_POP:.4f}'])
print("✅ godeok_pop_forecast_annual.csv")

# ── 그림 ──
fig,(a1,a2)=plt.subplots(1,2,figsize=(14.5,5.8))
fig.suptitle(f'고덕 인구 연도별 예측 — 로지스틱(계획 수용인구 K=144,173 고정) · backcast MAPE {mape_all:.1f}%',fontsize=13,fontweight='bold')
a1.plot(year,tot/1000,'o-',color='#c33',label='observed',lw=2)
grid=np.arange(2018,2036)
a1.plot(grid,logistic(grid,g,t0)/1000,'--',color='#37a',label='logistic fit / forecast')
a1.fill_between(fut,(pred-band)/1000,(pred+band)/1000,color='#37a',alpha=0.18,label='uncertainty band')
a1.axhline(K_POP/1000,color='gray',ls=':',lw=1.2); a1.text(2019,K_POP/1000+2,f'계획 수용인구 {K_POP/1000:.0f}천명',fontsize=8.5,color='gray')
a1.set_xlabel('Year'); a1.set_ylabel('Population (thousands)'); a1.set_title('Population trajectory'); a1.legend(fontsize=9); a1.grid(alpha=0.3)
# backcast 검증
if val:
    ox=[str(v[0]) for v in val]; oy=[v[3] for v in val]
    a2.bar(ox,oy,color=['#2a8' if v<20 else '#d33' for v in oy])
    for i,v in enumerate(oy): a2.text(i,v+0.4,f'{v:.1f}%',ha='center',fontweight='bold')
    a2.axhline(20,color='#d33',ls='--',lw=1,label='20% gate')
    a2.set_xlabel('Fitting origin year'); a2.set_ylabel('MAPE of later years (%)'); a2.set_title('Rolling-origin backcast'); a2.legend(fontsize=9); a2.grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.93])
o=REPO + '/analysis/31_backcast_validation.png'
plt.savefig(o,dpi=120,bbox_inches='tight'); print(f'✅ {o}')
