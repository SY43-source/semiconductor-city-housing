"""[EN] Tenure turnover adjustment — converts transaction flow to housing stock.
#P3-점유 회전율 보정 — 거래건수(flow) → 재고(stock) 점유 변환.
문제: 실거래 건수는 회전율(계약주기)이 짧은 월세·전세가 과대집계(매매는 8~10년 보유→과소).
보정: stock_k ∝ 건수_k × 보유기간_k. 매매 보유기간 sensitivity(6/8/10년), 전세·월세=2년(임대차 2+2 하한 근사).
결과: 모델 규격수요(Dsize)에 flow/stock 두 점유매트릭스를 각각 적용 → 점유수요 비교.
데이터: godeok_tenure_by_size.csv (면적대별 매매/전세/월세 건수).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
EMP=DATA_ROOT + '/employment'
order=['소형<60','국평60-85','대형85+']
# 면적대별 거래건수
cnt={}
for r in csv.DictReader(open(f'{EMP}/godeok_tenure_by_size.csv')):
    cnt[r['size_band']]=np.array([int(r['sale']),int(r['jeonse']),int(r['wolse'])],float)  # [매매,전세,월세]
# 모델 규격수요(24 출력, 실측파생 고정)
Dsize=np.array([47.5,41.3,11.2]); Dsize=Dsize/Dsize.sum()

def tenure_of(counts, hold):
    """counts[매매,전세,월세] → 점유비율. hold=[매매,전세,월세] 보유기간(년). hold=None이면 flow(원건수)."""
    w=counts*np.array(hold) if hold else counts
    return w/w.sum()
def overall(hold):
    D=np.zeros(3)
    for i,s in enumerate(order):
        D+=Dsize[i]*tenure_of(cnt[s],hold)
    return D/D.sum()*100

flow=overall(None)
stock8=overall([8,2,2]); stock6=overall([6,2,2]); stock10=overall([10,2,2])
print("점유수요 (매매/전세/월세, %)")
print(f"  flow(원 거래건수)      : {flow[0]:.0f} / {flow[1]:.0f} / {flow[2]:.0f}")
print(f"  stock 보정(매매6년)    : {stock6[0]:.0f} / {stock6[1]:.0f} / {stock6[2]:.0f}")
print(f"  stock 보정(매매8년,기준): {stock8[0]:.0f} / {stock8[1]:.0f} / {stock8[2]:.0f}")
print(f"  stock 보정(매매10년)   : {stock10[0]:.0f} / {stock10[1]:.0f} / {stock10[2]:.0f}")

# 면적대별 stock 점유(기준 8년) 참고
print("\n면적대별 stock 점유(매매8년 보정, %)")
for s in order:
    t=tenure_of(cnt[s],[8,2,2])*100
    print(f"  {s:9s} 매매 {t[0]:.0f} / 전세 {t[1]:.0f} / 월세 {t[2]:.0f}")

fig,(a1,a2)=plt.subplots(1,2,figsize=(14,6))
fig.suptitle('Tenure turnover adjustment: flow vs stock',fontsize=13,fontweight='bold')
lab=['sale','jeonse','monthly']; x=np.arange(3); w=0.2
for j,(d,nm,c) in enumerate([(flow,'flow (counts)','#bbb'),(stock6,'stock 6y','#9cf'),(stock8,'stock 8y','#39c'),(stock10,'stock 10y','#036')]):
    a1.bar(x+(j-1.5)*w,d,w,label=nm,color=c)
    for i in range(3): a1.text(x[i]+(j-1.5)*w,d[i]+0.6,f'{d[i]:.0f}',ha='center',fontsize=7)
a1.set_xticks(x); a1.set_xticklabels(lab); a1.set_ylabel('%'); a1.set_title('Overall tenure demand'); a1.legend(fontsize=8); a1.grid(alpha=0.3,axis='y')
# 면적대별 stock
sm=np.array([tenure_of(cnt[s],[8,2,2])*100 for s in order])
btm=np.zeros(3)
for k,(nm,c) in enumerate([('sale','#c62'),('jeonse','#2a8'),('monthly','#39c')]):
    a2.bar(range(3),sm[:,k],bottom=btm,label=nm,color=c)
    for i in range(3):
        if sm[i,k]>4: a2.text(i,btm[i]+sm[i,k]/2,f'{sm[i,k]:.0f}',ha='center',fontsize=8,color='white',fontweight='bold')
    btm+=sm[:,k]
a2.set_xticks(range(3)); a2.set_xticklabels(['Small<60','Standard 60-85','Large 85+']); a2.set_ylabel('%'); a2.set_title('Tenure by size band (stock, 8-yr)'); a2.legend(fontsize=8); a2.grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/26_tenure_stock_adjust.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
