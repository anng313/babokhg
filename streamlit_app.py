
import streamlit as st

st.title("함수 연속성 판별기")
st.markdown("""
함수를 입력하면, 해당 함수가 특정 구간에서 연속인지 판별합니다. (실수 함수, 기본적인 연속성 판별)
예시: x**2, sin(x), 1/x 등
""")

import sympy as sp

func_str = st.text_input("함수식을 입력하세요 (예: x**2, sin(x), 1/x)", value="x**2")
interval = st.text_input("구간을 입력하세요 (예: -1,1)", value="-1,1")

if func_str:
    x = sp.symbols('x')
    try:
        func = sp.sympify(func_str)
        a, b = [float(s.strip()) for s in interval.split(",")]
        # 구간 내 임의의 점에서 연속성 판별
        points = [a, (a+b)/2, b]
        results = []
        for pt in points:
            is_cont = sp.is_continuous(func, x, pt)
            results.append((pt, is_cont))
        st.write(f"함수: $f(x) = {sp.latex(func)}$")
        st.write(f"구간: [{a}, {b}]")
        for pt, res in results:
            st.write(f"x = {pt} 에서 연속성: {'연속' if res else '불연속'}")
        if all(res for _, res in results):
            st.success("이 함수는 해당 구간 내에서 연속입니다.")
        else:
            st.error("이 함수는 해당 구간 내에서 불연속인 점이 있습니다.")
    except Exception as e:
        st.error(f"오류: {e}")

# --- 함수 연속성 판별 페이지 ---
st.header("함수 연속성 판별기")
st.markdown("""
함수를 입력하면, 해당 함수가 특정 구간에서 연속인지 판별합니다. (실수 함수, 기본적인 연속성 판별)
예시: x**2, sin(x), 1/x 등
""")

import sympy as sp

func_str = st.text_input("함수식을 입력하세요 (예: x**2, sin(x), 1/x)", value="x**2")
interval = st.text_input("구간을 입력하세요 (예: -1,1)", value="-1,1")

if func_str:
    x = sp.symbols('x')
    try:
        func = sp.sympify(func_str)
        a, b = [float(s.strip()) for s in interval.split(",")]
        # 구간 내 임의의 점에서 연속성 판별
        points = [a, (a+b)/2, b]
        results = []
        for pt in points:
            is_cont = sp.is_continuous(func, x, pt)
            results.append((pt, is_cont))
        st.write(f"함수: $f(x) = {sp.latex(func)}$")
        st.write(f"구간: [{a}, {b}]")
        for pt, res in results:
            st.write(f"x = {pt} 에서 연속성: {'연속' if res else '불연속'}")
        if all(res for _, res in results):
            st.success("이 함수는 해당 구간 내에서 연속입니다.")
        else:
            st.error("이 함수는 해당 구간 내에서 불연속인 점이 있습니다.")
    except Exception as e:
        st.error(f"오류: {e}")
