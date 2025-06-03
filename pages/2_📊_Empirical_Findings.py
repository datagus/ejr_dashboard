import streamlit as st
import pandas as pd
#import json
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("📊 Main Empirical Findings")


# Load once and cache using Streamlit's built-in cache
@st.cache_data
def load_data():
    #con_file = open("gsheet.json")
    #file_key = json.load(con_file)
    #con_file.close()
    #loading google spreadsheet
    spreadsheet_id = st.secrets["id"]  #from the json file
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=xlsx"
    xls = pd.ExcelFile(url)
    return xls.parse("Sheet1")


df = load_data()

# Creating 3 columns for each filter section
col1, col2, col3 =  st.columns(3)

# ---- Filter section 1: Authors ----
with col1:
    st.subheader("Authors")
    coauthors_filter = st.selectbox("Select if authors were co-authors", ('all', '-', 'Yes', 'No', 'not determined'))
    acknowledged_filter = st.selectbox("Select if actors were acknowledged", ('all', '-', 'Yes', 'No', 'not determined'))

# ---- Filter section 2: Justice ----
with col2:
    st.subheader("Justice")
    distributive_filter = st.selectbox("Select if distributive justice appeared", ('all', '-', 'Yes', 'No'))
    procedural_filter = st.selectbox("Select if procedural justice apparead", ('all', '-', 'Yes', 'No'))
    recognition_filter = st.selectbox("Select if recognition justice apparead", ('all', '-', 'Yes', 'No'))

# ---- Filter section 3: Ethics ----
with col3:
    st.subheader("Ethics")
    ethics_filter = st.selectbox("Select if ethics based appeared", ('all', '-', 'Yes', 'No'))
    consequence_filter = st.selectbox("Select if consequence based apparead", ('all', '-', 'Yes', 'No'))
    contract_filter = st.selectbox("Select if social contract based apparead", ('all', '-', 'Yes', 'No'))
    policy_filter = st.selectbox("Select if there were policy recommendations", ('all', '-', 'Yes', 'No'))
    policy_applied_filter = st.selectbox("Select if policies were proposed and applied", ('all', '-', 'Yes', 'No'))


# ------ showing dataframe ---------
# Copying the original df
f_df = df.copy() #f_df stands for filtered_df


if coauthors_filter != "all":
    f_df = f_df.loc[f_df['actor_co-author'] == coauthors_filter,]
if acknowledged_filter != "all":
    f_df = f_df.loc[f_df['actor_acknowledged'] == acknowledged_filter,]

if distributive_filter != "all":
    f_df = f_df.loc[f_df['EJ_distributive'] == distributive_filter,]
if procedural_filter != "all":
    f_df = f_df.loc[f_df['EJ_procedual'] == procedural_filter,]
if recognition_filter != "all":
    f_df = f_df.loc[f_df['EJ_recognition'] == recognition_filter,]

if ethics_filter != "all":
    f_df = f_df.loc[f_df['ethics_rule_based'] == ethics_filter,]
if consequence_filter != "all":
    f_df = f_df.loc[f_df['ethics_consequence_based'] == consequence_filter,]
if contract_filter != "all":
    f_df = f_df.loc[f_df['ethics_contract_based'] == contract_filter,]
if policy_filter != "all":
    f_df = f_df.loc[f_df['policy_relevance'] == policy_filter,]
if policy_applied_filter != "all":
    f_df = f_df.loc[f_df['policy_relevance_applied'] == policy_applied_filter,]


# Creating 3 columns for each filter section
col4, col5 =  st.columns(2)

with col4:
    # Display the filtered dataframe
    st.subheader("Subselected dataframe")
    st.dataframe(f_df.reset_index(drop=True))

with col5:
    st.subheader("Count of articles by")
    variables = f_df.iloc[:,6:17].columns.tolist()
    variables.remove("study_location_coordinates")
    select_variable = st.selectbox("Choose variable", variables)
    if select_variable:
        selected_variable = select_variable
    # Create the countplot
    fig,ax = plt.subplots()
    sns.countplot(data=f_df, y=selected_variable, color="purple", ax=ax)
    # Display the plot in Streamlit
    st.pyplot(fig)