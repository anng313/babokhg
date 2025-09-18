import streamlit as st

st.title("🎈 My new app")
st.header("Streamlit 요소 데모")

# 텍스트 요소
st.subheader("텍스트 요소")
st.text("이것은 일반 텍스트입니다.")
st.markdown("**마크다운**도 지원합니다!")
st.code("print('Hello, Streamlit!')", language="python")

# 입력 요소
st.subheader("입력 요소")
name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("동의합니다")

# 버튼
st.subheader("버튼")
if st.button("클릭!"):
    st.success(f"{name}님, 버튼을 눌렀습니다!")

# 슬라이더
st.subheader("슬라이더")
value = st.slider("값을 선택하세요", 0, 100, 50)
st.write(f"선택한 값: {value}")

# 선택박스
st.subheader("선택박스")
option = st.selectbox("좋아하는 색상은?", ["빨강", "파랑", "초록", "노랑"])
st.write(f"선택한 색상: {option}")

# 차트
st.subheader("차트 예시")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(df)

# 이미지
st.subheader("이미지")
st.image(
    "https://static.streamlit.io/examples/dog.jpg",
    caption="Streamlit 샘플 이미지",
    use_column_width=True
)
