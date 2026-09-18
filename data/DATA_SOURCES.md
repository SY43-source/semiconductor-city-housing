# 데이터 출처 레퍼런스 (DATA SOURCES) — 재현·검증용

> **용도**: 본 연구에 쓰인 **모든 데이터의 출처·수집방법·파일·주의사항**을 한 곳에 정리. 나중에 누구나 검증·재현 가능하게.
> 논문 참고문헌(선행 논문)은 [`PAPER_DRAFT.md`](PAPER_DRAFT.md) §10 · [`PAPER_WRITING_GUIDE.md`](PAPER_WRITING_GUIDE.md) §7 · [`DATA_READINESS_AND_LITERATURE.md`](DATA_READINESS_AND_LITERATURE.md) Part B 참고.
> 갱신: 2026-07-06

---

## 0. 한눈 요약 (데이터셋 × 출처)

| # | 데이터셋 | 출처기관 | 표ID/API | 수록기간 | 산출 파일 |
|---|---|---|---|---|---|
| D1 | 아파트 매매 실거래 | 국토교통부 (공공데이터포털) | RTMSDataSvcAptTrade (15126469) | 2015~2025 | `realprice/realprice_apt_trade.csv`(+`_anseong.csv`) |
| D2 | 5세별 인구 | 통계청 KOSIS | DT_1B04005N | 2011~2025 | `population/city_population_5yr_2011_2025.csv` |
| D3 | 1인가구 비율 | 통계청 KOSIS (등록센서스) | DT_1YL21161 | 2015~2024 | `population/city_1person_household_2015_2024.csv` |
| D3b | **가구원수별 가구(실측)** | 통계청 KOSIS 인구총조사 | **DT_1JC1516** | 2015~2024 | `employment/pyeongtaek_hhsize_2015_2024.csv` |
| D3c | **가구주연령×가구원수(실측)** | 통계청 KOSIS 인구총조사 | **DT_1JC1511** | 2024 | `employment/pyeongtaek_head_age_hhsize_2024.csv` (+ `pyeongtaek_headship_2024.csv`) |
| D3d | 고덕 점유(매매/전세/월세) | 국토부 실거래(매매+전월세) | 파생 | 2015~2025 | `employment/godeok_tenure_by_size.csv` |
| D4 | 주민등록 인구(시군구, 장기) | 통계청 KOSIS | DT_1B040A3 | 평택 1992~/안성 2000~ | (차트용, 아래 D6에 통합) |
| D5 | 인구총조사 장기(1966~) | 통계청 인구총조사 | (레거시표·편찬치) | 1966~2015 | `population/city_longterm_pop_1966_2024.csv` |
| D6 | 장기 인구 추세(통합) | D4+D5 stitch | — | 1966~2024 | `population/city_longterm_pop_1966_2024.csv` |
| D7 | 아파트 단지/평형 메타 | NAVER 부동산 | front-api/v1 | 1956~2026 | master sqlite (6,244단지) |
| D8 | 평면도 이미지 | NAVER 2D + NH | — | — | `floorplans/` (118장) |

> **공통 경로**: 데이터는 `/Users/Shared/seoyeon_research/`(= 프로젝트 `shared_data/` 심볼릭). API 키는 `.secrets.env`(값은 코드/문서에 하드코딩 금지 — 환경변수명만 기재).

---

## ⚠️ D0. 광주 = "전남광주통합특별시"(신 코드 12xxx) — 행정통합 (2026, 필독)
- **발견(2026-07-06)**: data.go.kr OpenAPI가 광주(29xxx)·화성(41590)·인천중구(28110)에 **전 연도 0** 반환. 원인=코드·키·엔드포인트 아님(모두 정상 검증). **2025~26 행정개편으로 광주광역시+전라남도 → "전남광주통합특별시"(신 시도코드 12000)로 통합**, 공개시스템은 신 코드로 이전했으나 **OpenAPI는 구 29xxx를 계속 써서 빈 응답**.
- **광주 자치구 신 코드** (rt.molit.go.kr `/data/sgg.do?signguCode=12`): 동구 `12210`·서구 `12240`·남구 `12270`·북구 `12300`·**광산구 `12330`**(군공항 부지). 전남 시군도 12xxx(장성군 `12840`·나주 `12170` 등).
- **군공항 부지** = 광산구(12330). 인근 동: 송정·도산·신촌·우산·신가·수완·장덕(rt CSV `umdNm` 필터).
- **수집 경로**: OpenAPI ❌ → **국토부 실거래가 공개시스템(rt.molit.go.kr) CSV 다운로드**(D1b). 신 코드 12xxx로 정상.

## D1. 아파트 매매 실거래가 (OpenAPI)
- **출처**: 국토교통부 「아파트 매매 실거래가 자료」 (공공데이터포털 data.go.kr, 서비스 15126469)
- **엔드포인트**: `https://apis.data.go.kr/1613000/RTMSDataSvcAptTrade/getRTMSDataSvcAptTrade`
- **파라미터**: `LAWD_CD`(법정동 5자리), `DEAL_YMD`(YYYYMM), `pageNo`, `numOfRows`
- **인증키(env)**: `DATA_GO_KR_KEY`  · **주의**: data.go.kr WAF가 TLS지문 검사 → `curl_cffi(impersonate=chrome124)` 필수(urllib=403)
- **수집 지역(LAWD)**: 평택 `41220` / 용인 `41461·41463·41465` / 이천 `41500` / **안성 `41550`**(대조도시, 2026-07-06 추가)
- **수집 스크립트**: `src/molit_realprice.py`(평택·용인·이천) · `src/molit_realprice_control.py`(안성, 비파괴 별도파일)
- **산출**: `realprice/realprice_apt_trade.csv`(253,256건, 평택 70,615) · `realprice/realprice_apt_trade_anseong.csv`(27,733건)
- **⚠️ caveat**: 화성 `41590`·광주 `29xxx`·인천중구 `28110`는 API가 0 반환(행정통합/구 신설로 구 코드 폐기, D0 참조) → OpenAPI 미수집. 조회일 이후 실거래는 신고지연으로 최근월 과소.

## D1b. 아파트 매매 실거래가 (공개시스템 CSV — 광주 등 OpenAPI 결측 지역)
> 📘 **재사용 방법 상세(엔드포인트·파라미터·신코드·함정) → [`REF_molit_rt_download.md`](REF_molit_rt_download.md)**
- **출처**: 국토부 **실거래가 공개시스템** `https://rt.molit.go.kr` (신 행정코드 12xxx 정상)
- **흐름**: `GET /pt/xls/xls.do`(세션) → `POST /pt/xls/ptXlsDownDataCheck.do`(cnt 확인) → `POST /pt/xls/ptXlsCSVDown.do`(CSV, **cp949**)
- **핵심 파라미터**: `srhThingNo=A`(아파트)·`srhDelngSecd=1`(매매)·`srhSidoCd=12000`·`srhSggCd=<구코드>`·`srhFromDt/srhToDt=YYYY-MM-DD`(형식 엄격)·`srhAddrGbn=1`·`srhLfstsSecd=1`
- **인증**: 불필요(세션 쿠키만) · TLS `curl_cffi(chrome124)` 필수
- **스크립트**: `src/molit_rt_download.py` (`--sido --sgg --name --slug --years`, 기존 스키마로 정규화, 안내문 스킵)
- **산출**: `realprice/realprice_apt_trade_gwangju.csv`(광주 5구 병합) + `realprice_apt_trade_gj_<code>.csv`(구별)
- **컬럼(원본 추가)**: API 스키마 + `dealType`(중개/직거래), 원본엔 매수자·매도자·등기일자·도로명도 존재
- **검증(2026-07-06)**: 광산구 2024 cnt=4,436 = 다운로드 행수 일치. 군공항 인근 동(우산·송정·도산·수완 등) 필터 확인.
- **수집 결과(2026-07-06)**: 광주 5구 2015~2025 **228,649건** (북구70,491·광산구67,180·서구47,591·남구31,339·동구12,048). 군공항 인근 동 25,877건.
- **📦 부수효과**: `src/molit_rt_download.py` + `realprice_apt_trade_gwangju.csv`(병합) + `realprice_apt_trade_gj_{12210,12240,12270,12300,12330}.csv`(구별). 롤백 시 삭제.

## D2. 5세별 연령 인구
- **출처**: 통계청 KOSIS 「주민등록인구현황(성/연령/5세별)」 `DT_1B04005N`
- **엔드포인트**: `https://kosis.kr/openapi/Param/statisticsParameterData.do` (method=getList)
- **파라미터**: `orgId=101`, `tblId=DT_1B04005N`, `itmId=T2`(총인구), `objL1=<지역코드>`, `objL2=ALL`(연령), `prdSe=Y`
- **인증키(env)**: `KOSIS_API_KEY`
- **지역코드**: 평택 `41220`·용인 `41460`·화성 `41590`·이천 `41500`·광주광역시 `29`·장성 `46880` + **안성 `41550`**(추가)
- **스크립트**: `src/kosis_city_pop.py`(+ 안성 append 2026-07-06)
- **산출**: `population/city_population_5yr_2011_2025.csv` (2,971행, 안성 330행 포함)

## D3. 1인가구 비율
- **출처**: 통계청 KOSIS 「인구총조사(등록센서스) 1인가구」 `DT_1YL21161`
- **파라미터**: `orgId=101`, `tblId=DT_1YL21161`, `objL1=ALL`, `itmId=ALL`, `prdSe=Y` (지역명 C1_NM으로 필터)
- **인증키(env)**: `KOSIS_API_KEY`
- **스크립트**: `src/kosis_1person_hh.py`(+ 안성 append)
- **산출**: `population/city_1person_household_2015_2024.csv` (91행, 안성 10행 포함). 컬럼: `year,region,single_hh,total_hh,single_ratio`
- **⚠️ caveat**: 2025 미공개. census 계열은 Param API objL 까다로움. **백업본** `*.bak_20260706_165642.csv` 보존.

## D3b. 가구원수별 가구 (실측, gap 지수용)
- **출처**: 통계청 KOSIS 「세대구성 및 가구원수별 가구(일반가구) - 시군구」 `DT_1JC1516`
- **파라미터(★함정 해결)**: `orgId=101`, `tblId=DT_1JC1516`, `objL1=31070`(**평택 — KOSIS 레거시 시군구 순번코드**, 표준 41220 아님·경기=31), `objL2=00`(세대구성 '계'), `itmId=T10`(일반가구)/`T21~T25`(가구원수 1~5명), `prdSe=Y`
- **⚠️ 파라미터 교훈**: 이 표 지역코드는 표준 행정코드(41220)가 아니라 **DT_1YL21161과 동일한 레거시 순번코드**(평택=31070, 서울=11). 표준코드 넣으면 err21. objL2(세대구성) 계=`00`(다른 값 전부 err21). getMeta type=OBJ는 err30(미제공)이라, DT_1YL21161 지역코드로 교차 확인해 발견.
- **스크립트**: `src/kosis_hhsize_pyeongtaek.py` (python3.11)
- **산출**: `employment/pyeongtaek_hhsize_2015_2024.csv`. 평택 2024: 1인 37.3%·2인 27.3%·3인 18.5%·4인 13.3%·5인+ 3.0% (합계검증 차 0.65%=6인+ 별항 추정, 정규화 사용)
- **용도**: `analysis/21_gap_index_prototype.py` HH 분포 실측화, `21b` 기준 시나리오.

## D4. 주민등록 인구 (시군구 장기)
- **출처**: 통계청 KOSIS 「주민등록인구(시군구)」 `DT_1B040A3`
- **파라미터**: `orgId=101`, `tblId=DT_1B040A3`, `itmId=T20`(총인구수), `objL1=<지역코드>`, `prdSe=Y`
- **인증키(env)**: `KOSIS_API_KEY`
- **실측 수록범위**: 평택 `41220` **1992~** (단 1992-94=통합 前 옛 평택시) / 안성 `41550` **2000~**
- **용도**: D6 장기추세의 2020·2024 tail (평택 598,556 / 안성 193,949 = 2024)

## D5. 인구총조사 장기 (1966~2015)
- **출처**: 통계청 **인구총조사(census)**, 5년주기. 편찬치(경계재구성) 사용.
- **경계 재구성**: 평택 pre-1995 = **평택군 + 송탄시(1981~) + 옛 평택시(1986~) 합산** (1995.5 통합시 출범). 안성 = 안성군 → 안성시(1998 승격).
- **교차검증**: census vs 주민등록(D4) 차이 <1.5% (예: 평택 2015 census 457,873 vs 주민등록 460,532) → 시계열 일관.
- **KOSIS 레거시 표(참고, 존재하나 Param API 스키마 난해)**:
  - `orgId=110 / TX_11001_A324` 면적·세대·인구 **1970~1991**
  - `orgId=110 / TX_11001_A118` 면적·세대·인구 **1992~2000**
  - `orgId=101 / DT_1IN0001` 인구총조사 **1925~2010**(단 **시도 단위**, 시군구 없음)
- **⚠️ caveat**: 시군구 1970s는 위 레거시표가 objL 다단계라 API 직접추출 곤란 → 편찬치 인용. **안성 census 편찬치는 원출처 재확인 권장**(평택은 통계청 KOSIS 명시, 안성은 미명시). 정본화 시 통계청 원자료 대조.

## D6. 장기 인구 추세 (통합 데이터셋)
- **구성**: 1966~2015 = D5(인구총조사) / 2020·2024 = D4(주민등록). **측정기준 혼합** 명시.
- **스크립트**: `analysis/04_longterm_population_trend.py` (원천값 인라인 + CSV 저장)
- **산출**: `population/city_longterm_pop_1966_2024.csv` (26행). 컬럼: `year,region,population,source`(census/resident)
- **핵심 수치**: 평택 199,700(1970)→598,556(2024) ×3.0 / 안성 132,685→193,949 ×1.5. 격차 1.5배→3.1배.

## D9. 주택 규모별 공급 (신축 인허가) — '공급' 축
- **출처**: 국토교통부 KOSIS `DT_MLTM_668` 주택규모별 주택건설 인허가실적 (년 2007~2025). (준공 `DT_MLTM_5374`·착공 `DT_MLTM_5388` 월계도 있음)
- **파라미터**: `orgId=116`, `itmId=13103871095T1`(인허가실적), `objL1/objL2/objL3=ALL` (권역/시도/규모), `prdSe=Y`
- **규모(objL3)**: 40㎡이하·40~60·**60~85**·85~135·135초과 → 소형(<60)·국평(60-85)·대형(85+) 매핑. ⚠️ `계` 행 제외.
- **⚠️ 지역 한계**: **시도 단위만(경기·광주광역시). 평택·광산 시군구 없음.** 경기 시도평균은 서울인접 소형수요 혼입으로 평택 대표성 없음(소형 48% 착시). → **시군구 공급은 D9b(NAVER 단지메타)로 대체**.
- **스크립트**: `src/kosis_housing_supply.py` → `housing_supply/housing_permit_by_size_2007_2025.csv` (시도 참고용)

## D9b. 시군구 신축 공급 구성 (NAVER 단지메타) — 공급 축 *정본*
- **출처**: NAVER 단지 메타 sqlite `complexes.approval_year` + `pyeong_types.exclusive_area_m2·units_of_same_area` → 승인연도별 규모(소형/국평/대형) 세대수.
- **범위**: 평택(bjd 41220%) 319단지, 광주 5구(bjd 12210/12240/12270/12300/12330) 등. 산출은 `analysis/09_supply_vs_demand.py` 인라인.
- **핵심(정정)**: **평택 신축 소형 12→5~19%, 국평 60~89%** / 광주 5구 소형 ≈20% → 두 도시 모두 신축이 국평 편중, 소형(1인 적합) 극소 = **"건설사 국평 편중" 시군구 기준 성립**(경기 시도평균의 반대).
- **⚠️**: NAVER=현 등재 단지 스냅샷(2013+ 신축 양호), 소코호트 연도 표본변동.

## D10. 아파트 전월세 실거래 — '밀려남/모집단' 축
- **출처**: 국토부 실거래가 공개시스템 rt.molit `srhDelngSecd=2` (전월세). 스크립트 `src/molit_rt_rent.py`
- **코드**: 경기 sido `41000`(평택 41220·안성 41550), 광주 sido `12000`(5구). ※ OpenAPI `getRTMSDataSvcAptRent`는 403(별도 활용신청 필요)
- **컬럼(추가)**: 전월세구분·보증금·월세·계약구분·갱신요구권. 산출 `realprice_apt_rent_{pt,an,gwangju}.csv`
- **현황(2026-07-07 완료)**: 평택 156,330·안성 49,667·**광주 5구 254,926**(동13,842·서43,494·남36,851·북72,424·광산88,315). `realprice_apt_rent_gwangju.csv` 병합. analysis/10에 광주 반영 완료.
- **⚠️ 수집 제약 2종(REF §2)**: 일일 100다운로드/IP + **시도별 계약일자 범위 최대 1년** → 반드시 연도별. molit_rt_rent.py는 연도별 루프.

## D11. 평택 제조업 고용 (용량반응 dose) — 원인 축
- **출처**: KOSIS 통계청 `DT_118N_MONA49` (행정구역 시군구/산업별 고용, 반기 2018~2025)
- **파라미터**: `orgId=118`, `objL1=ZONE2017A313107`(평택), `objL2=IND201701`(광업·제조업 BC), `itmId=16118z1`(전체종사자), `prdSe=H`, `newEstPrdCnt=16` (PRD 형식 'YYYY0H', 예 202502)
- **스크립트/산출**: `analysis/15_dose_employment.py` → `employment/pyeongtaek_mfg_2018_2025.csv`
- **값**: 88,297(2018)→97,019(2025). 용량반응 r=0.66(고용↔고덕 가격배율, p=0.077). ⚠️ 2018~ 반기만(pre-2018 없음).
- 캠퍼스 라인 timeline(P1 2017·P2 2020·P3 2022·P4 ~2024·P5 2028): 삼성 뉴스룸·DART·평택시사(라인수 dose, analysis/14).

## D7. 아파트 단지/평형 메타
- **출처**: NAVER 부동산 `https://fin.land.naver.com/front-api/v1/` (`/complex`, `/complex/pyeongList`, `/complex/complexClusters`)
- **인증**: 쿠키 기반(`NAVER_LAND_COOKIE` env / `_state/.naver_cookie`), TLS `curl_cffi(chrome124)` 필수, rate ≥1초/요청
- **스크립트**: `src/crawl_naver.py`·`naver_enumerate.py`·`batch_naver_meta.py`·`city_batch.py`·`seoul_batch.py`
- **산출**: master sqlite (6,244단지 / 29,014평형, 서울 1956~2026 포함)
- **⚠️ 법적**: 내부 분석 한정, 상업적 재배포·외부 제공 금지. 429/403 시 즉시 중단.

## D8. 평면도 이미지
- **출처**: NAVER 2D 도면 + NH(농협) mm 도면 (`landthumb-phinf.pstatic.net`)
- **산출**: `floorplans/` 118장 (seoul_dual_validation 등). OCR = Gemma4(방/거실 mm, ±5~20%)
- **⚠️**: 원본 보존(resize 금지), 이미지 외부 노출 금지.

---

## 참고 — 선행 논문(문헌) 출처
데이터가 아닌 **논문 참고문헌**은 아래에 정리됨(중복 회피):
- 핵심 5편 + 훔칠 기법 → [`PAPER_WRITING_GUIDE.md`](PAPER_WRITING_GUIDE.md) §7
- 반도체·산업도시 주거예측 확장 5편 → [`DATA_READINESS_AND_LITERATURE.md`](DATA_READINESS_AND_LITERATURE.md) Part B
- 논문 References 최종본 → [`PAPER_DRAFT.md`](PAPER_DRAFT.md) §10

## 재현 체크리스트
- [ ] `.secrets.env`에 `DATA_GO_KR_KEY`, `KOSIS_API_KEY` 존재 (값은 비공개)
- [ ] `pip install curl_cffi` (data.go.kr·NAVER TLS 우회)
- [ ] 실거래 재수집: `DATA_GO_KR_KEY=... python3 src/molit_realprice_control.py --lawd 41550 --region 안성시 --slug anseong --years 2015 2025`
- [ ] KOSIS 재수집: `KOSIS_API_KEY=... python3 src/kosis_city_pop.py` / `kosis_1person_hh.py`
- [ ] 차트 재생성: `python3 analysis/0{1,2,3,4}_*.py`
