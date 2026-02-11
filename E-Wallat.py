import streamlit as st

st.set_page_config(page_title="E-Wallet App", page_icon="💳", layout="centered")

st.title("💳 Simple E-Wallet")
st.write("Add money and track your spending easily")

wallet = 0

add_money = st.number_input("How much money do you want to add?", min_value=0, step=100)
food = st.number_input("How much money did you spend on food?", min_value=0, step=50)
transport = st.number_input("How much money did you spend on transport?", min_value=0, step=50)
shopping = st.number_input("How much money did you spend on shopping?", min_value=0, step=50)

if st.button("Calculate Balance"):
    wallet += add_money
    wallet -= food
    wallet -= transport
    wallet -= shopping

    check = wallet > 500 and wallet < 5000

    st.success(f"💰 Final Wallet Balance: Rs {wallet}")
    st.info(f"Balance between 500 and 5000: {check}")
