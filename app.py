import streamlit as st
import pandas as pd
from validator import validate

st.set_page_config(
    page_title="Data Validation Portal",
    layout="wide"
)

st.title("Data Validation Portal")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    st.subheader("Uploaded Data")

    st.dataframe(df)

    if st.button("Validate Data"):

        error_df = validate(df)

        total = len(df)
        failed = error_df["Row"].nunique() if not error_df.empty else 0
        passed = total - failed

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Rows", total)
        col2.metric("Passed", passed)
        col3.metric("Failed", failed)

        st.divider()

        if error_df.empty:

            st.success("No validation issues found")

        else:

            st.error(f"{len(error_df)} issues found")

            st.dataframe(error_df)
