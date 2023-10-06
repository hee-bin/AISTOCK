# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

# from langchain.llms import OpenAI
# llm = OpenAI()
# re = llm.predict("how are you!")
# print(re)

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title('AI report')
st.write('Welcome! :sunglasses:')



content = st.text_input('It is supposed to be with a stock chart ')

if st.button('I wanna a easier explain about the chart'):
    with st.spinner('Wait for it...'):
        prompt = "You are an amazing financial analyst. As an analyst, analyze the stock chart information in detail and give me your brief opinion in korean. here is the imformation"
        result = chat_model.predict(prompt + content )
        st.write(":pencil:"+ content)
        st.write(result)