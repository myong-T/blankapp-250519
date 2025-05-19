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
if "clicked" not in st.session_state:
    st.session_state.clicked = None

st.title("🐾 두더지 잡기 게임")
st.markdown("세 개의 버튼 중 **두더지(🐹)** 가 나오는 버튼을 눌러보세요!")

# 점수 표시
st.markdown(f"### 🎯 점수: {st.session_state.score}")

# 두더지 위치 업데이트 (1초마다)
if time.time() - st.session_state.last_update > 1:
    st.session_state.mole_position = random.randint(0, 2)
    st.session_state.last_update = time.time()
    st.session_state.clicked = None  # 리셋 클릭 상태

# 버튼 클릭 처리 함수
def button_click(pos):
    st.session_state.clicked = pos
    if pos == st.session_state.mole_position:
        st.session_state.score += 1

# 버튼 3개 가로로 배치 (HTML + 폼 사용)
with st.form("mole_form", clear_on_submit=True):
    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            emoji = "🐹" if i == st.session_state.mole_position else "🕳️"
            submitted = st.form_submit_button(
                label=emoji,
                key=f"btn_{i}",
                help="두더지를 잡아보세요!",
                args=(i,),
                on_click=button_click,
                kwargs={"pos": i},
            )
# 다시 시작 버튼
if st.button("🔄 다시 시작"):
    st.session_state.score = 0
    st.session_state.mole_position = random.randint(0, 2)
    st.session_state.clicked = None
