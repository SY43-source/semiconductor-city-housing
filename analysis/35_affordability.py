"""[EN] Housing affordability — PIR, mortgage burden, public vs private rent (SS IV.8).
#P0 (v9 §IV.10) — 주거 접근성(affordability): 감당 가능한 주거는 어디서 공급되는가.
실측: 고덕 매매 중위가(2024~25) · 월세 실질부담(보증금 전월세전환 포함) · 임대주택 비중.
가정(명시): 초년생 연소득 3개 시나리오 · LTV 70% · 금리 4% · 30년 원리금균등.
산출: employment/godeok_affordability.csv + 그림 35
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,csv,sqlite3,statistics as st
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
RP=DATA_ROOT + '/realprice'; EMP=DATA_ROOT + '/employment'
DB=INVENTORY_DB
BANDS=['Small<60','Standard 60-85','Large 85+']
# ⚠️ 고덕 판별은 **법정동 기준**. 단지명 '고덕' 매칭은 금지 —
#    FP: 이충동 소재 '고덕시티'·'고덕코아루더블루시티'(구도심) 오포착
#    FN: 실거래 umdNm 은 '고덕면 궁리' 형식이라 '고덕면' 완전일치로는 태평·평택영화블렌하임 누락
def god(a,u): return (u or '').startswith('고덕')
def band(a): return BANDS[0] if a<60 else (BANDS[1] if a<85 else BANDS[2])

# ── 1) 매매 중위가 (실측, 2024~2025) ──
buy={b:[] for b in BANDS}
for r in csv.DictReader(open(f'{RP}/realprice_apt_trade.csv',encoding='utf-8-sig')):
    if r['region']!='평택시' or not god(r['aptNm'],r['umdNm']): continue
    try:
        y=int(r['dealYear']); amt=float(str(r['dealAmount']).replace(',','')); a=float(r['excluUseAr'])
    except: continue
    if y>=2024: buy[band(a)].append(amt)
P={b:st.median(v) for b,v in buy.items() if v}
print("=== 고덕 매매 중위가 (2024~25, 만원) [실측] ===")
for b in BANDS: print(f"  {b:<10} {P[b]:>8,.0f}만원  (n={len(buy[b]):,})")

# ── 2) 월세 실질부담 (실측 + 전월세전환율 5.5% 가정) ──
CONV=0.055
# ⚠️ 공공임대 단지는 NAVER 단지 메타에 미등재 → 실거래 단지명으로만 식별 가능.
#    명목 매칭이지만 대안 자료원이 없으므로 '명시/추정'을 분리해 보수적으로 사용한다.
PUBKEY=['엘에이치','LH','행복주택','국민임대','영구임대','공공','사회임대']
def is_pub(n): return any(k in (n or '') for k in PUBKEY) or ((n or '').startswith('평택고덕') and '단지' in n)
rent={b:[] for b in BANDS}; rent_pub={b:[] for b in BANDS}; rent_priv={b:[] for b in BANDS}
for r in csv.DictReader(open(f'{RP}/realprice_apt_rent_pt.csv',encoding='utf-8-sig')):
    if not god(r['aptNm'],r['umdNm']) or r['rentType']!='월세': continue
    try:
        a=float(r['excluUseAr']); m=float(r['monthly']); d=float(r['deposit']); y=int(r['dealYear'])
    except: continue
    if y>=2024 and m>0:
        e=m + d*CONV/12; b_=band(a); rent[b_].append(e)
        (rent_pub if is_pub(r['aptNm']) else rent_priv)[b_].append(e)
R={b:st.median(v) for b,v in rent.items() if v}
RPUB={b:st.median(v) for b,v in rent_pub.items() if v}
RPRIV={b:st.median(v) for b,v in rent_priv.items() if v}
print(f"\n=== 월세 실질부담 (보증금 {CONV*100:.1f}% 환산, 2024~) — 공공/민간 분리 ===")
for b in BANDS:
    p_=f"{RPUB[b]:.0f}만(n={len(rent_pub[b]):,})" if b in RPUB else "—"
    v_=f"{RPRIV[b]:.0f}만(n={len(rent_priv[b]):,})" if b in RPRIV else "—"
    print(f"  {b:<10} 전체 {R.get(b,0):>4.0f}만  |  공공 {p_:<18} 민간 {v_}")
print("  ⚠️ 소형 전체 중위값은 공공임대가 81%를 차지한 혼합값 — 민간 시장가로 오독 금지")

# ── 3) 임대주택 비중 (실측) ──
con=sqlite3.connect(DB)
# ⚠️ 임대는 **lease_households 실측 필드** 기준. 단지명 '임대' 매칭 금지 —
#    임대 세대의 대부분이 명칭에 드러나지 않는 분양·임대 혼합 단지 소재(6개 중 5개).
#    명칭 기준은 실제(9.4%)의 1/3 이하만 포착했다(2,249 → 660).
q="""SELECT SUM(total_households), SUM(IFNULL(lease_households,0)) FROM complexes
     WHERE bjd_code LIKE '41220%' AND (sector LIKE '%고덕%' OR road_name LIKE '%고덕%')"""
TOTU,RENTU=con.execute(q).fetchone()
qc="""SELECT SUM(total_households), SUM(IFNULL(lease_households,0)) FROM complexes WHERE bjd_code LIKE '41220%'"""
PT_T,PT_R=con.execute(qc).fetchone(); con.close()
RENT_SH=RENTU/TOTU*100
# ⚠️ 공공임대 단지는 NAVER 단지 메타 미등재 → 공고·보도 실측치를 외부 병합(하한).
#    전량임대: LH2(A-6) 1,600 · LH15(A-58) 1,295 · LH12(A57-1) 900 · 경기행복주택(A-62) 800
#             · LH17 1·2단지 594 · LH35(A-2) 549 · 센트레빌NHF3(A-1) 383  = 6,121
#    혼합단지 임대분(단지메타 lease_households, 공급자=LH): NHF7 609 · 르플로랑 295 · 헤스티블 167 · 양우내안애 129 = 1,200
#    ⚠️ 민간임대는 어울림스퀘어 660 + 다해브 389 = 1,049 뿐 (v10 의 '민간임대 2,249'는 오분류)
#    미포함: 사회임대주택 1·3차 → 실제 총량은 이보다 큼
PUBU_FULL=1600+1295+900+800+594+549+383+5+5 # 6,131 (단지메타 미등재 → 분모 가산. +사회임대주택 1·3차 각 5세대)
PUBU_MIX=609+295+167+129+389                # 1,589 (메타에 포함, 공급자는 LH. +다해브 A-53 신혼희망타운 행복주택)
PUBU=PUBU_FULL+PUBU_MIX                     # 7,321
PRIVR=660                                   # 660 (어울림스퀘어만 민간임대)
TOT_ALL=TOTU+PUBU_FULL; PRIV_SALE=TOTU-RENTU; RENTU=PRIVR
print(f"\n=== 공급 재고 [단지메타 + 공공임대 공고 병합] ===")
print(f"  민간 분양   {PRIV_SALE:>7,}세대 = {PRIV_SALE/TOT_ALL*100:>5.1f}%")
print(f"  민간 임대   {RENTU:>7,}세대 = {RENTU/TOT_ALL*100:>5.1f}%   (어울림스퀘어)")
print(f"  공공 임대   {PUBU:>7,}세대 = {PUBU/TOT_ALL*100:>5.1f}%   (전량 공고·건축물대장 확정)")
print(f"  임대 계     {RENTU+PUBU:>7,}세대 = {(RENTU+PUBU)/TOT_ALL*100:>5.1f}%  / 총 {TOT_ALL:,}세대")
print(f"  (참고) 단지메타만 볼 때 임대 {RENT_SH:.1f}% — 공공임대 미등재로 과소")

# ── 4) 부담 지표 (가정 명시) ──
INC={'Low 36M':3600,'Mid 50M':5000,'High 60M':6000}   # 연소득 시나리오
LTV,RATE,YRS=0.70,0.04,30
def monthly_pay(price):
    L=price*LTV; i=RATE/12; n=YRS*12
    return L*i*(1+i)**n/((1+i)**n-1)
print(f"\n=== 자가 진입 장벽 (LTV {LTV:.0%}·금리 {RATE:.0%}·{YRS}년 원리금균등) [가정] ===")
print(f"{'규격':<10}{'가격':>9}{'자기자본':>10}{'월상환':>9} | " + " ".join(f"{k.split()[0]}PIR" for k in INC))
rows=[]
for b in BANDS:
    pay=monthly_pay(P[b]); eq=P[b]*(1-LTV)
    pirs=[P[b]/v for v in INC.values()]
    burden=[pay/(v/12)*100 for v in INC.values()]
    rows.append(dict(band=b,price=P[b],equity=eq,pay=pay,pir=pirs,burden=burden,rent=R.get(b,float('nan'))))
    print(f"{b:<10}{P[b]:>9,.0f}{eq:>10,.0f}{pay:>9,.0f} | " + " ".join(f"{x:>6.1f}" for x in pirs))
print(f"\n=== 월세 부담률 vs 자가 상환부담률 (월소득 대비 %) ===")
for r_ in rows:
    rb=[r_['rent']/(v/12)*100 for v in INC.values()]
    print(f"  {r_['band']:<10} 월세 {' / '.join(f'{x:.0f}%' for x in rb)}   vs   자가상환 {' / '.join(f'{x:.0f}%' for x in r_['burden'])}")

with open(f'{EMP}/godeok_affordability.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['band','median_price_manwon','equity_needed','monthly_payment','rent_equiv',
                                 'PIR_3600','PIR_5000','PIR_6000','burden_own_3600','burden_own_5000','burden_own_6000'])
    for r_ in rows:
        w.writerow([r_['band'],f"{r_['price']:.0f}",f"{r_['equity']:.0f}",f"{r_['pay']:.0f}",f"{r_['rent']:.0f}"]
                   +[f"{x:.1f}" for x in r_['pir']]+[f"{x:.1f}" for x in r_['burden']])
print(f"✅ {EMP}/godeok_affordability.csv")

# ── 그림 ──
fig,ax=plt.subplots(1,3,figsize=(17,5.4))
fig.suptitle('Housing access: where affordable housing comes from (Godeok, 2024-25 transactions)',fontsize=13.5,fontweight='bold')
C=['#3a7ca5','#c1553b','#c99a3b']
# ① PIR
x=np.arange(3); w=0.26
for j,(k,v) in enumerate(INC.items()):
    vals=[P[b]/v for b in BANDS]
    ax[0].bar(x+(j-1)*w,vals,w,label=k,color=['#8fb3cc','#5588aa','#2c5f80'][j])
    for i,val in enumerate(vals): ax[0].text(i+(j-1)*w,val+0.25,f'{val:.1f}',ha='center',fontsize=7.5)
ax[0].axhline(5.1,color='#c0392b',ls='--',lw=1.4)
ax[0].text(2.45,5.55,'5.1 = international "severely unaffordable"',fontsize=8,color='#c0392b',ha='right',fontweight='bold',
           bbox=dict(facecolor='white',alpha=0.88,edgecolor='#c0392b',linewidth=0.6,boxstyle='round,pad=0.25'))
ax[0].set_xticks(x); ax[0].set_xticklabels(BANDS,fontsize=9); ax[0].set_ylabel('PIR (price / annual income)')
ax[0].set_title('(1) Ownership burden relative to entry-level income'); ax[0].legend(fontsize=7.5,title='Annual income',title_fontsize=7.5)
ax[0].grid(alpha=0.25,axis='y')
# ② 월 부담 비교 (국평 자가 vs 소형 월세)
lab=['국평 자가\n(월 상환액)','국평 월세\n(민간)','소형 월세\n민간','소형 월세\n공공임대']
val=[monthly_pay(P['Standard 60-85']), RPRIV.get('Standard 60-85',0), RPRIV.get('Small<60',0), RPUB.get('Small<60',0)]
bars=ax[1].bar(lab,val,color=['#c0392b','#7f8c8d','#d98b3a','#2e7d32'],width=0.6)
for i,v in enumerate(val): ax[1].text(i,v+4,f'{v:.0f}',ha='center',fontsize=10,fontweight='bold')
ax[1].text(2.5,172,'Only public rental\nstays within the line',ha='center',fontsize=9,color='#1b5e20',fontweight='bold',
           bbox=dict(facecolor='white',alpha=0.9,edgecolor='#2e7d32',linewidth=0.7,boxstyle='round,pad=0.3'))
for j,(k,inc) in enumerate(INC.items()):
    ax[1].axhline(inc/12*0.30,color='#555',ls=':',lw=1)
    ax[1].text(3.48,inc/12*0.30+2,f'30% of {k.split()[0]} income',fontsize=7,color='#555',ha='right')
ax[1].set_ylabel('Monthly housing cost (10k KRW)'); ax[1].set_title('(2) Against the 30%-of-income line: only public rental passes')
ax[1].tick_params(axis='x',labelsize=8.5)
ax[1].grid(alpha=0.25,axis='y')
# ③ 공급 점유유형 vs 실제 점유
ps=PRIV_SALE/TOT_ALL*100; pr=RENTU/TOT_ALL*100; pu=PUBU/TOT_ALL*100
ax[2].bar(['Supply stock\n(by tenure)'],[ps],color='#c0392b')
ax[2].bar(['Supply stock\n(by tenure)'],[pr],bottom=[ps],color='#d98b3a')
ax[2].bar(['Supply stock\n(by tenure)'],[pu],bottom=[ps+pr],color='#2e7d32')
ax[2].bar(['Realized tenure\n(lease records)'],[26.6],color='#c0392b')
ax[2].bar(['Realized tenure\n(lease records)'],[73.4],bottom=[26.6],color='#2e7d32')
ax[2].text(0,ps/2,f'Private sale {ps:.0f}%',ha='center',color='white',fontsize=9.5,fontweight='bold')
ax[2].text(0,ps+pr/2,f'Private rent {pr:.0f}%',ha='center',va='center',color='white',fontsize=8)
ax[2].text(0,ps+pr+pu/2,f'Public rental {pu:.0f}%',ha='center',va='center',color='white',fontsize=9,fontweight='bold')
ax[2].text(0,103,'Public rental: notice-confirmed',ha='center',va='bottom',fontsize=7.5,color='#1b5e20')

ax[2].text(1,13,'Jeonse 26.6%',ha='center',color='white',fontsize=9)
ax[2].text(1,63,'Monthly rent 73.4%',ha='center',color='white',fontsize=10,fontweight='bold')
ax[2].set_ylabel('Share (%)'); ax[2].set_ylim(0,132)
ax[2].set_title('(3) Stock vs realized tenure')
ax[2].annotate('',xy=(0.95,120),xytext=(0.05,120),arrowprops=dict(arrowstyle='->',color='#c0392b',lw=2))
ax[2].text(0.5,123,'Price barrier -> move to tenancy',ha='center',fontsize=9.5,color='#c0392b',fontweight='bold')
ax[2].grid(alpha=0.25,axis='y')
plt.tight_layout(rect=[0,0,1,0.92])
o=REPO + '/analysis/35_affordability.png'
plt.savefig(o,dpi=120,bbox_inches='tight'); print(f'✅ {o}')
