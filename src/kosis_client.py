"""[EN] Shared client for the KOSIS OpenAPI (Statistics Korea), with rate limiting.
KOSIS OpenAPI 공용 클라이언트 — 분당 200건 제한(2026-07-15 시행) 대응.

정책(2026-07-15 KOSIS 공지): 1분간 호출 200건 초과 시 err=40 반환·차단.
본 모듈은 그 제한을 자동 준수하며 "끊김 없이" 데이터를 받도록:
  1) 선제 스로틀 — rolling 60초 윈도우에서 최대 LIMIT(190, 안전마진 10)건. 초과 예정이면 오래된 호출이 만료될 때까지 sleep.
  2) 백오프 재시도 — 그래도 err=40이 오면 윈도우 리셋까지 대기 후 재시도(최대 MAX_RETRY).
  3) 네트워크 오류 지수 백오프.

사용:
    from kosis_client import kosis_get
    rows = kosis_get({'method':'getList','orgId':'101','tblId':'DT_1JC1516',
                      'objL1':'31070','objL2':'00','itmId':'T10','prdSe':'Y',
                      'startPrdDe':'2024','endPrdDe':'2024'})  # apiKey/format/jsonVD 자동주입
    meta = kosis_get({'method':'getMeta','orgId':'101','tblId':'DT_1JC1516','type':'ITM'}, endpoint='data')

반환: 파싱된 JSON(대개 list). err=40 이외의 err(20/21/30 등)는 그대로 dict로 반환(호출자가 판단; 파라미터 탐색 등).
"""
import os, json, time, urllib.request, urllib.parse

_ENDPOINTS = {
    'param': 'https://kosis.kr/openapi/Param/statisticsParameterData.do',
    'data':  'https://kosis.kr/openapi/statisticsData.do',
}
LIMIT = 190          # 분당 200 - 안전마진 10
WINDOW = 60.0        # 초
MAX_RETRY = 6
UA = {'User-Agent': 'Mozilla/5.0'}
_calls = []          # 최근 호출 timestamps (monotonic), 프로세스 로컬

def _throttle():
    """rolling 60초 윈도우 기준 LIMIT 초과 예정이면 sleep."""
    now = time.monotonic()
    cutoff = now - WINDOW
    while _calls and _calls[0] < cutoff:
        _calls.pop(0)
    if len(_calls) >= LIMIT:
        wait = _calls[0] + WINDOW - now + 0.1
        if wait > 0:
            print(f"  [throttle] 분당 {LIMIT}건 근접 → {wait:.1f}s 대기")
            time.sleep(wait)
        _throttle()  # 재정리

def kosis_get(params, endpoint='param', timeout=60):
    base = _ENDPOINTS[endpoint]
    p = dict(params)
    p.setdefault('apiKey', os.environ['KOSIS_API_KEY'])
    p.setdefault('format', 'json')
    p.setdefault('jsonVD', 'Y')
    url = base + '?' + urllib.parse.urlencode(p)
    for attempt in range(MAX_RETRY):
        _throttle()
        try:
            _calls.append(time.monotonic())
            raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()
            data = json.loads(raw)
        except Exception as e:
            back = 2 ** attempt
            print(f"  [net err] {e} → {back}s 후 재시도 ({attempt+1}/{MAX_RETRY})")
            time.sleep(back)
            continue
        # 레이트리밋 err=40 → 윈도우 만료까지 대기 후 재시도
        if isinstance(data, dict) and str(data.get('err')) == '40':
            # 다음 윈도우 시작까지 대기 (가장 오래된 호출 + 60초)
            now = time.monotonic()
            wait = (_calls[0] + WINDOW - now + 1.0) if _calls else (WINDOW + 1.0)
            wait = max(wait, 5.0)
            print(f"  [err40 호출초과] {wait:.0f}s 대기 후 재시도 ({attempt+1}/{MAX_RETRY})")
            time.sleep(wait)
            _calls.clear()
            continue
        return data
    raise RuntimeError(f"KOSIS 호출 {MAX_RETRY}회 재시도 실패: {url[:120]}")
