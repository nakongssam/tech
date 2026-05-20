```python
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="스케줄 관리 앱",
    page_icon="📅",
    layout="centered"
)

st.title("📅 나의 스케줄 관리")

# 세션 상태 초기화
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# 일정 추가 영역
st.subheader("➕ 일정 추가")

task = st.text_input("할 일을 입력하세요")
task_date = st.date_input("날짜 선택", value=date.today())

if st.button("추가하기"):
    if task.strip() != "":
        st.session_state.tasks.append({
            "task": task,
            "date": task_date,
            "done": False
        })
        st.success("일정이 추가되었습니다!")
    else:
        st.warning("할 일을 입력해주세요.")

st.divider()

# 일정 목록 표시
st.subheader("📋 일정 목록")

if len(st.session_state.tasks) == 0:
    st.info("등록된 일정이 없습니다.")
else:
    for idx, item in enumerate(st.session_state.tasks):

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            done = st.checkbox(
                "",
                value=item["done"],
                key=f"check_{idx}"
            )
            st.session_state.tasks[idx]["done"] = done

        with col2:
            if done:
                st.markdown(
                    f"~~{item['task']}~~ ({item['date']}) ✅"
                )
            else:
                st.write(f"{item['task']} ({item['date']})")
```
