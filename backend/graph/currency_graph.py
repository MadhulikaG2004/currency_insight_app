from langgraph.graph import StateGraph, END
from backend.agents.currency_agent import currency_agent
from backend.agents.news_agent import news_agent
from typing import TypedDict
class CurrencyState(TypedDict):
    pair: str
    rate: str
    news: str

# 🔹 Entry Node: Prepares state
def entry_node(input):
    return {
        "pair": input  # e.g. "USD/INR"
    }

# 🔹 Merge Node: Combines outputs
def merge_results(state):
    rate = state.get("rate")
    news = state.get("news")
    return {
        "output": f"### 💹 Currency Rate\n{rate}\n\n### 📰 Related News\n{news}"
    }

def create_graph():
    graph = StateGraph(CurrencyState)

    # 1️⃣ Add all nodes
    graph.add_node("Entry", entry_node)
    graph.add_node("CurrencyAgent", currency_agent)
    graph.add_node("NewsAgent", news_agent)
    graph.add_node("Merge", merge_results)

    # 2️⃣ Set edges
    graph.set_entry_point("Entry")
    graph.add_edge("Entry", "CurrencyAgent")
    graph.add_edge("Entry", "NewsAgent")

    graph.add_edge("CurrencyAgent", "Merge")
    graph.add_edge("NewsAgent", "Merge")

    graph.set_finish_point("Merge")

    return graph.compile()
