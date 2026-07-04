import streamlit as st
import pandas as pd

# 1. 웹 브라우저 탭 설정
st.set_page_config(page_title="K-POP 아이돌 도감", page_icon="🎤", layout="centered")

# 2. 아이돌 데이터베이스 (자유롭게 추가/수정해보세요!)
# 성별, 소속사, 그룹명, 멤버수, 대표곡 데이터를 담고 있습니다.
idol_data = [
    # 여자 아이돌
    {"성별": "여자아이돌", "소속사": "뉴진스 어소시에이트", "그룹명": "뉴진스 (NewJeans)", "멤버수": 5, "대표곡": "Hype Boy, OMG"},
    {"성별": "여자아이돌", "소속사": "에스엠 (SM)", "그룹명": "에스파 (aespa)", "멤버수": 4, "대표곡": "Next Level, Supernova"},
    {"성별": "여자아이돌", "소속사": "스타쉽", "그룹명": "아이브 (IVE)", "멤버수": 6, "대표곡": "LOVE DIVE, I AM"},
    {"성별": "여자아이돌", "소속사": "하이브 (HYBE)", "그룹명": "르세라핌 (LE SSERAFIM)", "멤버수": 5, "대표곡": "ANTIFRAGILE, Perfect Night"},
    
    # 남자 아이돌
    {"성별": "남자아이돌", "소속사": "하이브 (HYBE)", "그룹명": "방탄소년단 (BTS)", "멤버수": 7, "대표곡": "Dynamite, Butter"},
    {"성별": "남자아이돌", "소속사": "하이브 (HYBE)", "그룹명": "세븐틴 (SEVENTEEN)", "멤버수": 13, "대표곡": "아주 NICE, 손오공"},
    {"성별": "남자아이돌", "소속사": "에스엠 (SM)", "그룹명": "NCT DREAM", "멤버수": 7, "대표곡": "Candy, Smoothie"},
    {"성별": "남자아이돌", "소속사": "JYP", "그룹명": "스트레이 키즈 (Stray Kids)", "멤버수": 8, "대표곡": "특, 락 (LALALALA)"}
]

# 데이터를 판다스(DataFrame) 형태로 변환하여 다루기 쉽게 만듭니다.
df = pd.DataFrame(idol_data)

# 3. 메인 화면 타이틀 구역
st.title("🎤 K-POP 아이돌 도감 앱")
st.write("원하는 성별이나 소속사별로 아이돌 데이터를 검색해 보세요!")
st.markdown("---")

# 4. 사이드바(왼쪽 메뉴) 또는 상단 필터 구성
st.subheader("🔍 검색 및 필터링")

# [기능 1] 남자아이돌 / 여자아이돌 / 전체 선택 라디오 버튼
gender_option = st.radio(
    "1. 성별을 선택하세요",
    options=["전체", "남자아이돌", "여자아이돌"],
    horizontal=True
)

# [기능 2] 소속사별 선택 드롭다운 메뉴 (데이터에 있는 소속사만 자동으로 추출)
companies = ["전체"] + sorted(list(df["소속사"].unique()))
company_option = st.selectbox("2. 소속사를 선택하세요", options=companies)

st.markdown("---")

# 5. 사용자가 선택한 조건에 맞게 데이터 필터링하기
filtered_df = df.copy()

# 성별 필터 적용
if gender_option != "전체":
    filtered_df = filtered_df[filtered_df["성별"] == gender_option]

# 소속사 필터 적용
if company_option != "전체":
    filtered_df = filtered_df[filtered_df["소속사"] == company_option]

# 6. 결과 화면에 깔끔한 표(Table)로 보여주기
st.subheader(f"📊 검색 결과 (총 {len(filtered_df)}팀)")

if not filtered_df.empty:
    # 인덱스(번호)를 1부터 시작하도록 예쁘게 세팅해서 표 출력
    filtered_df.index = range(1, len(filtered_df) + 1)
    st.dataframe(filtered_df, use_container_width=True)
    
    # 소소한 팁: 개별 그룹을 골라 대표곡을 큰 글씨로 보는 기능
    st.markdown("---")
    st.subheader("🎵 그룹별 대표곡 한눈에 보기")
    selected_group = st.selectbox("자세히 보고 싶은 그룹을 골라보세요", options=filtered_df["그룹명"].tolist())
    
    # 선택한 그룹의 대표곡 가져오기
    song = filtered_df[filtered_df["그룹명"] == selected_group]["대표곡"].values[0]
    st.info(f"🎤 **{selected_group}**의 대표곡은 **[{song}]** 입니다!")
    
else:
    st.warning("선택하신 조건에 맞는 아이돌 데이터가 없습니다. 다른 조건을 선택해 보세요!")
