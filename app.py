import streamlit as st
import pandas as pd 
import plotly.express as px

file_path  = "test_data.csv"
df = pd.read_csv(file_path , index_col=[0])
# columns = ['stock_id', 'dt', 'message', 'source', 'url']

# st.plotly_chart()
with st.sidebar:
    select_mode = st.selectbox(
        "Mode",
        ("Mode 1", "Mode 2", "Mode 3")
    )
    option_select = st.radio(
        "Option",
        ("Option 1", "Option 2", "Option 3")
    )
    with st.echo():
        st.write("This will be printed.")

st.dataframe(df)