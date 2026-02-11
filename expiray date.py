import streamlit as st
from datetime import datetime, timedelta

# Page setup
st.set_page_config(
    page_title="Expiry Date Tracker",
    page_icon="📦",
    layout="centered"
)

# Title
st.title("📦 Expiry Date Tracker")
st.write("Check if your product is **Valid** or **Expired** based on manufacture date and validity period.")

# Step 1: User input
mfg_date = st.date_input("📅 Select Manufacture Date")
valid_days = st.number_input("⏳ Enter Validity (in days)", min_value=1, step=1)

# Step 2 & 3: Calculate and display on button click
if st.button("Check Expiry"):
    mfg_date_dt = datetime.combine(mfg_date, datetime.min.time())
    expiry_date = mfg_date_dt + timedelta(days=valid_days)
    today = datetime.today()
    
    # Determine status
    if today > expiry_date:
        status = "❌ Expired"
        st.error(status)
    else:
        status = "✅ Valid"
        st.success(status)
    
    # Display formatted results
    st.markdown("### 📌 Product Expiry Details")
    st.write(f"**Manufacture Date:** {mfg_date_dt.strftime('%d-%m-%Y')}")
    st.write(f"**Expiry Date:** {expiry_date.strftime('%d-%m-%Y')}")
    st.write(f"**Status:** {status}")
