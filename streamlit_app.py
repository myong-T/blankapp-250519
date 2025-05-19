import streamlit as st
import random
import time

st.set_page_config(page_title="🐹 두더지 잡기", layout="centered")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "mole_position" not in st.session_state:
    st.session_state.mole_position = random.randint(0, 2)
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

st.title("🎯 두더지 잡기 게임")
st.markdown(f"### 점수: {st.session_state.score}")

# 두더지 위치 업데이트 (1초마다)
if time.time() - st.session_state.last_update > 1:
    st.session_state.mole_position = random.randint(0, 2)
    st.session_state.last_update = time.time()

# 버튼 UI
cols = st.columns(3)
for i in range(3):
    with cols[i]:
        emoji = "🐹" if i == st.session_state.mole_position else "🕳️"

        # 이모지 + 큰 버튼 스타일을 위해 HTML 사용
        button_clicked = st.button(
            label=emoji,
            key=f"mole_button_{i}"
        )

        # 버튼 스타일 커스터마이징: 큰 폰트와 패딩을 적용
        st.markdown(
            f"""
            <style>
            div[data-testid="mole_button_{i}"] button {{
                height: 120px;
                width: 120px;
                font-size: 60px !important;
                border-radius: 16px;
                border: 3px solid #666;
                background-color: #f9f9f9;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # 클릭 처리
        if button_clicked:
            if i == st.session_state.mole_position:
                st.session_state.score += 1
                st.session_state.mole_position = random.randint(0, 2)
                st.session_state.last_update = time.time()

# 다시 시작
if st.button("🔄 다시 시작"):
    st.session_state.score = 0
    st.session_state.mole_position = random.randint(0, 2)
