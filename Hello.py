# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# 아파치 라이센스 버전 2.0 ("라이센스")에 따라 라이센스가 부여됩니다.
# 라이센스에 따라 이 파일을 사용할 수 없으며 라이센스를 준수해야 합니다.
# 라이센스 사본은 다음에서 얻을 수 있습니다.
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# 적용 가능한 법률에 필요하거나 서면으로 동의하지 않는 한,
# 라이센스에 따라 배포되는 소프트웨어는 "있는 그대로" 배포되며,
# 명시적이든 묵시적이든 어떠한 종류의 보증이나 조건 없이 배포됩니다.
# 라이센스에서 권한과 제한을 관리하는 조항을 참조하세요.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="안녕하세요, 광호",
        page_icon="👋",
    )

    st.write("# 광호님, Streamlit에 오신 것을 환영합니다! 👋")

    st.sidebar.success("위의 데모를 선택하세요.")

    st.markdown(
        """
        Streamlit은 특히 머신러닝과 데이터 과학 프로젝트를 위해 만들어진 오픈소스 앱 프레임워크입니다.
        **👈 사이드바에서 데모를 선택하세요** Streamlit이 할 수 있는 몇 가지 예제를 보실 수 있습니다!
        ### 더 알고 싶으신가요?
        - [streamlit.io](https://streamlit.io)를 확인하세요.
        - 우리의 [문서](https://docs.streamlit.io)로 뛰어 들어보세요.
        - [커뮤니티 포럼](https://discuss.streamlit.io)에서 질문하세요.
        ### 더 복잡한 데모를 보세요
        - 신경망을 사용하여 [Udacity 자율주행 자동차 이미지 데이터셋을 분석](https://github.com/streamlit/demo-self-driving)하세요.
        - [뉴욕시 라이드셰어 데이터셋을 탐색](https://github.com/streamlit/demo-uber-nyc-pickups)하세요.
    """
    )

if __name__ == "__main__":
    run()
