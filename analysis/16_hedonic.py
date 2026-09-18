"""[EN] Hedonic model — controls for building age to isolate the location effect.
#hedonic — 고덕 인접 프리미엄에서 '신축 효과' 통제 → 순수 입지효과 분리.

우려: 고덕권은 신축 많아 프리미엄에 연식효과 혼입. 통제:
(a) 연도별 OLS log(단가)~near+건축연도+전용면적 → exp(near계수)=연식·면적 보정 프리미엄.
(b) 신축(2015+)만 / 구축(~2004)만 각각 고덕/외곽 배율 (동일연식 비교).
raw 배율 vs 보정 배율 비교. numpy lstsq(statsmodels 불요).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv,statistics
from collections import defaultdict
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
RP='/Users/Shared/seoyeon_research/realprice'; YEARS=list(range(2015,2026))
NEAR=['고덕','서정동','지제동','동삭동','신촌']; FAR=['안중읍','포승읍','팽성읍','청북읍','현덕면','오성면']
pt=[r for r in csv.DictReader(open(f'{RP}/realprice_apt_trade.csv',encoding='utf-8-sig')) if r['region']=='평택시']
def parse(r):
    try:
        a=float(str(r['dealAmount']).replace(',','')); ar=float(r['excluUseAr']); by=int(r['buildYear']); y=int(r['dealYear'])
        near=1 if any(k in r['umdNm'] for k in NEAR) else (0 if any(k in r['umdNm'] for k in FAR) else None)
        if ar>0 and near is not None and 2015<=y<=2025 and 1970<by<2030: return dict(ppm=a/ar,ar=ar,by=by,near=near,y=y)
    except: pass
    return None
rows=[x for x in (parse(r) for r in pt) if x]

# (a) 연도별 OLS: log(ppm) ~ 1 + near + by_c + ar_c → exp(β_near)=보정 프리미엄
adj={}; raw={}
for y in YEARS:
    yr=[x for x in rows if x['y']==y]
    n1=[x for x in yr if x['near']==1]; n0=[x for x in yr if x['near']==0]
    if len(n1)<10 or len(n0)<10: continue
    raw[y]=statistics.median([x['ppm'] for x in n1])/statistics.median([x['ppm'] for x in n0])
    X=np.array([[1,x['near'],x['by'],x['ar']] for x in yr],float); Y=np.log(np.array([x['ppm'] for x in yr]))
    X[:,2]-=X[:,2].mean(); X[:,3]-=X[:,3].mean()
    beta,*_=np.linalg.lstsq(X,Y,rcond=None)
    adj[y]=np.exp(beta[1])  # 연식·면적 보정 near 프리미엄(배율)
# (b) 동일연식 배율
def ratio_era(lo,hi):
    out={}
    for y in YEARS:
        n1=[x['ppm'] for x in rows if x['y']==y and x['near']==1 and lo<=x['by']<hi]
        n0=[x['ppm'] for x in rows if x['y']==y and x['near']==0 and lo<=x['by']<hi]
        if len(n1)>=5 and len(n0)>=5: out[y]=statistics.median(n1)/statistics.median(n0)
    return out
new=ratio_era(2015,2030); old=ratio_era(1970,2005)

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('hedonic — 고덕 인접 프리미엄에서 신축효과 통제 후 순수 입지효과',fontsize=13.5,fontweight='bold')
a1.plot([y for y in YEARS if y in raw],[raw[y] for y in YEARS if y in raw],'o-',color='#bbb',lw=2,label='raw 배율(무보정)')
a1.plot([y for y in YEARS if y in adj],[adj[y] for y in YEARS if y in adj],'D-',color='#a2d',lw=2.6,label='연식·면적 보정 배율(OLS)')
a1.axhline(1,color='gray',ls='--',lw=1); a1.set_title('연식·면적 통제 후에도 프리미엄 유지되나')
a1.set_xlabel('연도'); a1.set_ylabel('고덕/외곽 단가배율'); a1.legend(fontsize=9); a1.grid(alpha=0.3)
a2.plot([y for y in YEARS if y in new],[new[y] for y in YEARS if y in new],'s-',color='#e33',lw=2.3,label='신축(2015+)끼리 비교')
a2.plot([y for y in YEARS if y in old],[old[y] for y in YEARS if y in old],'^-',color='#2a8',lw=2.3,label='구축(~2004)끼리 비교')
a2.axhline(1,color='gray',ls='--',lw=1); a2.set_title('동일 연식대 내 고덕/외곽 배율\n(신축·구축 각각에서 프리미엄?)')
a2.set_xlabel('연도'); a2.set_ylabel('고덕/외곽 단가배율'); a2.legend(fontsize=9); a2.grid(alpha=0.3)
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/16_hedonic.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
yy=[y for y in YEARS if y in adj]
print(f"raw 배율 {raw.get(yy[0]):.2f}→{raw.get(yy[-1]):.2f} / 보정 배율 {adj[yy[0]]:.2f}→{adj[yy[-1]]:.2f}")
print(f"신축끼리 배율: {[round(new[y],2) for y in sorted(new)]}")
print(f"구축끼리 배율: {[round(old[y],2) for y in sorted(old)]}")
