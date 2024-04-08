import streamlit as st
import numpy as np
import altair as alt
import pandas as pd


st.header("Streamlit Studies")

#day3 learn st.button

st.subheader('st.button')

st.write("let's check st.button function")

if st.button('Click to Button for hello'):
    st.write('hello there')
else:
    st.write('Goodbye')

#day5 learn st.write usages

st.subheader('st.write')

##example 1
st.write('1.)', 'Hello, *world!* :sunglasses:')

##example 2
st.write('2.)',1234)

##example3
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column':[10,20,30,40]
})
st.write('3.)',df)

##example4
st.write('4.)','Below is a dataframe:', df, '4.)','Above is a dataframe')

##example5
df2= pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write('5.)',c)
st.write('5.)',df2)