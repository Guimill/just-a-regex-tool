import streamlit as st
import pandas as pd

def main():
    st.title("CSV Transformer")

    st.write("Upload your CSV file:")
    uploaded_file = st.file_uploader("Choose a file", type=['csv'])

    if uploaded_file is not None:
        # Specify the separator as ';', skip the first line, don't include the index column, and indicate no header
        dataframe = pd.read_csv(uploaded_file, sep=';', skiprows=1, index_col=None, header=None)
        # Drop the first column
        dataframe = dataframe.iloc[:, 1:]
        
        # Replace double whitespace with commas
        dataframe.replace(to_replace=r'\s\s', value=',', regex=True, inplace=True)
        # Replace 'NaN' with empty quotes
        dataframe.replace(to_replace=r'^NaN$', value='""', regex=True, inplace=True)
        
        st.write("Original CSV:")
        # Convert DataFrame to CSV-like format and join all rows into a single string
        csv_string = '\n'.join([','.join(map(str, row)) for index, row in dataframe.iterrows()])
        # Display the CSV-like string
        st.code(csv_string)

if __name__ == "__main__":
    main()
