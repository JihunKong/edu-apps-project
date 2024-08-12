import streamlit as st

# 사이드바에 탭을 구성
st.sidebar.title("앱 선택")
app_selection = st.sidebar.radio("앱을 선택하세요:", 
                                 ('Life Coach', 'Ethical Dilemma System', 'School Food', 
                                  'Literature', 'Grasps', 'Test Feedback', 
                                  'Student Record Enhancement System', 'Curriculum', 'Evaluation'))

# 각 앱의 메인 코드를 조건문으로 구분하여 포함
if app_selection == 'Life Coach':
    st.title("Life Coach")
    import apps.lifecoach as lifecoach
    lifecoach.main()

elif app_selection == 'Ethical Dilemma System':
    st.title("Ethical Dilemma System")
    import apps.ethical_dilemma_system as ethical_dilemma_system
    ethical_dilemma_system.main()

elif app_selection == 'School Food':
    st.title("School Food")
    import apps.schoolfood as schoolfood
    schoolfood.main()

elif app_selection == 'Literature':
    st.title("Literature")
    import apps.literature as literature
    literature.main()

elif app_selection == 'Grasps':
    st.title("Grasps")
    import apps.grasps as grasps
    grasps.main()

elif app_selection == 'Test Feedback':
    st.title("Test Feedback")
    import apps.test_feedback as test_feedback
    test_feedback.main()

elif app_selection == 'Student Record Enhancement System':
    st.title("Student Record Enhancement System")
    import apps.student_record_enhancement as student_record_enhancement
    student_record_enhancement.main()

elif app_selection == 'Curriculum':
    st.title("Curriculum")
    import apps.curriculum as curriculum
    curriculum.main()

elif app_selection == 'Evaluation':
    st.title("Evaluation")
    import apps.evaluation as evaluation
    evaluation.main()
