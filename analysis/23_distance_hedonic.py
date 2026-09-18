"""[EN] Continuous distance-to-campus hedonic, separating proximity from the new-town label.
#C1 내생성 보강 — 캠퍼스 연속거리(km) hedonic. '공장 근접' vs '신도시 패키지' 부분 분리.
모델: ln(단가 만원/㎡) ~ dist_km + newtown(고덕더미) + ln(면적) + age(연식) + 연도FE
 (1) 전체 평택: 신도시더미 통제 후에도 거리 계수 유의? (2) 고덕 제외: 신도시 없이 순수 근접 gradient 남나?
데이터: realprice_apt_trade(평택) × complexes(sqlite, lat/lon·approval_year) aptNm 매칭.
캠퍼스 기준점=삼성로 114 정문(37.0336,127.0551). haversine.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import csv,sqlite3,re,math
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
RP=DATA_ROOT + '/realprice/realprice_apt_trade.csv'
DB=INVENTORY_DB
CAMPUS=(37.0336,127.0551)
def norm(s):  # 단지명 정규화: 괄호·공백·특수문자 제거
    s=re.sub(r'\(.*?\)','',s or ''); s=re.sub(r'[^가-힣0-9A-Za-z]','',s); return s
def hav(a,b):
    R=6371; p=math.pi/180
    dla=(b[0]-a[0])*p; dlo=(b[1]-a[1])*p
    x=math.sin(dla/2)**2+math.cos(a[0]*p)*math.cos(b[0]*p)*math.sin(dlo/2)**2
    return 2*R*math.asin(math.sqrt(x))
# 1) 평택 단지 좌표 인덱스
con=sqlite3.connect(DB)
cx=[]
for name,lat,lon,ay,sec,rd in con.execute(
    "SELECT name,latitude,longitude,approval_year,COALESCE(sector,''),COALESCE(road_name,'') FROM complexes WHERE bjd_code LIKE '41220%' AND latitude IS NOT NULL"):
    god = ('고덕' in sec) or ('고덕' in rd)
    cx.append((norm(name),lat,lon,ay,god))
con.close()
cxmap={n:(lat,lon,ay,god) for n,lat,lon,ay,god in cx if n}
# 2) 실거래 매칭 + 피처
rows=[]
miss=0; tot=0
for r in csv.DictReader(open(RP,encoding='utf-8-sig')):
    if r['region']!='평택시': continue
    tot+=1
    an=norm(r['aptNm']); m=cxmap.get(an)
    if not m:  # 부분매칭(포함)
        cand=[v for k,v in cxmap.items() if an and (an in k or k in an) and len(an)>=4]
        m=cand[0] if len(cand)==1 else None
    if not m: miss+=1; continue
    lat,lon,ay,god=m
    try:
        amt=float(str(r['dealAmount']).replace(',','')); ar=float(r['excluUseAr']); y=int(r['dealYear']); by=int(r['buildYear'])
        if ar<=0 or amt<=0 or not (2015<=y<=2025): continue
    except: continue
    ppm2=amt/ar; age=max(0,y-by)
    rows.append(dict(lny=math.log(ppm2),lat=lat,lon=lon,dist=hav(CAMPUS,(lat,lon)),god=1.0 if god else 0.0,
                     lnar=math.log(ar),age=age,year=y))
print(f"실거래 평택 {tot:,} · 매칭 {len(rows):,} · 미매칭 {miss:,} (매칭률 {len(rows)/tot*100:.1f}%)")

def ols(data, use_god=True):
    yrs=sorted({d['year'] for d in data})[1:]  # 첫해 기준(FE)
    X=[]; Y=[]
    for d in data:
        row=[1.0,d['dist']]
        if use_god: row.append(d['god'])
        row+= [d['lnar'],d['age']] + [1.0 if d['year']==yy else 0.0 for yy in yrs]
        X.append(row); Y.append(d['lny'])
    X=np.array(X); Y=np.array(Y)
    beta,_,_,_=np.linalg.lstsq(X,Y,rcond=None)
    resid=Y-X@beta; n,k=X.shape
    XtXinv=np.linalg.inv(X.T@X)
    # HC0 robust
    S=(X*resid[:,None]); meat=S.T@S; cov=XtXinv@meat@XtXinv
    se=np.sqrt(np.diag(cov)); t=beta/se
    p=2*(1-stats.t.cdf(np.abs(t),n-k))
    names=['const','dist_km']+(['newtown_godeok'] if use_god else [])+['ln_area','age']+[f'y{yy}' for yy in yrs]
    return names,beta,se,p,n
print("\n=== (1) 전체 평택: 신도시더미 통제 ===")
nm,b,se,p,n=ols(rows,True)
for i,name in enumerate(nm):
    if name.startswith('y'): continue
    print(f"  {name:14s} β={b[i]:+.4f}  SE={se[i]:.4f}  p={p[i]:.4f}")
d1=b[nm.index('dist_km')]; g1=b[nm.index('newtown_godeok')]
print(f"  → 거리 1km 멀어질수록 단가 {(math.exp(d1)-1)*100:+.1f}% · 신도시 프리미엄 {(math.exp(g1)-1)*100:+.1f}% (n={n:,})")

print("\n=== (2) 고덕 제외 서브샘플: 순수 근접 gradient ===")
sub=[d for d in rows if d['god']==0]
nm2,b2,se2,p2,n2=ols(sub,False)
for i,name in enumerate(nm2):
    if name.startswith('y'): continue
    print(f"  {name:14s} β={b2[i]:+.4f}  SE={se2[i]:.4f}  p={p2[i]:.4f}")
d2=b2[nm2.index('dist_km')]
print(f"  → (고덕 제외) 거리 1km당 단가 {(math.exp(d2)-1)*100:+.1f}% (n={n2:,})")

# 3) 캠퍼스 기준점 민감도 — 거리계수 부호 강건성
print("\n=== (3) 캠퍼스 기준점 민감도 (전체모델 거리계수) ===")
CPS=[((37.0336,127.0551),'Main gate'),((37.010,127.090),'East P2'),((37.020,127.070),'Centroid')]
sens=[]
for cp,lbl in CPS:
    for d in rows: d['dist']=hav(cp,(d['lat'],d['lon']))
    nmx,bx,sex,px,_=ols(rows,True)
    dc=bx[nmx.index('dist_km')]; sens.append((lbl,dc,px[nmx.index('dist_km')]))
    print(f"  {lbl:16s} 거리 1km당 {(math.exp(dc)-1)*100:+.1f}% (p={px[nmx.index('dist_km')]:.4f})")
for d in rows: d['dist']=hav(CAMPUS,(d['lat'],d['lon']))  # 기본값 복원

# 4) 시각화 — 거리 vs 단가 산점(연도색) + OLS 계수 요약
fig,(a1,a2)=plt.subplots(1,2,figsize=(15,6))
fig.suptitle('Continuous distance-to-campus hedonic: separating proximity from the new town',fontsize=14,fontweight='bold')
dd=np.array([d['dist'] for d in rows]); yy=np.array([math.exp(d['lny']) for d in rows]); gg=np.array([d['god'] for d in rows])
a1.scatter(dd[gg==0],yy[gg==0],s=4,alpha=0.15,color='#888',label='Pyeongtaek, other')
a1.scatter(dd[gg==1],yy[gg==1],s=6,alpha=0.25,color='#e33',label='Godeok New Town')
a1.set_xlabel('Distance to campus main gate (km)'); a1.set_ylabel('Unit price (10k KRW/m2)'); a1.set_title('Distance vs unit price (all transactions, 2015-2025)')
a1.legend(); a1.grid(alpha=0.3); a1.set_ylim(0,yy.mean()*3)
# 계수 막대
labels=['전체:거리\n(1km당%)','전체:신도시\n프리미엄%','고덕제외:거리\n(1km당%)']
vals=[(math.exp(d1)-1)*100,(math.exp(g1)-1)*100,(math.exp(d2)-1)*100]
cols=['#37a','#e33','#2a8']
a2.bar(range(3),vals,color=cols)
for i,v in enumerate(vals): a2.text(i,v+(0.4 if v>=0 else -1.2),f'{v:+.1f}%',ha='center',fontweight='bold',fontsize=10)
a2.axhline(0,color='gray',lw=1); a2.set_xticks(range(3)); a2.set_xticklabels(labels,fontsize=9)
a2.set_ylabel('Effect on unit price (%)'); a2.set_title(f'Hedonic coefficients (age, area, year FE controlled)\nDistance p-value: all {p[nm.index("dist_km")]:.3f} / excl. Godeok {p2[nm2.index("dist_km")]:.3f}')
a2.grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/23_distance_hedonic.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
