import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# 타이틀
st.title("촉매와 반응속도 시뮬레이션 실험")
st.markdown("### 실험 시나리오: 3% 과산화수소 + 주방세제 + 다양한 촉매")

# 초기 설명
st.markdown("모든 시험관에 **3% 과산화수소수**와 **주방세제 3스푼**이 들어있습니다.")
st.markdown("각 시험관에 하나씩 촉매를 넣고, 반응 속도를 확인해보세요!")

# 시험관 목록
catalysts = {
    "시험관 1": "인산",
    "시험관 2": "아이오딘화 칼륨",
    "시험관 3": "이산화 망가니즈",
    "시험관 4": "썰은 감자",
    "시험관 5": "촉매 없음 (비교군)"
}

# 촉매별 반응 속도 시뮬레이션 (임의 설정)
reaction_rates = {
    "인산": 0.3,
    "아이오딘화 칼륨": 0.8,
    "이산화 망가니즈": 1.0,
    "썰은 감자": 0.6,
    "촉매 없음 (비교군)": 0.1
}

# 반응 그래프 생성 함수
def show_reaction(catalyst_name, rate):
    st.write(f"⏱️ **{catalyst_name}을(를) 넣은 후 반응 시작!**")
    progress = st.progress(0)
    chart_placeholder = st.empty()

    x = []
    y = []

    for t in range(1, 11):
        x.append(t)
        y.append(rate * t + np.random.normal(0, 0.05))
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o')
        ax.set_title("거품 생성량(ml) vs 시간(초)")
        ax.set_xlabel("시간 (초)")
        ax.set_ylabel("거품 생성량 (ml)")
        chart_placeholder.pyplot(fig)
        progress.progress(t * 10)
        time.sleep(0.3)

    st.success(f"✅ {catalyst_name} 반응 완료!")

# 버튼으로 하나씩 실험 시작
for key, catalyst in catalysts.items():
    if st.button(f"{key}: {catalyst} 넣기"):
        show_reaction(catalyst, reaction_rates[catalyst])
        st.stop()  # 한 번에 하나씩만 실행되도록 정지
