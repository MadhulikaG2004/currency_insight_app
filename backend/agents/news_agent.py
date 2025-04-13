from langchain_core.runnables import RunnableLambda
from backend.tools.news_tool import get_news

news_agent = RunnableLambda(lambda inputs: {"news": get_news(inputs["pair"])})
