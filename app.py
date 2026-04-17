
import streamlit as st
from ai_agent_llm import ai_agent_llm

st.set_page_config(page_title="Flight Booking AI", layout="centered")

st.title("✈️ AI Flight Booking Assistant")

st.write("Ask me to book a flight (cheapest or expensive)")

# User input
user_input = st.text_input("Enter your request:")
email = st.text_input("Enter your email:")

if st.button("Book Flight"):

    if user_input and email:
        result = ai_agent_llm(user_input, email)

        st.success("✅ Ticket Booked!")

        st.write("### ✈️ Flight Details")
        st.write(f"**Airline:** {result['airline']}")
        st.write(f"**Price:** ₹{result['price']}")
        st.write(f"**PNR:** {result['pnr']}")
        st.write(f"**Status:** {result['status']}")

    else:
        st.warning("⚠️ Please enter both request and email")