import streamlit as st
from datetime import datetime

# Step 1: Get user budget
st.title("Expense Tracker")

if "budget" not in st.session_state:
    st.session_state.budget_set = False
    st.session_state.budget = 0.0

if "expenses" not in st.session_state:
    st.session_state.expenses = []

if not st.session_state.budget_set:
    budget_input = st.number_input("Enter your total budget ($)", min_value=0.0, format="%.2f")
    if st.button("Set Budget"):
        st.session_state.budget = budget_input
        st.session_state.budget_set = True
        st.success(f"Budget set to ${budget_input:.2f}")
    st.stop()

# Step 2: Expense Input Form
with st.form("expense_form"):
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
    amount = st.number_input("Amount ($)", min_value=0.0, format="%.2f")
    receipt = st.file_uploader("Upload Receipt (optional)", type=["png", "jpg", "jpeg", "pdf"])
    submitted = st.form_submit_button("Add Expense")

    # Step 3: Process the Expense
    if submitted:
        if amount > 0:
            expense = {
                "category": category,
                "amount": amount,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "receipt": receipt.name if receipt else "No Receipt"
            }
            st.session_state.expenses.append(expense)

            # Step 4: Display Success Message
            st.success(f"Added ${amount:.2f} to {category}")
        else:
            st.error("Amount must be greater than 0.")

# Step 5: Show Expense List
if st.session_state.expenses:
    st.subheader("All Expenses")
    for e in st.session_state.expenses:
        st.write(f"{e['timestamp']} - {e['category']} - ${e['amount']:.2f} - Receipt: {e['receipt']}")

    # Step 6: Calculate and Display Totals
    total = sum(e["amount"] for e in st.session_state.expenses)
    remaining = st.session_state.budget - total

    st.write(f"Total Expenses: ${total:.2f}")
    st.write(f"Remaining Budget: ${remaining:.2f}")

    if remaining < 0:
        st.warning("You have exceeded your budget!")
else:
    st.info("No expenses added yet.")
