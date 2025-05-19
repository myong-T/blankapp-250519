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

# 두더지 위치 업데이트 (1초마다)
if time.time() - st.session_state.last_update > 1:
    st.session_state.mole_position = random.randint(0, 2)
    st.session_state.last_update = time.time()

st.title("🎯 두더지 잡기 게임")
st.markdown(f"### 점수: {st.session_state.score}")

# 버튼 UI
cols = st.columns(3)
for i in range(3):
    with cols[i]:
        emoji = "🐹" if i == st.session_state.mole_position else "🕳️"
        # 버튼 클릭 처리
        if st.button(f"{emoji}", key=f"btn_{i}"):
            if i == st.session_state.mole_position:
                st.session_state.score += 1
                st.session_state.mole_position = random.randint(0, 2)
                st.session_state.last_update = time.time()

        # 버튼을 크게 보이게 하기 위한 마크다운
        st.markdown(
            f"<div style='text-align: center; font-size: 60px'>{emoji}</div>",
            unsafe_allow_html=True
        )

# 다시 시작 버튼
if st.button("🔄 다시 시작"):
    st.session_state.score = 0
    st.session_state.mole_position = random.randint(0, 2)
