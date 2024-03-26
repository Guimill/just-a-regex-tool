import streamlit as st
from streamlit.logger import get_logger
import re

LOGGER = get_logger(__name__)


def transform_list(input_text):

    lines = input_text.split('\n')
    transformed_lines = [line.strip() for line in lines if ')' in line]

    final_transform = []

    for line in transformed_lines:
        if line.strip():  # Check if line is not empty
            # Apply regex replacements
            line = re.sub(r'ad_nombat=', '', line)
            line = re.sub(r'Vide', '', line)
            line = re.sub(r'\)', '', line)
            line = re.sub(r'\(', '', line)
            line = re.sub(r'no name', '', line)
            line = re.sub(r'.\s',',',line)
            line = re.sub(r'\[\]','',line)
            line = re.sub(r'no','',line)
            line = re.sub(r'batimen','',line)
            line = re.sub(r'REFSITES=','',line)
            line = re.sub(r',,,',',,',line)
            line = re.sub(r'\,$','',line)
            line = re.sub(r',,N',',N',line)
            line = re.sub(r',,',',"",', line)
            line = re.sub(r',$',',""', line)


            final_transform.append(line)

    return '\n'.join(final_transform)


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
