import requests
import pandas as pd
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# API KEY 환경변수에서 불러오기
API_KEY = os.getenv("API_KEY")
URL = "http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll"

def fetch_bus_arrivals(route_id: str) -> pd.DataFrame:
    """
    Extract 단계: 서울시 버스 도착정보 API 호출
    """
    params = {
        "serviceKey": API_KEY,
        "busRouteId": route_id,
        "_type": "json"
    }

    # 1. API 요청
    response = requests.get(URL, params=params)

    # 2. 응답 확인 (디버깅 용)
    print("HTTP 상태 코드:", response.status_code)
    print("응답 내용 일부:", response.text[:500])   # 앞부분 500자만 출력

    # 3. JSON 파싱
    data = response.json()
    rows = data["ServiceResult"]["msgBody"]["itemList"]
    df = pd.DataFrame(rows)
    return df