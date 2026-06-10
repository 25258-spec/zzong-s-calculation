import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="고급 계산기", page_icon="🧮")

st.title("🧮 고급 계산기 웹앱")

st.write("사칙연산, 모듈러, 지수, 로그, 삼각함수 계산 및 그래프 기능을 제공합니다.")

# 연산 선택
operation = st.selectbox(
    "연산을 선택하세요",
    (
        "덧셈",
        "뺄셈",
        "곱셈",
        "나눗셈",
        "모듈러 연산",
        "지수 연산",
        "로그 연산",
        "sin",
        "cos",
        "tan",
        "삼각함수 그래프"
    )
)

# 삼각함수 계산
if operation in ["sin", "cos", "tan"]:

    angle = st.number_input("각도(°)를 입력하세요", value=0.0)

    if st.button("계산하기"):

        rad = math.radians(angle)

        if operation == "sin":
            result = math.sin(rad)

        elif operation == "cos":
            result = math.cos(rad)

        else:
            result = math.tan(rad)

        st.success(f"결과: {result}")

# 삼각함수 그래프
elif operation == "삼각함수 그래프":

    func = st.selectbox(
        "그래프를 선택하세요",
        ("sin", "cos", "tan")
    )

    if st.button("그래프 그리기"):

        x = np.linspace(-360, 360, 1000)
        rad = np.radians(x)

        if func == "sin":
            y = np.sin(rad)

        elif func == "cos":
            y = np.cos(rad)

        else:
            y = np.tan(rad)
            y = np.clip(y, -10, 10)

        fig, ax = plt.subplots()
        ax.plot(x, y)

        ax.set_title(f"{func} 그래프")
        ax.set_xlabel("각도(°)")
        ax.set_ylabel(func)
        ax.grid(True)

        st.pyplot(fig)

# 로그 연산
elif operation == "로그 연산":

    number = st.number_input(
        "로그를 계산할 숫자",
        min_value=0.0001,
        value=10.0
    )

    base = st.number_input(
        "로그 밑",
        min_value=0.0001,
        value=10.0
    )

    if st.button("계산하기"):

        result = math.log(number, base)
        st.success(f"결과: {result}")

# 나머지 계산
else:

    num1 = st.number_input("첫 번째 숫자", value=0.0)
    num2 = st.number_input("두 번째 숫자", value=0.0)

    if st.button("계산하기"):

        if operation == "덧셈":
            result = num1 + num2

        elif operation == "뺄셈":
            result = num1 - num2

        elif operation == "곱셈":
            result = num1 * num2

        elif operation == "나눗셈":
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
                st.stop()
            result = num1 / num2

        elif operation == "모듈러 연산":
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
                st.stop()
            result = num1 % num2

        elif operation == "지수 연산":
            result = num1 ** num2

        st.success(f"결과: {result}")
        
