from datetime import datetime, timedelta

mfg_date_input = input("Enter manufacture date (YYYY-MM-DD): ")
valid_days = int(input("Enter validity in days: "))

mfg_date = datetime.strptime(mfg_date_input, "%Y-%m-%d")

expiry_date = mfg_date + timedelta(days=valid_days)
today = datetime.today()

if today > expiry_date:
    status = "❌ Expired"
else:
    status = "✅ Valid"

print("\n--- Product Expiry Details ---")
print(f"Manufacture Date : {mfg_date.strftime('%d-%m-%Y')}")
print(f"Expiry Date      : {expiry_date.strftime('%d-%m-%Y')}")
print(f"Status           : {status}")
