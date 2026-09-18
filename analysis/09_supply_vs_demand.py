"""[EN] Supply vs transactions vs population, at the municipal level.
#B(정정) 공급 vs 거래 vs 인구 — 공급을 시군구(NAVER 단지메타 세대수)로 교체.

정정 배경: KOSIS 규모별 공급은 시도(경기)까지만이라 평택 대표성 부족(경기=서울인접 소형수요 혼입).
→ NAVER 단지메타(승인연도+평형별 세대수 units_of_same_area)로 평택·광주 시군구 공급을 직접 산출.
소형(<60㎡) 3중 대비: 공급(신축세대) vs 거래(실거래) vs 1인가구.
⚠️ NAVER 스냅샷=현재 등재 단지 기준(2013+ 신축엔 양호). 세대수=진짜 공급.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv, sqlite3
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
DB='/Users/Shared/seoyeon_inventory_master.sqlite'
RP='/Users/Shared/seoyeon_research/realprice'
POP='/Users/Shared/seoyeon_research/population/city_1person_household_2015_2024.csv'
YEARS=list(range(2015,2026))
GJ_GU=('12210','12240','12270','12300','12330')  # 광주 5구 신코드

def supply_small(bjd_like=None, bjd_in=None):
    """승인연도별 소형(<60) 공급비중(세대수)."""
    con=sqlite3.connect(DB); cur=con.cursor()
    where = f"c.bjd_code LIKE '{bjd_like}'" if bjd_like else "(" + " OR ".join(f"c.bjd_code LIKE '{p}%'" for p in bjd_in) + ")"
    q=f"""SELECT c.approval_year,
        SUM(CASE WHEN p.exclusive_area_m2<60 THEN p.units_of_same_area ELSE 0 END),
        SUM(p.units_of_same_area)
      FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number
      WHERE {where} AND c.approval_year BETWEEN 2015 AND 2025 GROUP BY c.approval_year"""
    d={y:float('nan') for y in YEARS}
    for yr,small,tot in cur.execute(q):
        if tot: d[yr]=small/tot*100
    con.close(); return d

def load(path,pred): return [r for r in csv.DictReader(open(path,encoding='utf-8-sig')) if r['excluUseAr'] and r['dealYear'] and pred(r)]
def trade_small(rows):
    t=defaultdict(int); s=defaultdict(int)
    for r in rows:
        y=int(r['dealYear'])
        if 2015<=y<=2025:
            t[y]+=1
            if float(r['excluUseAr'])<60: s[y]+=1
    return {y:(s[y]/t[y]*100 if t[y] else float('nan')) for y in YEARS}
single={}
for r in csv.DictReader(open(POP,encoding='utf-8-sig')):
    if r['single_ratio']: single.setdefault(r['region'],{})[int(r['year'])]=float(r['single_ratio'])

pt_sup=supply_small(bjd_like='41220%'); gj_sup=supply_small(bjd_in=GJ_GU)
pt_tr=trade_small(load(f'{RP}/realprice_apt_trade.csv',lambda r:r['region']=='평택시'))
gj_tr=trade_small(load(f'{RP}/realprice_apt_trade_gwangju.csv',lambda r:True))

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6),sharey=True)
fig.suptitle('공급(신축 세대, 시군구) vs 거래 vs 1인가구 — 소형(<60㎡) 3중 대비',fontsize=13.5,fontweight='bold')
def panel(ax,sup,tr,pop_reg,title):
    ys=[y for y in YEARS if sup[y]==sup[y]]
    ax.plot(ys,[sup[y] for y in ys],'D-',color='#c63',lw=2.3,label='소형 공급비중(신축세대)')
    ax.plot(YEARS,[tr[y] for y in YEARS],'s-',color='#2a8',lw=2.3,label='소형 거래비중(실거래)')
    yy=[y for y in YEARS if y in single.get(pop_reg,{})]
    ax.plot(yy,[single[pop_reg][y] for y in yy],'o--',color='#d33',lw=2,label=f'1인가구비율({pop_reg})')
    ax.set_title(title); ax.set_xlabel('연도'); ax.set_ylabel('비율(%)'); ax.legend(fontsize=8.5); ax.grid(alpha=0.3)
panel(a1,pt_sup,pt_tr,'평택시','평택 (공급·거래·인구 모두 시군구)')
panel(a2,gj_sup,gj_tr,'광주광역시','광주 5구')
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/09_supply_vs_demand.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
def fmt(d):
    a=next(d[y] for y in YEARS if d[y]==d[y]); b=[d[y] for y in YEARS if d[y]==d[y]][-1]; return f"{a:.0f}→{b:.0f}%"
print(f"평택 소형: 공급 {fmt(pt_sup)} | 거래 {fmt(pt_tr)} | 1인 {single['평택시'][2015]:.0f}→{single['평택시'][2024]:.0f}%")
print(f"광주 소형: 공급 {fmt(gj_sup)} | 거래 {fmt(gj_tr)} | 1인 {single['광주광역시'][2015]:.0f}→{single['광주광역시'][2024]:.0f}%")
