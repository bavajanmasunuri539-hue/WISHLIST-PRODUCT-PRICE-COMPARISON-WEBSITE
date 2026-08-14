from django.shortcuts import render
from django.core.paginator import Paginator

from .serpapi_service import search_products_serpapi
from .utils import extract_price


def index(request):
    return render(request, "scraper/index.html")


def home(request):
    query = request.GET.get("query")

    if not query:
        return render(request, "scraper/search.html")

    try:
        results = search_products_serpapi(query)
    except Exception as e:
        print("API failed:", e)
        results = []

    if not results:
        results = [
            {
                "title": "Apple iPhone 14",
                "price": "₹59,999",
                "url": "#",
                "source": "Amazon"
            },
            {
                "title": "Apple iPhone 13",
                "price": "₹52,999",
                "url": "#",
                "source": "Flipkart"
            }
        ]

    results = sorted(results, key=lambda x: extract_price(x.get("price")))

    paginator = Paginator(results, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "scraper/results.html", {
        "query": query,
        "page_obj": page_obj
    })
