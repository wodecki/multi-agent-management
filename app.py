import requests
import streamlit as st
from dotenv import load_dotenv
from graph.graph import app

load_dotenv()

st.title("STORM Agent")

st.write("------")

question = st.text_input("Ask your question",
                         help="1. Help a multinational manufacturing company in their journey to product management maturity. \n\n "
                              "2. Advise an international logistics company on developing a strategic roadmap for enhancing product lifecycle management.")

tab1, tab2 = st.tabs(['Using API', 'Local'])

with tab1:
    if st.button("Get report", key=1):
        response = requests.get(f"http://127.0.0.1:8000/generate-report?topic={question}")

        if response.status_code == 200:
            data = response.json()
            st.markdown(data.get('content', 'No content in response.'))
        else:
            st.error(f"Failed to fetch report: {response.status_code} - {response.text}")

with tab2:
    if st.button("Get report", key=2):
        st.markdown(app.invoke({"topic": question}, config={"configurable": {"thread_id": "1"}})['report'].content)