import streamlit as st
from model import classifier
from razdel import sentenize


st.title("Sentiment analysis evaluetor")

in_text = st.text_input("Enter a sentence to evaluate the sentiment \
of the text (only English)", "Write your text here. You can write any sentences.")

eval_sep = st.checkbox('Evaluate the sentences in the text separately', True)
if eval_sep:
    text = [list(sent)[2] for sent in list(sentenize(in_text))]
else:
    text = [in_text]


result = st.button("Evaluate!")
if result:
    evals = classifier(text)
    st.subheader("Result:", divider='rainbow')
    result = [
        {
            'Text': text[i],
            'Mood': eval['label'],
            'Score': round(eval['score'], 5)
        }
        for i, eval in enumerate(evals)
        ]
    st.table(result)
