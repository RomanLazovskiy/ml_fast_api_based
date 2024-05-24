import streamlit as st
from tools import get_model_result

st.title("Sentiment analysis evaluetor")

in_text = st.text_input("Enter a sentence to evaluate the sentiment \
of the text (only English)", "Write your text here. You can write any \
sentences.")

eval_sep = st.checkbox('Evaluate the sentences in the text separately', True)

result = st.button("Evaluate!")
if result:
    st.subheader("Result:", divider='rainbow')
    result = get_model_result(text=in_text, sep=eval_sep)
    st.table(result)
