"""[EN] [Template] Parameterized transaction heatmap for any semiconductor city.
[템플릿] 반도체 도시 아파트 실거래 규격 분석 — 도시 파라미터화.

서연이 사용법:
  python3 analysis/transaction_heatmap_template.py --city 평택시
  python3 analysis/transaction_heatmap_template.py --city 용인      # 용인 3구 합산
  python3 analysis/transaction_heatmap_template.py --city 이천시
  python3 analysis/transaction_heatmap_template.py --city 평택시 --fab-year 2017

옵션:
  --city      지역명 (부분일치. '용인' 이면 용인수지/기흥/처인 모두)
  --fab-year  반도체 공장 가동 연도 (세로선 표시, 기본 2017)

산출: analysis/heatmap_<city>.png
데이터: shared_data/realprice/realprice_apt_trade.csv
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv, argparse
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

CSV = '/Users/Shared/seoyeon_research/realprice/realprice_apt_trade.csv'
AREA_BINS = [(0,60,'~60㎡\n(소형)'),(60,85,'60-85㎡\n(국평3방)'),(85,102,'85-102㎡'),
             (102,135,'102-135㎡\n(4방)'),(135,999,'135㎡+\n(대형)')]

def abin(a):
    a=float(a)
    for lo,hi,lab in AREA_BINS:
        if lo<=a<hi: return lab
    return '기타'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--city', required=True, help="지역명 (부분일치)")
    ap.add_argument('--fab-year', type=int, default=2017, help="공장 가동 연도")
    args = ap.parse_args()

    rows = [r for r in csv.DictReader(open(CSV, encoding='utf-8-sig'))
            if args.city in r['region'] and r['excluUseAr'] and r['dealYear']]
    if not rows:
        print(f"[!] '{args.city}' 거래 없음. region 값: 평택시/용인수지구/용인기흥구/용인처인구/이천시")
        return
    print(f"▶ {args.city}: {len(rows):,}건 분석")

    labels=[l for _,_,l in AREA_BINS]; fy=args.fab_year
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    fig.suptitle(f'{args.city} 아파트 실거래 규격 분석 ({len(rows):,}건)\n반도체 공장 가동 {fy}', fontsize=15, fontweight='bold')

    # 1. 면적대 × 연도 히트맵
    years=list(range(2015,2026))
    mat=np.zeros((len(labels),len(years)))
    for r in rows:
        y=int(r['dealYear'])
        if 2015<=y<=2025 and abin(r['excluUseAr']) in labels:
            mat[labels.index(abin(r['excluUseAr']))][years.index(y)] += 1
    ax=axes[0,0]; im=ax.imshow(mat,aspect='auto',cmap='YlOrRd')
    ax.set_xticks(range(len(years))); ax.set_xticklabels(years,rotation=45,fontsize=8)
    ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels,fontsize=8)
    if 2015<=fy<=2025: ax.axvline(years.index(fy)-0.5,color='blue',ls='--',lw=2,label=f'가동 {fy}'); ax.legend(fontsize=8)
    ax.set_title('면적대 × 거래연도 (건수)'); fig.colorbar(im,ax=ax,fraction=0.046)

    # 2. 가동 전후 면적대 비중
    ax=axes[0,1]
    pre=[r for r in rows if fy-2<=int(r['dealYear'])<fy]
    post=[r for r in rows if fy+3<=int(r['dealYear'])<=fy+7]
    if pre and post:
        pc=Counter(abin(r['excluUseAr']) for r in pre); qc=Counter(abin(r['excluUseAr']) for r in post)
        x=np.arange(len(labels)); w=0.35
        ax.bar(x-w/2,[pc.get(l,0)/len(pre)*100 for l in labels],w,label=f'가동前',color='#88a')
        ax.bar(x+w/2,[qc.get(l,0)/len(post)*100 for l in labels],w,label=f'가동後',color='#e55')
        ax.set_xticks(x); ax.set_xticklabels(labels,fontsize=7); ax.legend(fontsize=8)
    ax.set_ylabel('거래비중(%)'); ax.set_title('공장 가동 전후 면적대 비중')

    # 3. 분양시기별 평균면적
    ax=axes[1,0]
    by=defaultdict(list)
    for r in rows:
        if r['buildYear'] and int(r['buildYear'])>1970:
            by[(int(r['buildYear'])//5)*5].append(float(r['excluUseAr']))
    eras=sorted([e for e in by if len(by[e])>30])
    if eras:
        ax.plot(eras,[np.mean(by[e]) for e in eras],'o-',color='#c33',lw=2)
        for e in eras: ax.annotate(f'{np.mean(by[e]):.0f}',(e,np.mean(by[e])),fontsize=7,ha='center',va='bottom')
    ax.set_xlabel('분양시기'); ax.set_ylabel('평균 전용(㎡)'); ax.set_title('분양시기별 거래 평균면적'); ax.grid(alpha=0.3)

    # 4. 국평 비중 추이
    ax=axes[1,1]
    gp=[]
    for y in years:
        yr=[r for r in rows if int(r['dealYear'])==y]
        gp.append(sum(1 for r in yr if 60<=float(r['excluUseAr'])<85)/len(yr)*100 if yr else 0)
    ax.plot(years,gp,'s-',color='#2a7',lw=2)
    if 2015<=fy<=2025: ax.axvline(fy,color='blue',ls='--',lw=2,label=f'가동 {fy}'); ax.legend(fontsize=8)
    ax.set_xlabel('거래연도'); ax.set_ylabel('국평(60-85㎡) 비중(%)'); ax.set_title('국평(3방) 거래비중 추이'); ax.grid(alpha=0.3)

    plt.tight_layout(rect=[0,0,1,0.96])
    safe=args.city.replace('/','_')
    out=f'{REPO}/analysis/heatmap_{safe}.png'
    plt.savefig(out,dpi=120,bbox_inches='tight')
    print(f'✅ {out}')

if __name__=='__main__':
    main()
