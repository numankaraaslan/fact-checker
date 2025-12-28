from tavily import TavilyClient
import os

client = TavilyClient("tvly-dev-xxx")

def tavily_search(query: str):
    response = client.search(query=query, search_depth="basic")
    return response.get("results", [])

