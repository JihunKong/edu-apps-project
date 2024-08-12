import streamlit as st

# 사이드바에 탭을 구성
st.sidebar.title("앱 선택")
app_selection = st.sidebar.radio("앱을 선택하세요:", 
                                 ('Life Coach', 'Ethical Dilemma System', 'School Food', 
                                  'Literature', 'Grasps', 'Test Feedback', 
                                  'Student Record Enhancement System', 'Curriculum', 'Evaluation'))

# 각 앱의 메인 코드를 조건문으로 구분하여 포함
if app_selection == 'Life Coach':
    st.title("라이프 코치")
    import apps.lifecoach as lifecoach
    lifecoach.main()

elif app_selection == 'Ethical Dilemma System':
    st.title("윤리적 딜레마 토론")
    import apps.ethical-dilemma-system-main as ethical_dilemma_system
    ethical_dilemma_system.main()

elif app_selection == 'School Food':
    st.title("급식 알리미")
    import apps.schoolfood as schoolfood
    schoolfood.main()

elif app_selection == 'Literature':
    st.title("문학 작품 창작 도우미")
    import apps.literature as literature
    literature.main()

elif app_selection == 'Grasps':
    st.title("Grasps 모형 활용 도우미")
    import apps.grasps as grasps
    grasps.main()

elif app_selection == 'Test Feedback':
    st.title("수행평가 피드백 시스템(예시)")
    import apps.test_feedback as test_feedback
    test_feedback.main()

elif app_selection == 'Student Record Enhancement System':
    st.title("생기부 업그레이드")
    import apps.record-enhancement as student_record_enhancement
    student_record_enhancement.main()

elif app_selection == 'Curriculum':
    st.title("교육과정 계획 도우미")
    import apps.curriculum as curriculum
    curriculum.main()

elif app_selection == 'Evaluation':
    st.title("Evaluation")
    import apps.evaluation as evaluation
    evaluation.main()
