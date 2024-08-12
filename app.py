import streamlit as st

# 사이드바에 탭을 구성
st.sidebar.title("앱 선택")
app_selection = st.sidebar.radio("앱을 선택하세요:", 
                                 ('문학 작품 창작 도우미', 'Grasps 모형 활용 도우미', '틀린 문제 해설 도우미(수능형)', 
                                  '생기부 업그레이드', '교육과정 계획 도우미', '수행평가 피드백 시스템(예시)'))

# 각 앱의 메인 코드를 조건문으로 구분하여 포함
if app_selection == '문학 작품 창작 도우미':
   st.title("문학 작품 창작 도우미")
   import apps.literature as literature
   literature.main()

elif app_selection == 'Grasps 모형 활용 도우미':
     st.title("Grasps 모형 활용 도우미")
     import apps.grasps as grasps
     grasps.main()

elif app_selection == '틀린 문제 해설 도우미(수능형)':
     st.title("틀린 문제 해설 도우미(수능형)")
     import apps.test_feedback as test_feedback
     test_feedback.main()

elif app_selection == '생기부 업그레이드':
     st.title("생기부 업그레이드")
     import apps.record_enhancement as student_record_enhancement
     student_record_enhancement.main()

elif app_selection == '교육과정 계획 도우미':
     st.title("교육과정 계획 도우미")
     import apps.curriculum as curriculum
     curriculum.main()

elif app_selection == '수행평가 피드백 시스템(예시)':
     st.title("수행평가 피드백 시스템(예시)")
     import apps.evaluation as evaluation
     evaluation.main()
