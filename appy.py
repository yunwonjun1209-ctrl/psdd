import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. LiteratureAI Analyst v17.0 함수 (순수 해석 분석)
# ==========================================
def analyze_literature_v17_pure(api_key, original_text, teacher_criteria, self_analysis):
    """
    LiteratureAI Analyst v17.0
    연출/시각화 제외. 오직 텍스트 해석의 정합성과 누락 요소만 정밀 평가.
    """
    # API 설정
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
    당신은 'LiteratureAI Analyst v17.0'입니다.
    당신의 임무는 [사용자 해석(S)]이 [선생님 기준(T)]과 논리적으로 일치하는지 텍스트 차원에서 정밀 평가하는 것입니다.

    [절대 규칙]
    1. **시각화/연출/이미지/촬영 지시 절대 금지**: 오직 텍스트의 '의미 해석'과 '논리'만 다루십시오.
    2. 선생님 기준(T)에 근거하여 S의 '오독(Misinterpretation)'과 '개념 누락(Omission)'을 찾아내십시오.
    3. 수정 제안은 S의 텍스트를 어떻게 고쳐써야 하는지 구체적인 '문장'이나 '키워드'로 제시하십시오.

    ---
    [입력 데이터]
    1. 원문 (Text <O>):
    {original_text}

    2. 선생님 기준 (Criteria <T>) [정답/채점 기준]:
    {teacher_criteria}

    3. 사용자 해석 (Analysis <S>) [평가 대상]:
    {self_analysis}

    ---
    [출력 형식]
    아래 형식을 그대로 사용하여 출력하십시오.

    [LiteratureAI Analyst: 해석 정밀 평가 리포트 (순수 분석)]
    ※ 기준(T): (선생님 강의 주제)
    ----------------------------------------------------------------------

    ### [장면 분할 N] (장면의 핵심 주제)
    1. ✅ 정합성 확인 (Match):
       - (S가 T의 기준대로 정확하게 해석한 내용)
    
    2. ❌ 오독 판정 (Critical Error):
       - [사용자(S)]: (틀린 해석 내용)
       - [선생님(T)]: (정확한 팩트/개념)
       - [수정 가이드]: (S의 '핵심 의미'나 설명 텍스트를 어떻게 수정해야 하는지 서술)
       * (오류가 없다면 "발견되지 않음." 출력)

    3. ⚠️ 결핍 요소 (Missing Concept):
       - [누락된 핵심어]: (S가 빠뜨린 T의 중요 키워드)
       - [보완 가이드]: (이 키워드를 넣어 S의 해석을 어떻게 보강해야 하는지 설명)
       * (누락이 없다면 "특이사항 없음." 출력)

    (모든 장면에 대해 위 항목 반복)

    ----------------------------------------------------------------------
    [Final Verdict]: (전체적인 해석 정확도 총평 및 S 텍스트 수정 요약)
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ 시스템 오류 발생: {str(e)}"

# ==========================================
# 2. Streamlit 화면 구성 (UI)
# ==========================================
st.set_page_config(page_title="LiteratureAI Analyst v17.0", layout="wide")
# ==========================================
# [보안] 비밀번호 잠금 장치 (여기서 멈춤)
# ==========================================
def check_password():
    """비밀번호 확인 함수"""
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if not st.session_state.password_correct:
        st.title("🔒 비공개 홈페이지 입니다.")
        st.write("관계자 외 출입금지")
        
       if pwd == st.secrets["PASSWORD"]:  
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("비밀번호가 틀렸습니다. 귀하의 접근 기록과 주소가 남습니다.")
        
        # 비밀번호 틀리면 여기서 코드 실행을 멈춤 (아래 내용 안 보임)
        st.stop()

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
