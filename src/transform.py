import pandas as pd

def transform_bus_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform 단계: API 응답 데이터 정리/가공
    - 불필요한 컬럼 제거
    - 컬럼명 표준화
    - 도착 시간 단위(초 → 분) 변환
    """
    # 필요한 컬럼만 추출
    df = df[["busRouteId", "stId", "stNm", "rtNm", "traTime1", "traTime2"]]

    # 컬럼명 정리
    df = df.rename(columns={
        "busRouteId": "route_id",
        "stId": "station_id",
        "stNm": "station_name",
        "rtNm": "route_name",
        "traTime1": "arrival_time_1",
        "traTime2": "arrival_time_2"
    })

    # 도착 시간(초 → 분 변환)
    df["arrival_time_1"] = df["arrival_time_1"].astype(int) // 60
    df["arrival_time_2"] = df["arrival_time_2"].astype(int) // 60

    return df