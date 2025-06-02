import streamlit as st

st.title("📊 Main Empirical Findings")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### 📌 Filters")
    st.selectbox("Select SDG", ["All", "SDG 4", "SDG 12", "SDG 13"])
    st.selectbox("Select AI Type", ["All", "ML", "DL", "NLP"])
    st.selectbox("Select Region", ["All", "Europe", "Asia", "Global"])

with col2:
    st.markdown("#### 📈 Summary of Results")
    st.info("Placeholder: Add summary metrics, key trends, and top algorithms.")

st.markdown("### 📂 Result Details")
st.dataframe({"Placeholder": ["Add detailed table here"]})