
import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("함수 연속성 판별 및 그래프 그리기")
st.markdown("""
함수를 입력하면, 해당 함수가 특정 구간에서 연속인지 판별하고 그래프를 그려줍니다. (실수 함수, 기본적인 연속성 판별)
예시: x**2, sin(x), 1/x 등
""")

func_str = st.text_input("함수식을 입력하세요 (예: x**2, sin(x), 1/x)", value="x**2")
interval = st.text_input("구간을 입력하세요 (예: -1,1)", value="-1,1")

if func_str:
    x = sp.symbols('x')
    try:
        func = sp.sympify(func_str)
        a, b = [float(s.strip()) for s in interval.split(",")]
        # 연속성 판별
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

        # 함수 그래프 그리기
        st.subheader("함수 그래프")
        xs = np.linspace(a, b, 400)
        f_lambdified = sp.lambdify(x, func, modules=["numpy"])
        try:
            ys = f_lambdified(xs)
            fig, ax = plt.subplots()
            ax.plot(xs, ys, label=f"f(x) = {func_str}")
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            ax.set_title("함수 그래프")
            ax.legend()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"그래프를 그릴 수 없습니다: {e}")
    except Exception as e:
        st.error(f"오류: {e}")
