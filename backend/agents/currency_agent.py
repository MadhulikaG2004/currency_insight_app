from langchain_core.runnables import RunnableLambda
from backend.tools.currency_tool import get_exchange_rate

currency_agent = RunnableLambda(lambda inputs: {"rate": get_exchange_rate(inputs["pair"])})
