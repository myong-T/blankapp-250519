import streamlit as st
import openai

# OpenAI API Key from secrets
openai.api_key = st.secrets["openai"]["api_key"]

# 페이지 설정
st.set_page_config(page_title="🧠 챗봇", layout="centered")
st.title("💬 OpenAI 챗봇")
st.write("멀티턴 대화가 가능한 Streamlit 기반 챗봇입니다.")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "당신은 친절한 AI 비서입니다."}
    ]

# 사용자 입력 받기
user_input = st.text_input("👤 사용자:", key="user_input")

# 사용자 메시지 처리
if user_input:
    # 사용자 메시지를 세션에 추가
    st.session_state.messages.append({"role": "user", "content": user_input})

    # ChatGPT 응답 생성
    with st.spinner("🤖 생각 중..."):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content.strip()

    # 응답을 세션에 추가
    st.session_state.messages.append({"role": "assistant", "content": reply})

# 전체 대화 출력
for msg in st.session_state.messages[1:]:  # system 메시지는 제외
    if msg["role"] == "user":
        st.markdown(f"**🙋‍♂️ 사용자:** {msg['content']}")
    else:
        st.markdown(f"**🤖 챗봇:** {msg['content']}")

# 다시 시작 버튼
if st.button("🔄 대화 초기화"):
    st.session_state.messages = [
        {"role": "system", "content": "당신은 친절한 AI 비서입니다."}
    ]
    st.experimental_rerun()
