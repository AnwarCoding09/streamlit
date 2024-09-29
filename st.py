import streamlit as st
import joblib
st.title('hello world')
model = joblib.load('best_lr.pkl')

st.write('## salary')
x= st.slider('exp',0,40)
y = model.predict([[x]])
st.write('slaray is ',y)
# x = streamlit run st.py