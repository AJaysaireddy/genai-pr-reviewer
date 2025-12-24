import streamlit as st
from review_engine import run_all_reviews

st.set_page_config(page_title="AI PR Reviewer", layout="wide")
st.title("AI PR Reviewer")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Before Code")
    before_code = st.text_area(
        "Paste BEFORE code here",
        height=300,
        placeholder="Paste original code here..."
    )

with col2:
    st.subheader("After Code")
    after_code = st.text_area(
        "Paste AFTER code here",
        height=300,
        placeholder="Paste modified code here..."
    )

st.markdown("---")

if st.button("Run Review"):
    if not before_code.strip() or not after_code.strip():
        st.warning("Please paste both BEFORE and AFTER code.")
    else:
        with st.spinner("Reviewing code..."):
            results = run_all_reviews(before_code, after_code)

        for section, output in results:
            st.subheader(section)
            st.markdown(output)
