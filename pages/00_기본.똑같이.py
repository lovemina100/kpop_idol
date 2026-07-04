import streamlit as st

# 페이지 설정
st.set_page_config(page_title="갓생 공부방", page_icon="📝", layout="centered")

# 홈 화면 꾸미기
st.title("📝 갓생 공부방에 오신 것을 환영합니다!")
st.subheader("오늘도 열공해서 목표를 달성해 볼까요? 🔥")

st.markdown("---")

st.write("### 🧭 메뉴 안내")
st.write("왼쪽 사이드바 메뉴를 클릭해서 원하는 공부 도구를 사용해 보세요!")
st.info("""
- **⏳ 공부 시간 측정:** 뽀모도로 타이머로 집중 시간을 기록해요.
- **🤖 AI 공부 도우미:** 공부하다 막히는 질문을 적으면 AI가 답변해 줘요.
- **📅 공부 시간표:** 나의 요일별 공부 계획과 시간표를 한눈에 확인해요.
""")

st.markdown("---")
st.caption("💡 '천재는 노력하는 자를 이길 수 없고, 노력하는 자는 즐기는 자를 이길 수 없다.' - 오늘도 파이팅!")
