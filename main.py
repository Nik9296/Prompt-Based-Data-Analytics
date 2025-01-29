from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import Agent
from pandasai.llm.openai import OpenAI

load_dotenv()

os.environ["PANDASAI_API_KEY"]="$2a$10$U1kZ.k8XozR/eP9Pb5zqW.hKbhfob3Y8.yeB61xelDPhclO6x015S"

st.title("Propmt driven Data Analytics")

dataset_option = st.selectbox(
    "Choose a dataset option",
    ("Upload CSV for analysis", "Use demo dataset")
)

if dataset_option == "Upload CSV for analysis":
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Dataset")
        st.write(df.head(3))
        ag = Agent(df)
else:
    # Load a demo dataset (e.g., Iris dataset)
    demo_data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(demo_data_url)
    st.write("### Demo Dataset (Iris)")
    st.write(df.head(3))
    ag = Agent(df)

prompt = st.text_area("Enter your prompt for data analysis")

if st.button("Generate"):
    if prompt:
        with st.spinner("Please wait..."):
            response = ag.chat(prompt)
        st.write("### Analysis Result")
        st.write(response)
    else:
        st.warning("Please enter a prompt!")




# "C:\Users\Aniket\OneDrive\Desktop\promt based anaysis\main.py"