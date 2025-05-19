import streamlit as st
import random
import time
from streamlit.components.v1 import html

st.set_page_config(page_title="두더지 잡기", layout="centered")

# 초기 상태 설정
if "score" not in st.session_state:
    st.session_state.score = 0
if "mole_position" not in st.session_state:
    st.session_state.mole_position = random.randint(0, 2)
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

st.title("🐹 두더지 잡기 게임")
st.markdown(f"### 점수: {st.session_state.score}")

# 두더지 위치 업데이트
if time.time() - st.session_state.last_update > 1:
    st.session_state.mole_position = random.randint(0, 2)
    st.session_state.last_update = time.time()

# 버튼 UI - 이모지를 HTML로 크게 표시
cols = st.columns(3)

for i in range(3):
    with cols[i]:
        if i == st.session_state.mole_position:
            clicked = st.button(" ", key=f"mole_{i}")
            html("""
            <div style="font-size:80px; text-align:center;">🐹</div>
            """, height=100)
            if clicked:
                st.session_state.score += 1
        else:
            st.button("🕳️", key=f"hole_{i}")

# 다시 시작 버튼
if st.button("다시 시작"):
    st.session_state.score = 0
    st.session_state.mole_position = random.randint(0, 2)
