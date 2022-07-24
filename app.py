import streamlit as st

def mul(a, b):
  return a*b

st.title('Multiplication App')

st.write("Multiplication of 2 given numbers")

a = st.number_input("Enter a number")

b = st.number_input("Enter another number")

st.write(mul(a, b))
