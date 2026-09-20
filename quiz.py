import streamlit as st

st.write("Hello, I am Vishnu, Welcome to my quiz zone...Hope you like the game. You may please proceed further for gaming....")
age = st.number_input("Enter your age")
if age>= 20:
  st.write("you are eligible for license...")
  st.ballons()
else:
  st.write("you are not eligible...")
  
