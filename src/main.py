from src.db import get_engine
from src.fetch_bus import fetch_bus_arrivals
from src.transform import transform_bus_data

def main():
    # DB 엔진 생성
    engine = get_engine()

    # 1. Extract
    df_raw = fetch_bus_arrivals("100100057")  # 노선 ID 예시

    # 2. Transform
    df_transformed = transform_bus_data(df_raw)

    # 3. Load
    df_transformed.to_sql(
        "bus_arrivals",
        engine,
        if_exists="append",
        index=False
    )

    print("✅ 데이터 파이프라인 실행 완료 (API → Transform → MySQL 저장)")

if __name__ == "__main__":
    main()