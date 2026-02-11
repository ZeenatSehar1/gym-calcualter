import streamlit as st

st.set_page_config(page_title="Gym Fee Calculator", page_icon="🏋️", layout="centered")

st.title("🏋️ Gym Membership Fee Calculator")
st.write("Enter your details to calculate the total fee:")

reg_fee = st.number_input("Enter Registration Fee (Rs):", min_value=0, step=100)
monthly_fee = st.number_input("Enter Monthly Fee (Rs):", min_value=0, step=100)
months = st.number_input("Enter Number of Months:", min_value=1, step=1)

coupon = st.checkbox("I have a 10% discount coupon")

if st.button("Calculate Total Fee"):
    total = reg_fee + (monthly_fee * months)

    # apply discount using assignment operator
    total *= 0.9 if coupon else 1

    st.success(f"💰 Final Amount to Pay: Rs {total:.2f}")
