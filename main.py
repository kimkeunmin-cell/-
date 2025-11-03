import streamlit as st
import math

def main():
    st.title("🧮 계산기 웹앱")
    st.write("사칙연산, 모듈러, 지수, 로그 기능을 제공합니다.")
    st.write("---")

    # 입력값
    num1 = st.number_input("첫 번째 숫자", value=0.0)
    num2 = st.number_input("두 번째 숫자", value=0.0)

    operation = st.selectbox(
        "연산 선택",
        ("덧셈 (+)", "뺄셈 (-)", "곱셈 (×)", "나눗셈 (÷)", "모듈러 (a mod b)", "지수 (a^b)", "로그 (log_b a)")
    )

    result = None
    error = None

    try:
        if operation == "덧셈 (+)":
            result = num1 + num2
        elif operation == "뺄셈 (-)":
            result = num1 - num2
        elif operation == "곱셈 (×)":
            result = num1 * num2
        elif operation == "나눗셈 (÷)":
            if num2 == 0:
                error = "오류: 두 번째 숫자가 0이면 나눗셈을 할 수 없습니다."
            else:
                result = num1 / num2
        elif operation == "모듈러 (a mod b)":
            if num2 == 0:
                error = "오류: 두 번째 숫자가 0이면 모듈로 연산을 할 수 없습니다."
            else:
                # 모듈러는 정수로 계산하는 것이 일반적이므로 int 변환
                result = int(num1) % int(num2)
        elif operation == "지수 (a^b)":
            result = num1 ** num2
        elif operation == "로그 (log_b a)":
            # 로그 밑과 숫자 모두 양수여야 함
            if num1 <= 0 or num2 <= 0 or num2 == 1:
                error = ("오류: 로그 계산 시에는 a>0, b>0 그리고 b≠1 이어야 합니다.")
            else:
                result = math.log(num1, num2)
        else:
            error = "알 수 없는 연산입니다."
    except Exception as e:
        error = f"오류 발생: {e}"

    st.write("---")
    if error:
        st.error(error)
    else:
        st.success(f"결과: {result}")

if __name__ == "__main__":
    main()
