# REF — 국토부 실거래가 공개시스템(rt.molit.go.kr) CSV 다운로드 경로

> **재사용 레퍼런스**: data.go.kr OpenAPI가 특정 시군구에 **빈 응답(0)** 을 줄 때(행정통합·구 신설로 구 코드 폐기), 이 경로로 우회 수집.
> 리버스·검증: 2026-07-06 (광주 5구 228,649건 성공). 스크립트: [`src/molit_rt_download.py`](../../src/molit_rt_download.py). 데이터 카탈로그: [`DATA_SOURCES.md`](DATA_SOURCES.md) D1b.

---

## 1. 언제 이 경로를 쓰나
- data.go.kr `RTMSDataSvcAptTrade`(OpenAPI)가 `resultCode=000`인데 **totalCount=0**을 전 연도 반환할 때.
- 원인은 대개 **행정구역 개편으로 구 법정동 코드 폐기**(OpenAPI는 구 코드 유지, 공개시스템은 신 코드 이전). 실측 예: 광주(29xxx→12xxx), 화성(구 신설), 인천 중구(영종/제물포 개편).
- OpenAPI가 정상인 지역(평택·서울 등)은 기존 `molit_realprice.py`를 그대로 쓰면 됨.

## 2. 호출 흐름 (3단계)
```
1) GET  https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=      → 세션 쿠키 확보
2) POST https://rt.molit.go.kr/pt/xls/ptXlsDownDataCheck.do → {"cnt": N} (0이면 조건/코드 오류)
3) POST https://rt.molit.go.kr/pt/xls/ptXlsCSVDown.do       → CSV 본문 (cp949 인코딩)
```
- **인증 불필요**(세션 쿠키만). **TLS 지문 검사 → `curl_cffi(impersonate='chrome124')` 필수**(urllib/requests 차단).
- CSV 상단 ~16줄은 안내문 → 데이터는 `"NO"`로 시작하는 헤더행부터.

## 3. POST 파라미터 (아파트 매매 기준)
| 파라미터 | 값 | 의미 |
|---|---|---|
| `srhThingNo` | `A` | 물건종류=아파트 |
| `srhDelngSecd` | `1` | 거래구분=매매 |
| `srhThingSecd` | `A` | (병기) |
| `srhAddrGbn` | `1` | 지번주소 |
| `srhLfstsSecd` | `1` | |
| `srhSidoCd` | 예 `12000` | **시도(신 코드)** |
| `srhSggCd` | 예 `12330` | **시군구(신 코드)** |
| `srhEmdCd` | `` | 읍면동(전체는 빈값) |
| `srhFromDt` / `srhToDt` | `YYYY-MM-DD` | **형식 엄격**(`YYYYMM`·`YYYY.MM` 전부 거부) |
| `sggNm` | 예 `광산구` | 표시용 |

> ⚠️ **함정**: ① 날짜는 반드시 `YYYY-MM-DD`. ② 응답 인코딩 **cp949**(utf-8 아님). ③ 세션 없이 POST하면 실패 → 반드시 1)단계 선행.
> ④ **일일 다운로드 100건 제한(IP당)**: 초과 시 datacheck가 `{"error":"일일 다운로드 횟수는 최대 100건 입니다."}`, CSV 빈 응답. 신선 세션·간격 무관, 다음날 리셋.
> ⑤ **시도별 자료는 계약일자 범위 최대 1년**(`시도별 자료제공 계약일자 범위는 최대 1년입니다`): 전체기간 1회 다운로드 **불가** → **반드시 연도별(1년씩)**. ∴ 구당 11회 필요. ④+⑤ 조합 = 하루 최대 ~9개 구(구×11년<100). 대량은 며칠 분할. (시군구 단위면 1년 제한 없을 수 있으나 광주=시도(전남광주통합) 하위라 적용됨)

## 4. 지역 코드 조회 (신 행정코드)
- **시도 목록**: `GET /data/sido.do` → `[{"signguCode":"12000","ctprvnNm":"전남광주통합특별시"}, ...]`
- **시군구 목록**: `GET /data/sgg.do?signguCode=<시도코드 앞2자리>` (예 `12`) → 하위 시군구 코드
  - JS 원본: `signguCode : $("#srhSidoCd option:selected").val().substr(0,2)` — **반드시 앞 2자리**.
- **읍면동**: `GET /cmm/ptEmdList.do` (frm_xls serialize 전달) — 신고자료 있는 동만.

### 확보된 신 코드 (전남광주통합특별시, 2026-07-06)
| 지역 | 신 코드 | 지역 | 신 코드 |
|---|---|---|---|
| 광산구(군공항) | `12330` | 북구 | `12300` |
| 서구 | `12240` | 남구 | `12270` |
| 동구 | `12210` | 장성군(SK후보) | `12840` |
| 나주시 | `12170` | 목포·여수·순천 | 12110·12130·12150 |
> 시도 `12000` = 전남광주통합특별시. 군공항 부지=광산구, 인근 동=송정·도산·신촌·우산·신가·수완·장덕.

## 5. 스크립트 사용
```bash
python3 src/molit_rt_download.py --sido 12000 --sgg 12330 --name 광산구 --slug gwangju_gwangsan --years 2015 2025
# 여러 구 반복 후 병합 → realprice_apt_trade_<슬러그>.csv (기존 스키마 정규화 + dealType)
```
- 출력 스키마: `lawd,region,ym,aptNm,excluUseAr,dealAmount,floor,buildYear,dealYear,dealMonth,dealDay,umdNm,jibun,dealType`
  (기존 `realprice_apt_trade.csv`와 호환 → 01~03 분석 스크립트 그대로 사용 가능)
- 원본 CSV엔 매수자·매도자·등기일자·도로명도 있음(필요 시 스키마 확장).

## 6. 검증 체크
- [ ] `ptXlsDownDataCheck.do` 의 `cnt` > 0 (0이면 코드/날짜/조건 재확인)
- [ ] 다운로드 행수 == cnt (광산구 2024: cnt 4,436 = 행수 4,436 ✅)
- [ ] `umdNm`(동) 정상 파싱 → 부지 인근 동 필터 가능
- [ ] cp949 디코딩(한글 깨짐 없음)

## 관련
- [[DATA_SOURCES]] D0(행정통합)·D1b · [[DATA_READINESS_AND_LITERATURE]] A.3(③ 광주 예측)
- 대체 경로 후보: 한국부동산원 R-ONE, KOSIS 실거래 통계 (미검증)
