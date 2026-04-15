import streamlit as st
import time
import random

# 웹 페이지 설정
st.set_page_config(page_title="멘헤라팟 멘탈 케어", page_icon="🎓")

# 메인 타이틀
st.title("시험기간 멘탈 케어 시스템")
st.subheader("오하람의 코딩 연습 겸 4.5를 위한 대시보드")

# 입력창 (사이드바에 배치)
with st.sidebar:
    st.header("사용자 정보")
    name = st.text_input("이름을 알려주세요", placeholder="이름 입력")
    subject = st.text_input("과목명", placeholder="전공과목 등")
    start_button = st.button("분석 시작")

if start_button:
    if name and subject:
        # 1. 분석 중 메시지
        with st.spinner(f"{name}님의 {subject} 지식 동기화 중..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
        
        st.success("✅ 지식 주입 완료!")
        st.balloons() # 웹이라서 가능한 화려한 축하 효과! 🎈

        # 2. 결과 출력 (카드 형태)
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="예상 학점", value="A+", delta="수석 가능성 높음")
        
        with col2:
            drinks = ["몬스터 울트라", "핫식스 더킹", "아아(샷추가)", "얼음물", "가온누리 말차라떼", "그냥 물이나 먹어라", "정신병약"]
            st.info(f"🥤 처방 음료: {random.choice(drinks)}")

        # 3. 응원 메시지
        st.write("---")
        cheers = [
            "중간고사 끝나면 관악산에 가야 해요",
            "교수님도 감동할 당신의 열정",
            "지금 이 순간도 당신은 성장하고 있어요.",
            "토닥토닥.....은 무슨 나도 힘들다"
        ]
        st.markdown(f"### 💌 오늘의 메시지\n> **{random.choice(cheers)}**")
        
    else:
        st.warning("이름과 과목을 입력해 주세요!")

# 하단 정보
st.caption(" 당신의 시험을 응원합니다.")