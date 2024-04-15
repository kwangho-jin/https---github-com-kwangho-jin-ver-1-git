# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello Kwangho",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit!Kwangho 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello Kwangho",
        page_icon="👋",
    )

    st.write("# Welcome to Kwangho's Streamlit Page! 👋")

    # Sidebar
    st.sidebar.success("Select a demo above.")

    # Main content area
    st.markdown("### Explore our Streamlit Demos")

    # Data for the table
    data = {
        "Demo Description": [
            "Machine Learning and Data Science projects",
            "Analyze the Udacity Self-driving Car Image Dataset",
            "Explore a New York City rideshare dataset"
        ],
        "Resource": [
            "Streamlit Documentation",
            "Self-driving Car Dataset Demo",
            "NYC Rideshare Data Demo"
        ],
        "Link": [
            "https://docs.streamlit.io",
            "https://github.com/streamlit/demo-self-driving",
            "https://github.com/streamlit/demo-uber-nyc-pickups"
        ]
    }

    # Display the table
    st.table(data)

    st.markdown("### Want to learn more?")
    st.markdown("""
    - Check out [streamlit.io](https://streamlit.io)
    - Ask a question in our [community forums](https://discuss.streamlit.io)
    """)

if __name__ == "__main__":
    run()
