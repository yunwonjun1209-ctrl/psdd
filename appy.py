import streamlit as st
import google.generativeai as genai

# ... (위쪽 설정 코드는 동일) ...

# ==========================================
# 3. LiteratureAI Analyst v17.5 (엄격성 고정 + 포맷 확정)
# ==========================================
def analyze_literature_v17_pure(api_key, original_text, teacher_criteria, self_analysis):
    genai.configure(api_key=api_key)
    
    # 논리적 사고력이 가장 좋은 Pro 모델 사용
    model = genai.GenerativeModel('gemini-pro')

    prompt = f"""
    당신은 타협을 모르는 문학 분석관 'Literature Investigation Squad (v17.5)'입니다.
    당신의 목표는 [사용자 해석]이 [선생님의 해석]의 **핵심 키워드**를 정확히 포함하고 있는지 '현미경 검증'하는 것입니다.

    [🔥🔥 절대 평가 기준 (변동 금지)]
    1. **대충 넘어가지 마십시오**: 
       - 선생님이 "가족"이라고 했으면, 사용자가 "사람"이라고 했을 때 "구체성 부족"으로 지적하십시오.
       - 선생님이 "귀향 소망"이라는 개념어를 썼으면, 사용자가 그냥 "가고 싶다"라고 했을 때 "개념어 누락"으로 잡으십시오.
       - **'비슷하면 통과'는 없습니다. 정확한 키워드가 없으면 무조건 [보완 지시]를 내리십시오.**

    2. **일관성 유지**:
       - 어떤 상황에서도 동일한 기준을 적용하십시오. 
       - 칭찬보다는 **'빈틈 찾기'**에 집중하십시오.

    3. **출력 형식 엄수**:
       - 영어(Section)를 쓰지 말고, 반드시 아래 한국어 형식을 따르십시오.

    ---
    [데이터 입력]
    1. 원문:
    {original_text}

    2. 선생님의 해석 (정답지):
    {teacher_criteria}

    3. 사용자 해석 (답안지):
    {self_analysis}

    ---
    [출력 리포트 형식]
    
    [Literature Investigation Squad: 정밀 분석 리포트]
    ※ 타겟 기준: (선생님의 강의 주제)
    ---------------------------------------------------
    ### [장면 분할 N] (주제)
    
    1. 핵심 의미 (정합성 확인):
       - (선생님의 해석과 일치하는 부분 확인)
       - (잘한 점은 짧게, 팩트 위주로 서술)

    2. 시각화 포인트 보완 (오독 및 누락 점검):
       - 🚨 **오독 발견**: (선생님 기준과 틀린 해석이 있다면 지적)
       - 🧩 **개념 보완**: (사용자가 놓친 '선생님의 핵심 키워드/개념어' 지적)
       - ✍️ **수정 가이드**: (어떻게 고쳐야 하는지 구체적 지시)
       * (완벽하다면 "특이사항 없음. 선생님의 기준과 완벽히 일치함." 출력)

    (모든 장면에 대해 위 항목 반복)
    ---------------------------------------------------
    [최종 결론]: (정확도 점수 및 총평)
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ 시스템 오류 발생: {str(e)}"

# ... (아래쪽 UI 코드는 동일) ...
# ==========================================
# 2. Streamlit 화면 구성 (UI)
# ==========================================
st.set_page_config(page_title="LiteratureAI Analyst v17.4", layout="wide")
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
    st.title("PSJ EDU Service v17.4") # 제목을 원하시는대로 수정하세요
    st.header("🧐 With PSJ EDU v17.4")
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
