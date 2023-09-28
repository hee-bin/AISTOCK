# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

# from langchain.llms import OpenAI
# llm = OpenAI()
# re = llm.predict("how are you!")
# print(re)

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title('welcome to make your own poem!')
st.write('Hello, *World!* :sunglasses:')



content = st.text_input('MAKING A COOOL POEM')

if st.button('submit'):
    with st.spinner('Wait for it...'):
        result = chat_model.predict("write a poem about" + content )
        st.write("subject is "+ content)
        st.write(result)