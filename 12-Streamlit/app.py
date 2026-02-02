import streamlit as st
import pandas as pd
import numpy as np

# df = pd.read_csv('sales_data.csv')
# st.write(df)
# # st.line_chart(df)
st.title("Streamlit basics")
st.write("this is my first proj")
name = st.text_input("Enter your name")
if name:
    st.write("hello",name)
age = st.slider("select age",0,100,20)
st.write(age)
st.selectbox("choose lang",["python","java","c++","rust"])
upload_file = st.file_uploader("choose",type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)

df1 = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


## Display the Dataframe
st.write("Here is the dataframe")
st.write(df1)

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)