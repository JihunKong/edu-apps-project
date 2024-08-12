import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from openai import OpenAI

# OpenAI 클라이언트 설정
client = OpenAI(api_key=st.secrets["api_keys"]["openai"])

# 2022 개정 국어과 교육과정 내용 영역
content_areas = {
    "중학교": ["듣기・말하기", "읽기", "쓰기", "문법", "문학"],
    "고등학교": ["듣기・말하기", "읽기", "쓰기", "문법", "문학", "매체"]
}

# 학습 방법 및 형태 예시
learning_methods = ["강의", "토론", "프로젝트 학습", "협동 학습", "개별 학습", "탐구 학습"]
learning_forms = ["개별", "모둠", "전체"]

# 디지털 도구 예시
digital_tools = {
    "기기": ["태블릿", "노트북", "스마트폰", "전자칠판"],
    "플랫폼": ["Google Classroom", "Microsoft Teams", "Padlet", "Kahoot"],
    "활용 방법": ["온라인 협업", "디지털 콘텐츠 제작", "온라인 토론", "디지털 포트폴리오"]
}

# 평가 방법 예시
assessment_methods = ["서술형 평가", "논술형 평가", "구술 평가", "관찰법", "포트폴리오 평가", "수행평가"]

def generate_curriculum_plan(school_level, grade, weekly_hours, selected_options):
    prompt = f"""
    {school_level} {grade} 국어과 연간 교육과정 계획을 작성해주세요. 
    주당 수업 시수는 {weekly_hours}시간이며, 1학기는 3월 첫 주부터 6월 마지막 주까지, 2학기는 8월 셋째 주부터 11월 마지막 주까지입니다.
    2022 개정 국어과 교육과정을 참조하여 각 영역({', '.join(content_areas[school_level])})을 균형있게 다루도록 해주세요.
    
    다음 선택된 옵션을 반영하여 계획을 수립해주세요:
    - 내용 영역: {', '.join(selected_options['content_areas'])}
    - 학습 방법: {', '.join(selected_options['learning_methods'])}
    - 학습 형태: {', '.join(selected_options['learning_forms'])}
    - 디지털 도구 (기기): {', '.join(selected_options['digital_tools_devices'])}
    - 디지털 도구 (플랫폼): {', '.join(selected_options['digital_tools_platforms'])}
    - 디지털 도구 (활용 방법): {', '.join(selected_options['digital_tools_usage'])}
    - 평가 방법: {', '.join(selected_options['assessment_methods'])}
    
    각 단원별로 다음 내용을 포함해주세요:
    1. 단원명
    2. 주요 학습 내용
    3. 권장 학습 방법 및 형태
    4. 활용 가능한 디지털 도구
    5. 추천 평가 방법
    """
    
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "당신은 2022 개정 교육과정에 정통한 국어과 교육과정 전문가입니다."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        st.error(f"OpenAI API 오류: {str(e)}")
        return "교육과정 계획 생성 중 오류가 발생했습니다."

def create_timeline(school_level, grade, weekly_hours):
    # 1학기: 3월 첫 주 ~ 6월 마지막 주
    first_semester_start = datetime(2024, 3, 1)
    first_semester_end = datetime(2024, 6, 30)
    
    # 2학기: 8월 셋째 주 ~ 11월 마지막 주
    second_semester_start = datetime(2024, 8, 15)
    second_semester_end = datetime(2024, 11, 30)
    
    # 주차 생성
    weeks = []
    current_date = first_semester_start
    week_count = 1
    
    while current_date <= second_semester_end:
        if first_semester_start <= current_date <= first_semester_end or second_semester_start <= current_date <= second_semester_end:
            weeks.append({
                "Week": f"Week {week_count}",
                "Start": current_date,
                "End": current_date + timedelta(days=6),
                "Hours": weekly_hours
            })
            week_count += 1
        current_date += timedelta(days=7)
    
    df = pd.DataFrame(weeks)
    return df

st.title("국어과 교육과정 계획 도우미")

# 사이드바에 선택 옵션 추가
st.sidebar.header("국어과 교육과정 참고 사항")

school_level = st.sidebar.selectbox("학교 급", ["중학교", "고등학교"])
grade = st.sidebar.selectbox("학년", ["1학년", "2학년", "3학년"])
weekly_hours = st.sidebar.number_input("주당 수업 시수", min_value=1, max_value=6, value=4)

selected_options = {
    "content_areas": st.sidebar.multiselect("내용 영역", content_areas[school_level], default=content_areas[school_level]),
    "learning_methods": st.sidebar.multiselect("학습 방법", learning_methods, default=learning_methods[:2]),
    "learning_forms": st.sidebar.multiselect("학습 형태", learning_forms, default=learning_forms[:2]),
    "digital_tools_devices": st.sidebar.multiselect("디지털 도구 (기기)", digital_tools["기기"], default=digital_tools["기기"][:2]),
    "digital_tools_platforms": st.sidebar.multiselect("디지털 도구 (플랫폼)", digital_tools["플랫폼"], default=digital_tools["플랫폼"][:2]),
    "digital_tools_usage": st.sidebar.multiselect("디지털 도구 (활용 방법)", digital_tools["활용 방법"], default=digital_tools["활용 방법"][:2]),
    "assessment_methods": st.sidebar.multiselect("평가 방법", assessment_methods, default=assessment_methods[:2]),
}

st.sidebar.markdown("""
### 수업 시간
- 중학교: 45분
- 고등학교: 50분
""")

st.sidebar.markdown("""
주의: 생성된 교육과정 계획은 참고용입니다. 실제 적용 시에는 학교와 학급 상황에 맞게 조정해 주세요.
""")

if st.button("교육과정 계획 생성"):
    curriculum_plan = generate_curriculum_plan(school_level, grade, weekly_hours, selected_options)
    st.markdown(curriculum_plan)
    
    # 타임라인 생성 및 표시
    timeline_df = create_timeline(school_level, grade, weekly_hours)
    fig = px.timeline(timeline_df, x_start="Start", x_end="End", y="Week", color="Hours")
    fig.update_layout(title=f"{school_level} {grade} 국어과 연간 수업 시수 계획")
    st.plotly_chart(fig)
