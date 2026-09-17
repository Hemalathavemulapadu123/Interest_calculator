import streamlit as st

st.title("Simple Interest Calculator")

principal = st.number_input("Enter Principal Amount")
rate = st.number_input("Enter Rate of Interest")
time = st.number_input("Enter Time (in years)")

if st.button("Calculate"):
    interest = (principal * rate * time) / 100
    total = principal + interest

    st.success("Simple Interest = " + str(interest))
    st.success("Total Amount = " + str(total))
