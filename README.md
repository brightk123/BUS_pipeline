# 서울시 버스도착 정보 API 기반 실시간 데이터 파이프라인 프로젝트 🚌

서울시 공공데이터포털 버스 도착 정보 API를 활용하여 **실시간 데이터를 수집 -> 가공 -> DB 적재**하는 파이프라인 프로젝트입니다. <br>
ETL(Extract, Transform, Load) 구조를 연습하기 위한 프로젝트이며, Python으로 작성되었습니다.

---
## 1. 프로젝트 구조
```plaintext
bus_pipeline/
├─ src/
│ ├─ main.py # ETL 전체 실행 (Extract → Transform → Load)
│ ├─ db.py # MySQL 연결 관리
│ ├─ fetch_bus.py # Extract 단계 (API 호출)
│ ├─ transform.py # Transform 단계 (데이터 가공)
│ └─ init.py
├─ .env # 환경 변수 (API KEY, DB 계정) → 비공개
├─ .env.example # 환경 변수 예시 파일 (예시 공개용)
├─ requirements.txt # 의존성 패키지
├─ .gitignore # 불필요/민감 파일 제외
└─ README.md
```
---
## 2. 사용 기술
- **Python** : requests, pandas, sqlalchemy, python-dotenv
- **DB** : MySQL
- **자동화** : Windows 작업 스케줄러 (주기 실행)

---

## 3. 결과 예시 (추후 추가 예정)
- **DB 테이블 구조**
- **DB 적재 데이터**
- **실행 화면**

---

## 4. 참고
* API 출처 : 공공데이터포털 서울특별시_버스도착정보조회 서비스 API
* 본 프로젝트는 학습 / 포트폴리오용으로 제작되었습니다.
