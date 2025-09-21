#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# In[3]:


# .env 파일 로드
load_dotenv()


# In[5]:


# MySQL 연결 객체 생성 함수
def get_engine():
    """
    MySQL 연결 엔진 생성
    - Load 단계에서 사용
    """
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4"
    engine = create_engine(url, echo=False)
    return engine

