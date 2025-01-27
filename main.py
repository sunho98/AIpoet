#from dotenv import load_dotenv
#load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(openai_api_key="your_key")

st.title('인공지능 시인')

content = st.text_input("시의 주제를 정해주세요")

if st.button("시 작성 요청하기"):
    result  = chat_model.predict(content + "에 대한 시를 써줘")
    st.write(result)