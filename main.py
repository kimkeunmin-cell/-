# main.py
import streamlit as st
import math
import numpy as np
import pandas as pd
import plotly.express as px

def calculator_app():
    st.header("🧮 계산기")
    st.write("사칙연산, 모듈러, 지수, 로그 기능을 제공합니다.")
    연산 = st.selectbox(
        "원하시는 연산을 선택하세요:",
        ("덧셈 (+)", "뺄셈 (-)", "곱셈 (×)", "나눗셈 (÷)",
         "모듈러 (a mod b)", "지수 (a^b)", "로그 (log_b a)")
    )

    # 입력 필드 및 설명
    if 연산 == "덧셈 (+)":
        st.write("두 숫자를 입력하세요. 결과는 첫 번째 숫자 + 두 번째 숫자 입니다.")
        a = st.number_input("첫 번째 숫자", value=0.0, key="calc_add_a")
        b = st.number_input("두 번째 숫자", value=0.0, key="calc_add_b")
    elif 연산 == "뺄셈 (-)":
        st.write("두 숫자를 입력하세요. 결과는 첫 번째 숫자 − 두 번째 숫자 입니다.")
        a = st.number_input("첫 번째 숫자", value=0.0, key="calc_sub_a")
        b = st.number_input("두 번째 숫자", value=0.0, key="calc_sub_b")
    elif 연산 == "곱셈 (×)":
        st.write("두 숫자를 입력하세요. 결과는 첫 번째 숫자 × 두 번째 숫자 입니다.")
        a = st.number_input("첫 번째 숫자", value=0.0, key="calc_mul_a")
        b = st.number_input("두 번째 숫자", value=0.0, key="calc_mul_b")
    elif 연산 == "나눗셈 (÷)":
        st.write("두 숫자를 입력하세요. 결과는 첫 번째 숫자 ÷ 두 번째 숫자 입니다. 두 번째 숫자는 0이 될 수 없습니다.")
        a = st.number_input("첫 번째 숫자", value=0.0, key="calc_div_a")
        b = st.number_input("두 번째 숫자 (0이 아닙니다)", value=1.0, key="calc_div_b")
    elif 연산 == "모듈러 (a mod b)":
        st.write("두 정수를 입력하세요. 결과는 첫 번째 정수 mod 두 번째 정수 입니다. 두 번째 정수는 0이 될 수 없습니다.")
        a = st.number_input("첫 번째 정수", value=0, step=1, format="%d", key="calc_mod_a")
        b = st.number_input("두 번째 정수 (0이 아닙니다)", value=1, step=1, format="%d", key="calc_mod_b")
    elif 연산 == "지수 (a^b)":
        st.write("두 숫자를 입력하세요. 결과는 첫 번째 숫자 ^ 두 번째 숫자 입니다.")
        a = st.number_input("밑 (a)", value=0.0, key="calc_exp_a")
        b = st.number_input("지수 (b)", value=1.0, key="calc_exp_b")
    elif 연산 == "로그 (log_b a)":
        st.write("두 숫자를 입력하세요. 결과는 밑(b)을 기준으로 한 로그 값입니다. a>0, b>0 그리고 b≠1 이어야 합니다.")
        a = st.number_input("로그할 숫자 (a, a>0)", value=1.0, key="calc_log_a")
        b = st.number_input("밑 (b, b>0 그리고 b≠1)", value=10.0, key="calc_log_b")
    else:
        st.error("알 수 없는 연산입니다.")
        return

    error = None
    result = None
    try:
        if 연산 == "덧셈 (+)":
            result = a + b
        elif 연산 == "뺄셈 (-)":
            result = a - b
        elif 연산 == "곱셈 (×)":
            result = a * b
        elif 연산 == "나눗셈 (÷)":
            if b == 0:
                error = "오류: 두 번째 숫자가 0이면 나눗셈을 할 수 없습니다."
            else:
                result = a / b
        elif 연산 == "모듈러 (a mod b)":
            if b == 0:
                error = "오류: 두 번째 정수가 0이면 모듈러 연산을 할 수 없습니다."
            else:
                result = int(a) % int(b)
        elif 연산 == "지수 (a^b)":
            result = a ** b
        elif 연산 == "로그 (log_b a)":
            if a <= 0 or b <= 0 or b == 1:
                error = "오류: 로그 계산 시에는 a>0, b>0 그리고 b≠1 이어야 합니다."
            else:
                result = math.log(a, b)
        else:
            error = "알 수 없는 연산입니다."
    except Exception as e:
        error = f"오류 발생: {e}"

    st.write("---")
    if error:
        st.error(error)
    else:
        st.success(f"결과: {result}")


def probability_simulator_app():
    st.header("🎲 확률 시뮬레이터")
    st.write("동전 또는 주사위를 선택하고, 시행 횟수를 입력하면 결과를 그래프로 확인할 수 있습니다.")
    realisation_type = st.selectbox("시뮬레이션 유형을 선택하세요:", ("동전 던지기", "주사위 굴리기"))

    trials = st.number_input("시행 횟수", min_value=1, value=100, step=1, key="sim_trials")

    if realisation_type == "동전 던지기":
        results = np.random.choice(["앞면", "뒷면"], size=trials)
        counts = {face: int((results == face).sum()) for face in ["앞면", "뒷면"]}
        df = pd.DataFrame({"결과": list(counts.keys()), "횟수": list(counts.values())})
        fig = px.bar(df, x="결과", y="횟수", title="동전 던지기 결과", text="횟수")
        st.plotly_chart(fig, use_container_width=True)
        st.write(f"총 시행 횟수: {trials}")
        st.write(f"앞면: {counts['앞면']}회, 뒷면: {counts['뒷면']}회")

    elif realisation_type == "주사위 굴리기":
        results = np.random.choice([1,2,3,4,5,6], size=trials)
        unique, counts_arr = np.unique(results, return_counts=True)
        df = pd.DataFrame({"눈": unique.tolist(), "횟수": counts_arr.tolist()})
        fig = px.bar(df, x="눈", y="횟수", title="주사위 굴리기 결과", text="횟수")
        fig.update_layout(xaxis_title="주사위 눈", yaxis_title="횟수")
        st.plotly_chart(fig, use_container_width=True)
        st.write(f"총 시행 횟수: {trials}")
        for eye, cnt in zip(unique.tolist(), counts_arr.tolist()):
            st.write(f"{eye} 눈: {cnt}회")

    else:
        st.error("알 수 없는 시뮬레이션 유형입니다.")


def world_population_analysis_app():
    st.header("🌍 연도별 세계인구 분석")
    st.write("연도별로 세계 각국의 인구를 지도 상에서 색으로 표현합니다.")

    # 연도 선택
    year = st.selectbox("연도를 선택하세요:", ("1970", "1980", "1990", "2000", "2010", "2015", "2020", "2022"))

    # 데이터 로드 (예: CSV 파일)
    # 여기서는 예시로 파일명이 'world_population_by_country.csv' 라고 가정
    # 파일은 컬럼: CountryCode, CountryName, Year1970, Year1980, ..., Year2022
    df_pop = pd.read_csv("world_population.csv", dtype={"CountryCode": str})
    # 선택한 연도 컬럼 이름
    col_year = f"Year{year}"
    if col_year not in df_pop.columns:
        st.error(f"데이터에 '{col_year}' 컬럼이 없습니다.")
        return

    # 지도 시각화를 위해 ISO-3 코드 이용
    fig = px.choropleth(
        df_pop,
        locations="CountryCode",
        color=col_year,
        hover_name="CountryName",
        color_continuous_scale="Viridis",
        title=f"{year}년 세계 인구 분포 (국가별)",
        labels={col_year: "인구수"}
    )
    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=False),
        margin={"r":0,"t":50,"l":0,"b":0}
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write(f"선택한 연도: {year}년")
    st.write("색이 진할수록 해당 국가의 인구가 많음을 의미합니다.")


def main():
    st.sidebar.title("메뉴")
    app_mode = st.sidebar.selectbox(
        "앱을 선택하세요:",
        ("계산기", "확률 시뮬레이터", "연도별 세계인구 분석")
    )

    if app_mode == "계산기":
        calculator_app()
    elif app_mode == "확률 시뮬레이터":
        probability_simulator_app()
    elif app_mode == "연도별 세계인구 분석":
        world_population_analysis_app()
    else:
        st.sidebar.error("알 수 없는 모드입니다.")

if __name__ == "__main__":
    main()
