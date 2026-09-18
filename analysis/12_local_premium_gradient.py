"""[EN] Distance decay within Pyeongtaek — proximity premium to the campus.
#핵심 — 평택 내부 거리 감쇠: 반도체 캠퍼스 인접 프리미엄 (공간 winner-vs-loser).

도시 내부 비교라 거시·금리·전국사이클·도시화 자동 통제 → 순수 반도체 국지효과.
캠퍼스 인접(고덕권 동부) vs 외곽(서부 읍면) 중위 실거래 단가(만원/㎡) + 배율.
데이터: 평택 실거래(realprice_apt_trade.csv), umdNm 그룹.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import csv, statistics
from collections import defaultdict
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
RP=DATA_ROOT + '/realprice'; YEARS=list(range(2015,2026))
NEAR=['고덕','서정동','지제동','동삭동','신촌']       # 캠퍼스·고덕신도시권(동부)
FAR=['안중읍','포승읍','팽성읍','청북읍','현덕면','오성면']  # 서부 외곽
pt=[r for r in csv.DictReader(open(f'{RP}/realprice_apt_trade.csv',encoding='utf-8-sig')) if r['region']=='평택시']
def ppm2(rows,keys):
    by=defaultdict(list)
    for r in rows:
        if any(k in r['umdNm'] for k in keys):
            try:
                amt=float(str(r['dealAmount']).replace(',','')); ar=float(r['excluUseAr']); y=int(r['dealYear'])
                if ar>0 and 2015<=y<=2025: by[y].append(amt/ar)
            except: pass
    return {y:(statistics.median(by[y]) if by[y] else np.nan) for y in YEARS}
near=ppm2(pt,NEAR); far=ppm2(pt,FAR)
ratio={y:near[y]/far[y] for y in YEARS}

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('반도체 국지 프리미엄 — 평택 내부 거리 감쇠 (거시·도시화 자동 통제)',fontsize=14,fontweight='bold')
a1.plot(YEARS,[near[y] for y in YEARS],'o-',color='#e33',lw=2.5,label='캠퍼스 인접(고덕권)')
a1.plot(YEARS,[far[y] for y in YEARS],'s--',color='#38a',lw=2.2,label='평택 외곽(서부 읍면)')
for x,l in [(2017,'P1'),(2020,'P2'),(2022,'P3')]:
    a1.axvline(x,color='gray',ls=':',lw=1.3); a1.text(x,150,l,fontsize=8,color='gray',ha='center')
a1.set_title('중위 실거래 단가 (만원/㎡)\n인접 ×2.6 폭등 vs 외곽 정체'); a1.set_xlabel('연도'); a1.set_ylabel('만원/㎡'); a1.legend(fontsize=9); a1.grid(alpha=0.3)
a2.plot(YEARS,[ratio[y] for y in YEARS],'D-',color='#a2d',lw=2.7)
a2.axhline(1.0,color='gray',ls='--',lw=1,label='동가(1.0)')
for x,l in [(2017,'P1'),(2020,'P2'),(2022,'P3')]: a2.axvline(x,color='blue',ls=':',lw=1.2)
a2.annotate(f'0.96(2015)\n공장前 프리미엄 없음',xy=(2015,ratio[2015]),xytext=(2016,1.5),fontsize=8,color='#555',arrowprops=dict(arrowstyle='->',alpha=0.5))
a2.set_title(f'인접/외곽 단가 배율: 0.96 → {ratio[2025]:.2f}\n= 순수 반도체 국지효과'); a2.set_xlabel('연도'); a2.set_ylabel('인접 ÷ 외곽'); a2.legend(fontsize=9); a2.grid(alpha=0.3)
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/12_local_premium_gradient.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
print(f"인접 ×{near[2025]/near[2015]:.2f} / 외곽 ×{far[2025]/far[2015]:.2f} / 배율 {ratio[2015]:.2f}→{ratio[2025]:.2f}")
PY_END=0
