```python
import streamlit as st
from datetime import date

# 페이지 설정
st.set_page_config(
    page_title="스케줄 관리 앱",
    page_icon="📅"
)

# 제목
st.title("📅 스케줄 관리 웹앱")

# 세션 상태 초기화
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# 일정 입력
st.subheader("➕ 일정 추가")

task = st.text_input("할 일을 입력하세요")
task_date = st.date_input("날짜 선택", value=date.today())

# 추가 버튼
if st.button("추가하기"):

    if task != "":
        st.session_state.tasks.append({
            "task": task,
            "date": task_date,
            "done": False
        })

        st.success("일정 추가 완료!")
    else:
        st.warning("할 일을 입력해주세요.")

# 구분선
st.divider()

# 일정 목록
st.subheader("📋 일정 목록")

if len(st.session_state.tasks) == 0:
    st.info("등록된 일정이 없습니다.")

else:

    for i, item in enumerate(st.session_state.tasks):

        col1, col2, col3 = st.columns([1, 6, 1])

        # 체크박스
        with col1:
            checked = st.checkbox(
                "",
                value=item["done"],
                key=i
            )

            st.session_state.tasks[i]["done"] = checked

        # 일정 표시
        with col2:

            if checked:
                st.markdown(
                    f"~~{item['task']}~~ 📅 {item['date']} ✅"
                )

            else:
                st.write(
                    f"{item['task']} 📅 {item['date']}"
                )

        # 삭제 버튼
        with col3:

            if st.button("❌", key=f"delete_{i}"):

                st.session_state.tasks.pop(i)

                st.rerun()
```
