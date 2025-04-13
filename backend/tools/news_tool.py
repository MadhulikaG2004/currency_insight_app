import os
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper

load_dotenv()

def get_news(pair: dict) -> str:
    try:
        currencies = pair.get("pair").split("/")
        query = f"{currencies[0]} {currencies[1]} currency exchange latest news"
    except Exception:
        return "❌ Invalid currency pair format."

    search = GoogleSerperAPIWrapper(serper_api_key=os.getenv("SERPER_API_KEY"))
    results = search.results(query)

    articles = results.get("organic", [])
    if not articles:
        return "❌ No news found for this currency pair."

    formatted_news = "📰 **Top Currency News Headlines:**\n\n"
    for i, article in enumerate(articles[:5], start=1):  
        title = article.get("title", "No Title")
        link = article.get("link", "#")
        snippet = article.get("snippet", "No description available.")

        formatted_news += (
            f"**{i}. [{title}]({link})**\n"
            f"{snippet}\n\n"
        )

    return formatted_news