import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.agent import exchange_agent
st.set_page_config(page_title="Currency News AI", layout="centered")

st.title("💱 Currency Pair Insights")
st.subheader("Select a currency pair")

currencies = ['USD', 'INR', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD']

col1, col2,col3 = st.columns(3)
with col1:
    from_currency = st.selectbox("From", currencies)
with col2:
    to_currency = st.selectbox("To", currencies)
with col3:
    amount=st.number_input("Amount")
if st.button("Submit"):
    if from_currency == to_currency:
        st.warning("Choose different currencies.")
    else:
        pair = f"{from_currency}/{to_currency}/{amount}"
        with st.spinner("Thinking..."):
            response = exchange_agent(pair)
        st.markdown("### 💹 Conversion Rate")
        st.write(response.get("rate"))
        st.markdown("### 📰 News")
        st.write(response.get("news"))
