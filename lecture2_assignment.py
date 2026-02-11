import streamlit as st
import random
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Lecture 2 Assignment", page_icon="📚", layout="centered")

st.title("📚 Lecture 2 Assignment")
tabs = st.tabs(["🏋️ Gym Fee Calculator", "💳 E-Wallet", "📦 Expiry Date Tracker", "🔐 OTP Verification"])

# --- Gym Fee Calculator ---
with tabs[0]:
    st.header("🏋️ Gym Membership Fee Calculator")
    st.write("Enter your details to calculate the total fee:")
    reg_fee = st.number_input("Enter Registration Fee (Rs):", min_value=0, step=100, key="reg_fee")
    monthly_fee = st.number_input("Enter Monthly Fee (Rs):", min_value=0, step=100, key="monthly_fee")
    months = st.number_input("Enter Number of Months:", min_value=1, step=1, key="months")
    coupon = st.checkbox("I have a 10% discount coupon", key="coupon")
    if st.button("Calculate Total Fee", key="calc_fee"):
        total = reg_fee + (monthly_fee * months)
        total *= 0.9 if coupon else 1
        st.success(f"💰 Final Amount to Pay: Rs {total:.2f}")

# --- E-Wallet ---
with tabs[1]:
    st.header("💳 Simple E-Wallet")
    st.write("Add money and track your spending easily")
    if "wallet" not in st.session_state:
        st.session_state.wallet = 0
    add_money = st.number_input("How much money do you want to add?", min_value=0, step=100, key="add_money")
    food = st.number_input("How much money did you spend on food?", min_value=0, step=50, key="food")
    transport = st.number_input("How much money did you spend on transport?", min_value=0, step=50, key="transport")
    shopping = st.number_input("How much money did you spend on shopping?", min_value=0, step=50, key="shopping")
    if st.button("Calculate Balance", key="calc_balance"):
        st.session_state.wallet += add_money
        st.session_state.wallet -= food
        st.session_state.wallet -= transport
        st.session_state.wallet -= shopping
        check = st.session_state.wallet > 500 and st.session_state.wallet < 5000
        st.success(f"💰 Final Wallet Balance: Rs {st.session_state.wallet}")
        st.info(f"Balance between 500 and 5000: {check}")

# --- Expiry Date Tracker ---
with tabs[2]:
    st.header("📦 Expiry Date Tracker")
    st.write("Check if your product is **Valid** or **Expired** based on manufacture date and validity period.")
    mfg_date = st.date_input("📅 Select Manufacture Date", key="mfg_date")
    valid_days = st.number_input("⏳ Enter Validity (in days)", min_value=1, step=1, key="valid_days")
    if st.button("Check Expiry", key="check_expiry"):
        mfg_date_dt = datetime.combine(mfg_date, datetime.min.time())
        expiry_date = mfg_date_dt + timedelta(days=valid_days)
        today = datetime.today()
        if today > expiry_date:
            status = "❌ Expired"
            st.error(status)
        else:
            status = "✅ Valid"
            st.success(status)
        st.markdown("### 📌 Product Expiry Details")
        st.write(f"**Manufacture Date:** {mfg_date_dt.strftime('%d-%m-%Y')}")
        st.write(f"**Expiry Date:** {expiry_date.strftime('%d-%m-%Y')}")
        st.write(f"**Status:** {status}")

# --- OTP Verification ---
with tabs[3]:
    st.header("🔐 OTP Verification System")
    st.write("Send amount securely using OTP verification")
    if "otp" not in st.session_state:
        st.session_state.otp = None
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if "verified" not in st.session_state:
        st.session_state.verified = False
    amount = st.text_input("💰 Enter the amount to send:", key="otp_amount")
    if st.button("Generate OTP", key="gen_otp"):
        if amount == "":
            st.warning("Please enter amount first")
        else:
            st.session_state.otp = random.randint(100000, 999999)
            st.session_state.start_time = time.time()
            st.session_state.verified = False
            st.info(f"📩 Your OTP is: {st.session_state.otp} (simulated sending)")
    user_otp = st.text_input("🔢 Enter OTP:", key="user_otp")
    if st.button("Verify OTP", key="verify_otp"):
        if st.session_state.otp is None:
            st.warning("Please generate OTP first")
        else:
            time_taken = time.time() - st.session_state.start_time
            if time_taken <= 10 and user_otp == str(st.session_state.otp):
                st.success("✅ Amount Sent Successfully")
                st.session_state.verified = True
            else:
                st.error("❌ OTP Expired or Incorrect")
    if st.session_state.start_time:
        remaining_time = int(10 - (time.time() - st.session_state.start_time))
        if remaining_time > 0:
            st.write(f"⏳ Time left: {remaining_time} seconds")
        else:
            st.write("⏰ OTP time expired")
