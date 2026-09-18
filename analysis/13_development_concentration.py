"""[EN] Spatial concentration of new development on Godeok New Town.
#반도체 효과 3번째 기둥 — 개발의 공간 집중(고덕신도시). '구조 동일'을 반증.

규격 배합(%)은 전국과 같아도, 신규 개발의 '입지'는 캠퍼스 인접으로 통째 이동 = 공간구조 재편.
평택 승인연도별 신규 세대수: 고덕권(캠퍼스) vs 외곽 + 고덕권 점유율.
데이터: NAVER 단지메타 sqlite(complexes.approval_year·total_households·sector).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sqlite3
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
DB='/Users/Shared/seoyeon_inventory_master.sqlite'; YEARS=list(range(2013,2026))
con=sqlite3.connect(DB); cur=con.cursor()
q="""SELECT approval_year,
 SUM(CASE WHEN (sector LIKE '%고덕%' OR road_name LIKE '%고덕%' OR sector LIKE '%서정%' OR sector LIKE '%지제%') THEN total_households ELSE 0 END),
 SUM(CASE WHEN (sector LIKE '%안중%' OR sector LIKE '%포승%' OR sector LIKE '%팽성%' OR sector LIKE '%청북%') THEN total_households ELSE 0 END),
 SUM(total_households)
FROM complexes WHERE bjd_code LIKE '41220%' AND approval_year BETWEEN 2013 AND 2025 GROUP BY approval_year"""
near={}; far={}; tot={}
for yr,n,f,t in cur.execute(q): near[yr]=n or 0; far[yr]=f or 0; tot[yr]=t or 0
con.close()
share=[(near.get(y,0)/tot[y]*100 if tot.get(y) else 0) for y in YEARS]

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('반도체 효과 ③ 개발의 공간 집중 — "구조 동일"의 반증',fontsize=14,fontweight='bold')
a1.bar([y-0.2 for y in YEARS],[near.get(y,0) for y in YEARS],0.4,color='#e33',label='고덕권(캠퍼스 인접)')
a1.bar([y+0.2 for y in YEARS],[far.get(y,0) for y in YEARS],0.4,color='#38a',label='외곽(서부 읍면)')
for x,l in [(2017,'P1'),(2020,'P2'),(2022,'P3')]: a1.axvline(x,color='gray',ls=':',lw=1.2)
a1.set_title('평택 신규 세대수 — 개발 입지 이동\n반도체 後 고덕 독점, 외곽 개발 중단'); a1.set_xlabel('승인연도'); a1.set_ylabel('신규 세대수'); a1.legend(fontsize=9); a1.grid(alpha=0.3,axis='y')
a2.plot(YEARS,share,'D-',color='#a2d',lw=2.6)
for x,l in [(2017,'P1'),(2020,'P2'),(2022,'P3')]: a2.axvline(x,color='blue',ls=':',lw=1.2)
a2.set_title('평택 신규 개발 중 고덕권 점유율\n반도체 前 ~1% → 後 70%+'); a2.set_xlabel('승인연도'); a2.set_ylabel('고덕권 점유율(%)'); a2.grid(alpha=0.3); a2.set_ylim(0,100)
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/13_development_concentration.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
print(f"고덕권 신규세대 2015 {near.get(2015)} → 2024 {near.get(2024)} / 점유율 {share[YEARS.index(2015)]:.0f}%→{share[YEARS.index(2024)]:.0f}%")
