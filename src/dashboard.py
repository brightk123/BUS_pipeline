# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# DB 연결
engine = create_engine("mysql+pymysql://root:비밀번호@localhost:3306/bus_db")

# 데이터 로드
df = pd.read_sql("SELECT * FROM bus_arrivals", con=engine)

st.title("Bus Arrival in SEOUL Dashboard")

# 노선 선택
routes = df["route_name"].dropna().unique()
selected_route = st.selectbox("노선을 선택하세요", routes)

# 필터링
df_filtered = df[df["route_name"] == selected_route]

# 정류소별 평균 대기시간
avg_wait = df_filtered.groupby("station_name")["arrival_time_1"].mean().reset_index()

# 시각화
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(avg_wait["station_name"], avg_wait["arrival_time_1"])
plt.xticks(rotation=45)
ax.set_title(f"{selected_route}번 노선 정류소별 평균 첫 버스 대기시간")
ax.set_ylabel("평균 대기 시간(분)")

st.pyplot(fig)

# 데이터 테이블도 함께 표시
st.dataframe(avg_wait)
