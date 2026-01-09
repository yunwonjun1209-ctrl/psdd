import streamlit as st
import google.generativeai as genai

# ==========================================
# ==========================================
# 🧠 LiteratureAI Brain v17.4 (용어 순화 + 개념 엄격 평가)
# ==========================================
def analyze_literature_v17_learning(api_key, original_text, teacher_criteria, self_analysis):
    genai.configure(api_key=api_key)
    
    # 논리적 엄밀함을 위해 Pro 모델 유지
    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt = f"""
    당신은 깐깐하지만 공정한 문학 분석관 'Literature Investigation Squad (v17.4)'입니다.
    [사용자 해석]이 [선생님의 해석]과 논리적으로 일치하는지 정밀 검증하십시오.

    [🔥🔥 분석 가이드라인]
    1. **용어 통일**: 
       - 'T'라고 부르지 말고 반드시 **'선생님의 해석'** 또는 **'선생님의 강의'**라고 지칭하십시오.
       - 'S'라고 부르지 말고 반드시 **'사용자 해석'**이라고 지칭하십시오.
       - 강의 회차(예: 14강, 8강)는 언급하지 마십시오. 그냥 **'선생님의 강의에선'**이라고만 하십시오.
    
    2. **깐깐한 개념 평가**: 
       - 억지로 트집 잡지는 마십시오. 논리가 맞으면 인정하십시오.
       - 단, 선생님이 강조한 **'전문 용어'**나 **'핵심 개념'**(예: 공감각, 역설, 객관적 상관물 등)이 사용자 해석에 빠져 있다면, 단순 말풀이로 넘어가지 말고 **'개념 누락'**으로 엄격하게 지적하십시오.

    3. **연출/시각화 인정**: 
       - 시각화 지시 자체는 허용합니다. 그 내용이 선생님의 해석과 분위기상 맞는지(정합성)만 따지십시오.

    ---
    [데이터 입력]
    1. 원문:
    {original_text}

    2. 선생님의 해석 (절대 기준):
    {teacher_criteria}

    3. 사용자 해석 (평가 대상):
    {self_analysis}

    ---
    [출력 리포트 형식]
    
    [Literature Investigation Squad: 정밀 분석 리포트]
    ※ 타겟 기준: (선생님의 강의 주제)
    ---------------------------------------------------
    ### [Section N] (주제)
    1. 🎯 정합성 일치 (Confirmed):
       - (선생님의 해석과 정확히 일치하는 부분)

    2. 🚨 오독 검출 (Critical Mismatch):
       - [사용자 해석]: (문제가 되는 부분)
       - [선생님의 해석]: (실제 팩트)
       - [교정 명령]: (구체적 수정 방향)
       * (없으면 "특이동향 없음" 출력)

    3. 🧩 데이터 누락 (Missing Intel):
       - [누락된 개념]: (사용자가 놓친 핵심 개념)
       - [보완 지시]: (이 개념을 어떻게 추가해야 하는지 설명)
       * (없으면 "특이동향 없음" 출력)
    ---------------------------------------------------
    [Final Conclusion]: (정확도 % 및 총평 - 깐깐하게 평가)
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ 분석 시스템 오류: {str(e)}"

# ==========================================
# 2. Streamlit 화면 구성 (UI)
# ==========================================
st.set_page_config(page_title="LiteratureAI Analyst v17.0", layout="wide")
def check_password():
    """비밀번호가 맞는지 확인하는 함수"""
    # 세션 상태 초기화
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    # 비밀번호가 아직 틀렸거나 입력 전이면 입력창 보여주기
    if not st.session_state.password_correct:
        st.title("🔒 비공개 홈페이지")
        st.write("관계자 외 출입금지")
        
        pwd = st.text_input("비밀번호를 입력하세요", type="password")
        
        if st.button("접속하기"):
            # [중요] Streamlit 사이트의 Secrets에 설정한 "PASSWORD"와 비교
            # 로컬(내컴퓨터)에서 테스트할 때는 에러가 날 수 있으니
            # secrets.toml 파일을 만들거나, 아래 코드를 잠시 if pwd == "1234": 로 쓰세요.
            try:
                if pwd == st.secrets["PASSWORD"]:  
                    st.session_state.password_correct = True
                    st.rerun()  # 맞으면 화면 새로고침
                else:
                    st.error("경고! 비밀번호가 틀렸습니다. 귀하의 접근 정보와 기록이 남습니다.")
            except FileNotFoundError:
                st.error("Secrets 설정이 안 되어 있습니다. Streamlit 사이트 설정을 확인하세요.")
        
        # 비밀번호가 틀리면 아래 코드는 실행하지 않고 여기서 멈춤
        st.stop()

# 비밀번호 검사 실행 (통과 못하면 여기서 멈춤)
check_password()

# 비밀번호 검사 실행
check_password()
# [수정됨] 화면을 왼쪽(1) : 가운데(4) : 오른쪽(1) 비율로 3등분
col_left, col_center, col_right = st.columns([1, 4, 1])

# 1. 왼쪽 기둥 ( 로고)
with col_left:
    st.image("https://i.namu.wiki/i/9HvRzzpNGP1k-k0PU4Hp-xQWUV2eNQEJu6a18aOEy3gizARGS8mbGf7TI0jYGEz6WP8HDAJxo4HdPZxZCNW5jv8Hkzibsf74tV714FEx56NbS55YfoYjjWG1iXpz6pozsNdmhIIR8Xb-Lvtvoz4uDA.webp", width=900)
# 2. 가운데 기둥 (제목)
with col_center:
    st.title("PSJ EDU Service v17.0") # 제목을 원하시는대로 수정하세요
    st.header("🧐 With PSJ EDU v17.0")
    st.caption("순수 해석 정밀 분석 모드 (연출 제외, 오독/누락 체크)")

# 3. 오른쪽 기둥 (새로 추가할 로고)
with col_right:
    # 여기에 원하시는 두 번째 사진 주소를 넣으세요!
    # 지금은 예시로 같은 걸 찾아서 넣거나, 원하시는 이미지 주소를 넣으세요.
    st.image("https://i.namu.wiki/i/9HvRzzpNGP1k-k0PU4Hp-xQWUV2eNQEJu6a18aOEy3gizARGS8mbGf7TI0jYGEz6WP8HDAJxo4HdPZxZCNW5jv8Hkzibsf74tV714FEx56NbS55YfoYjjWG1iXpz6pozsNdmhIIR8Xb-Lvtvoz4uDA.webp", width=900)
# 사이드바: API 키 입력
with st.sidebar:
    st.header("설정")
    api_key = st.text_input("Gemini API Key", type="password")
    st.markdown("[API 키 발급받기](https://aistudio.google.com/app/apikey)")

# 메인 입력창
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. 기준 및 해석 입력")
    teacher_criteria = st.text_area("선생님 기준 (Criteria <T>)", height=200, 
        placeholder="박석준 선생님 강의 내용, 팩트체크 포인트 등...")
    self_analysis = st.text_area("사용자 해석 (Analysis <S>)", height=200, 
        placeholder="내가 분석한 장면 분할 내용 (시각화 포인트 제외하고 텍스트 위주로)...")

with col2:
    st.subheader("2. 원문 입력")
    original_text = st.text_area("원문 텍스트 (Text <O>)", height=450, 
        placeholder="분석할 문학 작품의 원문...")

# 실행 버튼
if st.button("NIS에게 분석 요청하기 🚀", use_container_width=True):
    if not api_key:
        st.error("⚠️ 왼쪽 사이드바에 API 키를 입력해주세요.")
    elif not teacher_criteria or not self_analysis or not original_text:
        st.warning("⚠️ 선생님 기준, 사용자 해석, 원문을 모두 입력해야 합니다.")
    else:
        with st.spinner("LiteratureAI v17.0 엔진 가동 중... (순수 해석 정밀 분석)"):
            result = analyze_literature_v17_pure(api_key, original_text, teacher_criteria, self_analysis)
            st.success("NIS 분석 완료!")
            st.markdown("### 📊 NIS 리포트")
            st.markdown(result)
