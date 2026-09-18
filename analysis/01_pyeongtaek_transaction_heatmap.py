"""[EN] Pyeongtaek apartment transactions — unit-size x era activity heatmap.
평택 아파트 실거래 규격 분석 — 면적대 × 시대 거래활발도 + P1(2017) 전후 shift.
데이터: shared_data/realprice/realprice_apt_trade.csv (평택 70,615건)
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

ROWS = [r for r in csv.DictReader(open('/Users/Shared/seoyeon_research/realprice/realprice_apt_trade.csv', encoding='utf-8-sig'))
        if r['region'] == '평택시' and r['excluUseAr'] and r['dealYear']]

AREA_BINS = [(0,60,'~60㎡\n(소형)'),(60,85,'60-85㎡\n(국평3방)'),(85,102,'85-102㎡'),
             (102,135,'102-135㎡\n(4방)'),(135,999,'135㎡+\n(대형)')]
def abin(a):
    a=float(a)
    for lo,hi,lab in AREA_BINS:
        if lo<=a<hi: return lab
    return '기타'

fig, axes = plt.subplots(2, 2, figsize=(15, 11))
fig.suptitle('평택 아파트 실거래 규격 분석 (2015–2025, 70,615건)\n삼성 반도체 P1 가동 2017', fontsize=15, fontweight='bold')

# ── 1. 면적대 × 거래연도 히트맵 ──
years = list(range(2015,2026))
labels = [l for _,_,l in AREA_BINS]
mat = np.zeros((len(labels), len(years)))
for r in ROWS:
    y=int(r['dealYear'])
    if 2015<=y<=2025:
        lab=abin(r['excluUseAr'])
        if lab in labels:
            mat[labels.index(lab)][years.index(y)] += 1
ax=axes[0,0]
im=ax.imshow(mat, aspect='auto', cmap='YlOrRd')
ax.set_xticks(range(len(years))); ax.set_xticklabels(years, rotation=45, fontsize=8)
ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels, fontsize=8)
ax.axvline(years.index(2017)-0.5, color='blue', ls='--', lw=2, label='P1 2017')
ax.set_title('면적대 × 거래연도 (건수 히트맵)'); ax.legend(fontsize=8)
fig.colorbar(im, ax=ax, fraction=0.046)

# ── 2. 면적대별 거래 비중 — P1 전후 ──
ax=axes[0,1]
pre=[r for r in ROWS if 2015<=int(r['dealYear'])<=2016]
post=[r for r in ROWS if 2020<=int(r['dealYear'])<=2024]
pre_c=Counter(abin(r['excluUseAr']) for r in pre)
post_c=Counter(abin(r['excluUseAr']) for r in post)
x=np.arange(len(labels)); w=0.35
ax.bar(x-w/2,[pre_c.get(l,0)/len(pre)*100 for l in labels],w,label='2015-16(P1전)',color='#88a')
ax.bar(x+w/2,[post_c.get(l,0)/len(post)*100 for l in labels],w,label='2020-24(P1후)',color='#e55')
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=7)
ax.set_ylabel('거래 비중(%)'); ax.set_title('P1(2017) 전후 면적대 거래비중 변화'); ax.legend(fontsize=8)

# ── 3. 분양시기(buildYear)대별 거래 평균 전용면적 ──
ax=axes[1,0]
by=defaultdict(list)
for r in ROWS:
    if r['buildYear'] and int(r['buildYear'])>1970:
        by[(int(r['buildYear'])//5)*5].append(float(r['excluUseAr']))
eras=sorted([e for e in by if len(by[e])>50])
ax.plot(eras,[np.mean(by[e]) for e in eras],'o-',color='#c33',lw=2)
ax.set_xlabel('분양시기(건축연도)'); ax.set_ylabel('평균 전용면적(㎡)')
ax.set_title('분양시기대별 거래 아파트 평균면적\n(대형화→소형화 회귀)'); ax.grid(alpha=0.3)
for e in eras:
    ax.annotate(f'{np.mean(by[e]):.0f}',(e,np.mean(by[e])),fontsize=7,ha='center',va='bottom')

# ── 4. 연도별 국평(60-85) 거래 비중 추이 ──
ax=axes[1,1]
gukpyeong=[]
allc=[]
for y in years:
    yr=[r for r in ROWS if int(r['dealYear'])==y]
    g=sum(1 for r in yr if 60<=float(r['excluUseAr'])<85)
    gukpyeong.append(g/len(yr)*100 if yr else 0)
ax.plot(years,gukpyeong,'s-',color='#2a7',lw=2)
ax.axvline(2017,color='blue',ls='--',lw=2,label='P1 2017')
ax.set_xlabel('거래연도'); ax.set_ylabel('국평(60-85㎡) 거래비중(%)')
ax.set_title('국평(3방) 거래비중 추이\n반도체 가족 유입 신호'); ax.legend(fontsize=8); ax.grid(alpha=0.3)

plt.tight_layout(rect=[0,0,1,0.96])
out=REPO + '/analysis/01_pyeongtaek_transaction_heatmap.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'✅ {out}')
print(f'   분석 거래: {len(ROWS):,}건')
