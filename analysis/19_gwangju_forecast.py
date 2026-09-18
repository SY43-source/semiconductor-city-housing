"""[EN] Gwangju (Gwangsan-gu) population transfer projection, event-time aligned.
#광주(광산구) 인구 전이 예측 — 평택 궤적 event-time τ 정렬.

τ=0: 반도체 가동 (평택 2017 / 광주 군공항 ~2030, offset 13yr).
광산구는 현재 감소 중(400→388천). '반도체가 평택처럼 작동하면 반전하는가' 시나리오.
전이: 광산(τk) = 광산_2030baseline × [평택(τk)/평택(τ0)]  (성장률 이식).
⚠️ 광주=지방 감소 대도시(평택=수도권 성장)라 baseline 정반대 → 강한 가정.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,sys,csv
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
from kosis_client import kosis_get  # 분당 200건 제한 자동 스로틀+백오프
# 광산구 연간
def kosis(code):
    d=kosis_get({'method':'getList','orgId':'101','tblId':'DT_1B040A3','objL1':code,'itmId':'T20','prdSe':'Y','startPrdDe':'2005','endPrdDe':'2025'})
    return {int(x['PRD_DE']):int(x['DT'])/1000 for x in d}
gs=kosis('29200')  # 광산구
# 평택
CSV=DATA_ROOT + '/population/control_regions_pop_2000_2025.csv'
pt={int(r['year']):int(r['population'])/1000 for r in csv.DictReader(open(CSV,encoding='utf-8-sig')) if '평택' in r['region']}

# 평택 event-time (τ0=2017)
PT_FAB=2017; tau=list(range(0,9))  # 2017~2025
pt_tau={k:pt[PT_FAB+k] for k in tau}
growth={k:pt_tau[k]/pt_tau[0] for k in tau}  # 성장배율 (τ0=1)
# 광산 2030 baseline: 2015~2025 선형 외삽
gy=np.array([y for y in range(2015,2026) if y in gs]); gv=np.array([gs[y] for y in gy])
lr=stats.linregress(gy,gv); gs_2030=lr.intercept+lr.slope*2030
GS_FAB=2030
# 전이 예측 (τ1~τ8 → 2031~2038, τ5=2035)
years_f=[GS_FAB+k for k in tau]
gs_pred={GS_FAB+k: gs_2030*growth[k] for k in tau}
# 감소지속 counterfactual
gs_cf={y: lr.intercept+lr.slope*y for y in years_f}

print(f"평택 성장배율 τ0→τ5(2035상당): {growth[5]:.3f} (×{growth[5]:.2f}), τ8: {growth[8]:.3f}")
print(f"광산 2030 baseline(외삽): {gs_2030:.0f}천")
print(f"광산 전이예측: 2035(τ5) {gs_pred[GS_FAB+5]:.0f}천 / 2038(τ8) {gs_pred[GS_FAB+8]:.0f}천")
print(f"광산 감소지속(반도체無): 2035 {gs_cf[2035]:.0f}천")

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('광주 광산구 인구 전이 예측 — 평택 궤적 τ 정렬 (반도체 반전 시나리오)',fontsize=13.5,fontweight='bold')
# 패널1: 달력시간
gyr=sorted(gs)
a1.plot(gyr,[gs[y] for y in gyr],'o-',color='#37a',lw=2,ms=4,label='광산구 실측')
a1.plot([GS_FAB]+years_f,[gs.get(2025,gs_2030)]+[gs_pred[y] for y in years_f] if False else [gs_2030]+[gs_pred[y] for y in years_f],'D--',color='#e33',lw=2,ms=6,label='반전 시나리오(평택 전이)')
a1.plot(years_f,[gs_cf[y] for y in years_f],'v:',color='#888',lw=2,label='감소지속(반도체無)')
a1.axvline(GS_FAB,color='gray',ls=':',lw=1.5); a1.text(GS_FAB+0.2,300,'반도체 가동 τ=0(~2030)',fontsize=8,color='gray')
a1.plot([2035],[gs_pred[2035]],'*',color='#900',ms=15)
a1.annotate(f'2035 반전 {gs_pred[2035]:.0f}천\nvs 감소 {gs_cf[2035]:.0f}천',(2035,gs_pred[2035]),fontsize=8.5,color='#900',ha='right',va='bottom')
a1.set_xlabel('연도'); a1.set_ylabel('광산구 인구(천명)'); a1.set_title('광산구: 감소 반전 시나리오'); a1.legend(fontsize=8.5); a1.grid(alpha=0.3)
# 패널2: event-time τ 정렬
a2.plot(tau,[pt_tau[k] for k in tau],'s-',color='#e33',lw=2.2,label='평택(τ0=2017)')
a2.plot(tau,[gs_pred[GS_FAB+k] for k in tau],'D--',color='#37a',lw=2.2,label='광산 전이(τ0=2030)')
a2.axvline(0,color='gray',ls=':',lw=1.3)
a2.set_xlabel('반도체 가동 후 연차 τ'); a2.set_ylabel('인구(천명)'); a2.set_title('event-time 정렬\n(광산=평택 성장률 이식, baseline만 다름)'); a2.legend(fontsize=9); a2.grid(alpha=0.3)
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/19_gwangju_forecast.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
