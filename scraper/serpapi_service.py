import requests
from requests.exceptions import RequestException, Timeout

SERPAPI_KEY = "677c7f95d847727a7ce3ddc74c04e456d173c62d2121ca33bb4ba348307f8ff7"


def search_products_serpapi(query):
    url = "https://serpapi.com/search"

    params = {
        "engine": "google_shopping",
        "q": query,
        "hl": "en",
        "gl": "in",
        "api_key": SERPAPI_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except (Timeout, RequestException) as e:
        print("SerpAPI error:", e)
        return []

    data = response.json()
    results = []

    for item in data.get("shopping_results", []):
        results.append({
            "title": item.get("title"),
            "price": item.get("price"),
            "url": item.get("product_link") or item.get("link"),
            "image": item.get("thumbnail"),
            "source": item.get("source", "Google Shopping")
        })

    return results
