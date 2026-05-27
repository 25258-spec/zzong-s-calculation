import streamlit as st
import math

st.set_page_config(page_title="고급 계산기", page_icon="🧮")

st.title("🧮 고급 계산기 웹앱")

st.write("사칙연산, 모듈러, 지수, 로그 계산 기능을 제공합니다.")

# 연산 종류 선택
operation = st.selectbox(
    "연산을 선택하세요",
    (
        "덧셈",
        "뺄셈",
        "곱셈",
        "나눗셈",
        "모듈러 연산",
        "지수 연산",
        "로그 연산"
    )
)

# 로그 연산은 입력 방식이 다름
if operation == "로그 연산":
    number = st.number_input("로그를 계산할 숫자", min_value=0.0001, value=10.0)
    base = st.number_input("로그 밑", min_value=0.0001, value=10.0)

    if st.button("계산하기"):
        result = math.log(number, base)
        st.success(f"결과: {result}")

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
            result = num1 % num2

        elif operation == "지수 연산":
            result = num1 ** num2

        st.success(f"결과: {result}")
