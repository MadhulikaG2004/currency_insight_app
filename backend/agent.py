from backend.graph.currency_graph import create_graph

graph = create_graph()

def exchange_agent(pair):
    result = graph.invoke({"pair": pair})
    return result
