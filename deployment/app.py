import streamlit as st
import eda
import predict

page = st.sidebar.selectbox('Page', ('EDA', 'Prediction Page'))

if page == 'EDA':
    eda.run()
else:
    predict.run()