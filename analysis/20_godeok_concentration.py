"""[EN] Growth concentration in Godeok — Fig. 1. Godeok vs the rest of Pyeongtaek.
#고덕 집중 — 고덕 vs 평택(고덕 제외). 평택이 고르게 큰 게 아니라 고덕에 집중.
데이터: pyeongtaek_godeok_vs_rest_2013_2025.csv (KOSIS DT_1B04005N 읍면동).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
C=DATA_ROOT + '/population/pyeongtaek_godeok_vs_rest_2013_2025.csv'
rows=list(csv.DictReader(open(C,encoding='utf-8-sig')))
yr=[int(r['year']) for r in rows]
god=[int(r['godeok']) for r in rows]; exg=[int(r['pyeongtaek_ex_godeok']) for r in rows]; tot=[int(r['pyeongtaek_total']) for r in rows]
g0,e0=god[0],exg[0]
fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('Population growth in Pyeongtaek is concentrated in Godeok',fontsize=14,fontweight='bold')
# 패널1: 지수 2013=100
a1.plot(yr,[g/g0*100 for g in god],'o-',color='#e33',lw=2.6,label=f'Godeok (myeon+dong)  ×{god[-1]/g0:.1f}')
a1.plot(yr,[e/e0*100 for e in exg],'s--',color='#38a',lw=2.4,label=f'Pyeongtaek ex-Godeok  ×{exg[-1]/e0:.2f}')
a1.axhline(100,color='gray',lw=1); a1.axvline(2020,color='gray',ls=':',lw=1.2); a1.text(2020.1,480,'Godeok New Town\nfirst occupancy',fontsize=8,color='gray')
a1.set_title('Population index (2013=100)\nGodeok x5.7 vs rest of Pyeongtaek x1.2'); a1.set_xlabel('Year'); a1.set_ylabel('Index (2013=100)'); a1.legend(fontsize=9.5); a1.grid(alpha=0.3)
# 패널2: 고덕 비중 + 최근 순증 귀속
a2.plot(yr,[g/t*100 for g,t in zip(god,tot)],'D-',color='#a2d',lw=2.6)
a2.fill_between(yr,[g/t*100 for g,t in zip(god,tot)],alpha=0.12,color='#a2d')
a2.annotate(f'{god[0]/tot[0]*100:.1f}%',(yr[0],god[0]/tot[0]*100),fontsize=9,va='bottom')
a2.annotate(f'{god[-1]/tot[-1]*100:.1f}%',(yr[-1],god[-1]/tot[-1]*100),fontsize=10,fontweight='bold',ha='right',va='bottom',color='#a2d')
a2.set_title('Godeok share of Pyeongtaek population\n3.1% -> 12.7% (x4)'); a2.set_xlabel('Year'); a2.set_ylabel('Godeok share of Pyeongtaek (%)'); a2.grid(alpha=0.3)
# 최근 순증 귀속 박스
d22=len(yr)-1; i22=yr.index(2022)
gg=god[-1]-god[i22]; ee=exg[-1]-exg[i22]
a2.text(2013.3,10.5,f'Net change 2022-2025:\n Godeok +{gg:,}\n Rest {ee:+,}\n-> Recent growth is almost entirely Godeok',fontsize=8.5,
        bbox=dict(boxstyle='round',fc='#fff3f3',ec='#e33',alpha=0.9))
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/20_godeok_concentration.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
print(f"고덕 ×{god[-1]/g0:.2f} / ex-고덕 ×{exg[-1]/e0:.2f} / 비중 {god[0]/tot[0]*100:.1f}→{god[-1]/tot[-1]*100:.1f}%")
print(f"2022→2025: 고덕 {gg:+,} / 평택 나머지 {ee:+,}")
