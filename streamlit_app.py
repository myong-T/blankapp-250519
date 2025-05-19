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
if "clicked_index" not in st.session_state:
    st.session_state.clicked_index = None

# 두더지 위치 업데이트 (1초마다)
if time.time() - st.session_state.last_update > 1:
    st.session_state.mole_position = random.randint(0, 2)
    st.session_state.last_update = time.time()

st.title("🎯 두더지 잡기 게임")
st.markdown(f"### 점수: {st.session_state.score}")

# 클릭 감지
clicked = st.experimental_get_query_params().get("hit", [None])[0]
if clicked is not None:
    clicked = int(clicked)
    if clicked == st.session_state.mole_position:
        st.session_state.score += 1
    st.experimental_set_query_params()  # 클릭 후 URL 초기화

# 버튼 UI (HTML)
cols = st.columns(3)
for i in range(3):
    with cols[i]:
        emoji = "🐹" if i == st.session_state.mole_position else "🕳️"
        st.markdown(f"""
            <form action="" method="get">
                <input type="hidden" name="hit" value="{i}" />
                <button type="submit" style="
                    font-size: 60px;
                    width: 120px;
                    height: 120px;
                    border: 3px solid #444;
                    border-radius: 16px;
                    background-color: #f0f0f0;
                    cursor: pointer;
                ">{emoji}</button>
            </form>
        """, unsafe_allow_html=True)

# 다시 시작 버튼
if st.button("🔄 다시 시작"):
    st.session_state.score = 0
    st.session_state.mole_position = random.randint(0, 2)
    st.experimental_set_query_params()
