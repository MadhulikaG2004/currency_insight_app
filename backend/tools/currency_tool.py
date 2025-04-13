import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_exchange_rate(pair: dict) -> str:
    try:
        from_curr, to_curr, amount_str = pair.get("pair").split("/")
        amount = float(amount_str)
    except ValueError:
        return "Invalid input format. Use 'USD/EUR/100' format."

    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_curr}/{to_curr}/{amount}"
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        return f"Error reaching the API: {e}"

    if data.get("result") == "success":
        rate = data["conversion_rate"]
        converted = data["conversion_result"]
        return (
            f"💱 **Exchange Rate**: 1 {from_curr} = {rate:.4f} {to_curr}\n"
            f"💰 **Converted Amount**: {amount} {from_curr} = {converted:.2f} {to_curr}"
        )
    else:
        return f"❌ Failed to fetch rate: {data.get('error-type', 'Unknown error')}"
