import pandas as pd

def transform_bus_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform 단계: XML 기반 API 응답 DataFrame을 가공
    - 필요한 컬럼만 유지
    - 컬럼명 표준화
    - 도착시간(초 → 분) 변환
    """
    if df is None or df.empty:
        print("빈 DataFrame이 들어왔습니다")
        return pd.DataFrame(columns=[
            "route_id", "station_id", "station_name",
            "route_name", "arrival_msg_1", "arrival_msg_2",
            "arrival_time_1", "arrival_time_2"
        ])

    print("원본 컬럼:", df.columns.tolist())

    # 서울시 XML 응답에 포함되는 주요 컬럼들
    rename_map = {
        "busRouteId": "route_id",
        "stId": "station_id",
        "stNm": "station_name",
        "rtNm": "route_name",
        "arrmsg1": "arrival_msg_1",   # 도착 안내 메시지 (예: "운행종료", "곧 도착")
        "arrmsg2": "arrival_msg_2",
        "traTime1": "arrival_time_1", # 남은 시간(초 단위)
        "traTime2": "arrival_time_2"
    }

    # 필요한 컬럼만 선택 (실제로 존재하는 것만)
    keep = [c for c in rename_map.keys() if c in df.columns]
    df = df[keep].copy()

    # 컬럼명 변환
    df.rename(columns=rename_map, inplace=True)

    # 남은 시간(초 → 분) 변환
    def safe_minutes(x):
        try:
            return int(x) // 60
        except:
            return 0

    if "arrival_time_1" in df.columns:
        df["arrival_time_1"] = df["arrival_time_1"].apply(safe_minutes)
    else:
        df["arrival_time_1"] = 0

    if "arrival_time_2" in df.columns:
        df["arrival_time_2"] = df["arrival_time_2"].apply(safe_minutes)
    else:
        df["arrival_time_2"] = 0

    return df
