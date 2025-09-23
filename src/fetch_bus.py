import requests
import pandas as pd
import xmltodict   # XML → dict 변환용 라이브러리
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("API_KEY")
URL = "http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll"


def fetch_bus_arrivals(route_id: str) -> pd.DataFrame:
    """
    Extract 단계: 서울시 버스 도착정보 API 호출
    XML 응답을 받아 dict로 변환 후 DataFrame으로 리턴
    """
    params = {
        "ServiceKey": API_KEY,
        "busRouteId": route_id
        # "_type": "json"   # 필요 없을 수도 있음 (XML이 기본 응답)
    }

    response = requests.get(URL, params=params)
    print("상태코드:", response.status_code)

    if response.status_code != 200:
        print("API 호출 실패")
        return pd.DataFrame()

    # XML → dict 변환
    try:
        data = xmltodict.parse(response.text)
    except Exception as e:
        print("XML 파싱 실패:", e)
        return pd.DataFrame()

    # itemList 추출
    try:
        rows = data["ServiceResult"]["msgBody"]["itemList"]
    except (KeyError, TypeError):
        print("itemList 없음. 실제 응답:", data)
        return pd.DataFrame()

    # itemList가 dict 하나로만 올 수도 있고(list가 아닐 수도 있음)
    if isinstance(rows, dict):
        rows = [rows]

    df = pd.DataFrame(rows)
    print("DataFrame 컬럼:", df.columns.tolist())
    return df