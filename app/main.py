import os
import shutil
import streamlit as st
import pandas as pd
from langchain_community.document_loaders import WebBaseLoader
from chain import Chain
from portfolio import Portfolio
from utils import clean_text

VECTOR_STORE_DIR = "vectorstore"  # replace with your actual folder name

def delete_vectorstore_folder():
    if os.path.exists(VECTOR_STORE_DIR):
        shutil.rmtree(VECTOR_STORE_DIR)
        st.info(f"Deleted existing vector store folder: `{VECTOR_STORE_DIR}`")

def create_streamlit_app(llm, clean_text):
    st.title("📧 Cold Mail Generator")
    uploaded_file = st.file_uploader('Choose a CSV file (columns must include `TechStack` and `Links`)', type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if 'TechStack' in df.columns and 'Links' in df.columns:
            portfolio = Portfolio(data=df)
            # delete_vectorstore_folder()
            person_input = st.sidebar.text_input("Person Name")
            company_input = st.sidebar.text_input("Company Name")
            url_input = st.text_input("Enter a URL:")
            submit_button = st.button("Submit")

            if submit_button and person_input and company_input and url_input:
                try:
                    loader = WebBaseLoader([url_input])
                    data = clean_text(loader.load().pop().page_content)
                    portfolio.load_portfolio()
                    jobs = llm.extract_jobs(data)
                    for job in jobs:
                        skills = job.get('skills', [])
                        links = portfolio.query_links(skills)
                        email = llm.write_mail(job=job, links=links, person_name=person_input, company=company_input)
                        st.code(email, language='markdown')
                except Exception as e:
                    st.error(f"An Error Occurred: {e}")
            else:
                st.warning("Please fill all the fields")
        else:
            st.warning('`TechStack` and `Links` is not available')


if __name__ == "__main__":
    llm = Chain()
    st.set_page_config(layout="wide", page_icon="📧", page_title="Mail Generator")
    create_streamlit_app(llm, clean_text)

