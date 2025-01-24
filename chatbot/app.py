from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.llms import Ollama

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

#Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the following user inquiries."),
        ("user", "Question: {question}"),
    ]
)

# Streamlit App

st.title("Langchain Chatbot")
input_text = st.text_input("Enter your question here:")

# OLLAMA Chatbot

ollama = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt | ollama | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))

