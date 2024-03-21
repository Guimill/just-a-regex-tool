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
import re

LOGGER = get_logger(__name__)


def transform_list(input_text):
    # Split the input text by '\n' and remove empty lines
    input_list = filter(None, input_text.split('\n'))

    # Enclose each item in single quotes and join them with commas
    transformed_text = ','.join([f"'{item}'" for item in input_list])

    return f"({transformed_text})"

def main():
    st.title("List Transformer")

    st.write("Paste your list below (separated by \\n):")

    input_text = st.text_area("Input List", height=100)

    if st.button("Transform"):
        transformed_text = transform_list(input_text)
        st.write("Transformed List:")
        st.code(transformed_text)

if __name__ == "__main__":
    main()