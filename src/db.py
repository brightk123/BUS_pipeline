from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

def get_engine():
    """
    MySQL 연결 엔진 생성
    - Load 단게에서 사용
    """

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4"
    engine = create_engine(url, echo=False)
    return engine