import streamlit as st
from google import genai

# 페이지 설정
st.set_page_config(
    page_title="모닝루틴 코치",
    page_icon="🌅"
)

st.title("🌅 AI 모닝루틴 코치")
st.caption("좋은 아침 습관과 하루 계획을 도와드립니다.")

# API 키 확인
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# Gemini 클라이언트
client = genai.Client(api_key=api_key)

# 시스템 프롬프트
SYSTEM_PROMPT = """
당신은 전문 모닝루틴 코치입니다.

역할:
- 아침 습관 만들기
- 기상 시간 관리
- 생산성 향상
- 운동 및 독서 습관 형성
- 하루 계획 수립
- 동기부여 제공

답변 원칙:
- 친절하고 긍정적일 것
- 구체적인 실행 방법 제시
- 너무 길지 않게 설명
"""

# 채팅 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 🌅 모닝루틴 코치입니다. 어떤 아침 습관을 만들고 싶으신가요?"
        }
    ]

# 기존 메시지 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
prompt = st.chat_input("메시지를 입력하세요")

if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # 대화 이력 구성
        history = "\n".join(
            [f"{m['role']}: {m['content']}" for m in st.session_state.messages]
        )

        full_prompt = f"""
{SYSTEM_PROMPT}

대화기록:
{history}

assistant:
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=full_prompt
        )

        answer = response.text

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:
        error_msg = f"오류가 발생했습니다: {str(e)}"

        st.session_state.messages.append(
            {"role": "assistant", "content": error_msg}
        )

        with st.chat_message("assistant"):
            st.error(error_msg)

# 대화 초기화 버튼
if st.button("대화 초기화"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 🌅 모닝루틴 코치입니다. 어떤 아침 습관을 만들고 싶으신가요?"
        }
    ]
    st.rerun()
