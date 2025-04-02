import streamlit as st

st.title("Monthly Budget and Savings Goal")

with st.form("budget_form"):
    st.subheader("Enter your Budget Details")

    budget = st.slider("Monthly Budget ($)", 0, 10000, step=100)

    savings_input = st.text_input("Savings Goal ($)", placeholder="Enter amount")

    submitted = st.form_submit_button("Submit")

    if submitted:
        try:
            savings_goal = float(savings_input)
            if savings_goal > budget:
                st.error("Savings goal cannot be greater than your budget.")
            elif savings_goal < 0:
                st.error("Savings goal must be a positive number.")
            else:
                st.success(f" Your monthly budget is ${budget} and your savings goal is ${savings_goal}.")
        except ValueError:
            st.error("Please enter a valid number for the savings goal.")
