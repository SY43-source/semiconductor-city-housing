"""[EN] Age structure of Godeok inflow — Fig. 2. Working-age 25-39 plus young children.
#고덕 연령 구성 — 젊은 근로연령(25-39) + 어린 자녀 유입. v5 §4.2.
데이터: KOSIS DT_1B04005N 읍면동 5세별, 고덕면(4122033000)+고덕동(4122066000).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import os,sys
from collections import defaultdict
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
from kosis_client import kosis_get  # 분당 200건 제한 자동 스로틀+백오프
def call(code):
    return kosis_get({'method':'getList','orgId':'101','tblId':'DT_1B04005N',
       'objL1':code,'objL2':'ALL','itmId':'T2','prdSe':'Y','startPrdDe':'2018','endPrdDe':'2025'})
pop=defaultdict(lambda:defaultdict(int))
for c in ['4122033000','4122066000']:
    for x in call(c):
        if x.get('DT'): pop[int(x['PRD_DE'])][x['C2_NM']]+=int(x['DT'])
def b(y,ns): return sum(pop[y].get(n,0) for n in ns)
GROUPS=[('0-4\ninfants',['0 - 4세']),('5-19\nteens',['5 - 9세','10 - 14세','15 - 19세']),
        ('20-24',['20 - 24세']),('25-39\ncore working',['25 - 29세','30 - 34세','35 - 39세']),
        ('40-49\nparents',['40 - 44세','45 - 49세']),('50+',['50 - 54세','55 - 59세','60 - 64세','65 - 69세','70 - 74세','75 - 79세','80 - 84세','85세이상'])]
labels=[g[0] for g in GROUPS]
v2018=[b(2018,g[1]) for g in GROUPS]; v2025=[b(2025,g[1]) for g in GROUPS]
infl=[b-a for a,b in zip(v2018,v2025)]
fig,(a1,a2)=plt.subplots(1,2,figsize=(15,6))
fig.suptitle('Age structure of Godeok population: working age (25-39) plus young children',fontsize=14,fontweight='bold')
x=np.arange(len(labels)); w=0.38
a1.bar(x-w/2,[v/1000 for v in v2018],w,color='#bbb',label='2018')
a1.bar(x+w/2,[v/1000 for v in v2025],w,color='#e33',label='2025')
a1.set_xticks(x); a1.set_xticklabels(labels,fontsize=8.5); a1.set_ylabel('Population (thousands)'); a1.set_title('Population by age band, 2018 vs 2025'); a1.legend(); a1.grid(alpha=0.3,axis='y')
cols=['#c63' if '25-39' in l else '#37a' if ('5-19' in l or '0-4' in l) else '#999' for l in labels]
a2.bar(x,[v/1000 for v in infl],color=cols)
for i in x: a2.text(i,infl[i]/1000+0.3,f'+{infl[i]/1000:.1f}k',ha='center',fontsize=8.5,fontweight='bold')
a2.set_xticks(x); a2.set_xticklabels(labels,fontsize=8.5); a2.set_ylabel('Inflow (thousands, 2018-2025)')
w2539=infl[labels.index('25-39\ncore working')]; y519=infl[labels.index('5-19\nteens')]
a2.set_title(f'Net inflow 2018-2025\nCore working (25-39) = {w2539/y519:.1f}x teens (5-19)'); a2.grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/22_godeok_age.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
print(f"25-39 유입 {w2539:,} / 5-19 유입 {y519:,} ({w2539/y519:.1f}배)")
