import streamlit as st
import random
import time

st.set_page_config(page_title="두더지 잡기", layout="centered")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "mole_position" not in st.session_state:
    st.session_state.mole_position = random.randint(0, 2)
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

st.title("🎯 두더지 잡기 게임")
st.markdown("크고 귀여운 🐹 두더지를 잡아보세요!")

# 점수 표시
st.markdown(f"### 점수: {st.session_state.score}")

# 두더지 위치 업데이트 (1초마다)
if time.time() - st.session_state.last_update > 1:
    st.session_state.mole_position = random.randint(0, 2)
    st.session_state.last_update = time.time()

# 버튼 3개 생성 (이모지 포함)
cols = st.columns(3)
for i in range(3):
    with cols[i]:
        emoji = "🐹" if i == st.session_state.mole_position else "🕳️"
        # 이모지를 버튼 안에 크게 보여주기
        button_label = f"<div style='font-size: 60px; line-height: 1'>{emoji}</div>"
        if st.button(label="", key=f"btn_{i}"):
            if i == st.session_state.mole_position:
                st.session_state.score += 1
        st.markdown(button_label, unsafe_allow_html=True)

# 다시 시작
if st.button("🔁 다시 시작"):
    st.session_state.score = 0
    st.session_state.mole_position = random.randint(0, 2)
