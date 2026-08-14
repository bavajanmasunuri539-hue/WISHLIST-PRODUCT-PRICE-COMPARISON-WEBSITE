import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-IN,en;q=0.9"
}

def scrape_flipkart(query):
    products = []
    url = f"https://www.flipkart.com/search?q={query}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
    except RequestException as e:
        print("Flipkart error:", e)
        return products   # 👈 SAFE FAIL

    soup = BeautifulSoup(response.text, "lxml")
    items = soup.find_all("div", class_="_1AtVbE")

    for item in items:
        title = item.find("div", class_="_4rR01T")
        price = item.find("div", class_="_30jeq3")
        link = item.find("a", class_="_1fQZEK")

        if title and price and link:
            products.append({
                "title": title.text.strip(),
                "price": price.text.strip(),
                "url": "https://www.flipkart.com" + link.get("href"),
                "source": "Flipkart"
            })



def scrape_amazon(query):
    products = []
    url = f"https://www.amazon.in/s?k={query}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        "Accept-Language": "en-IN,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
    except Exception as e:
        print("Amazon error:", e)
        return products   # SAFE FAIL

    soup = BeautifulSoup(response.text, "lxml")
    items = soup.select('div[data-component-type="s-search-result"]')

    for item in items:
        title = item.select_one("h2 a span")
        price_whole = item.select_one("span.a-price-whole")
        link = item.select_one("h2 a")

        if title and price_whole and link:
            products.append({
                "title": title.text.strip(),
                "price": "₹" + price_whole.text.replace(",", "").strip(),
                "url": "https://www.amazon.in" + link.get("href"),
                "source": "Amazon"
            })


def scrape_croma(query):
    products = []
    url = f"https://www.croma.com/search/?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-IN,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
    except Exception as e:
        print("Croma error:", e)
        return products

    soup = BeautifulSoup(response.text, "lxml")
    items = soup.find_all("div", class_="cp-product")

    for item in items:
        title = item.find("h3", class_="product-title")
        price = item.find("span", class_="amount")
        link = item.find("a", class_="product__list--name")

        if title and price and link:
            products.append({
                "title": title.text.strip(),
                "price": "₹" + price.text.replace(",", "").strip(),
                "url": "https://www.croma.com" + link.get("href"),
                "source": "Croma"
            })


def scrape_reliance(query):
    products = []
    url = f"https://www.reliancedigital.in/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-IN,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
    except Exception as e:
        print("Reliance error:", e)
        return products

    soup = BeautifulSoup(response.text, "lxml")
    items = soup.find_all("div", class_="sp grid")

    for item in items:
        title = item.find("p", class_="__productTitle")
        price = item.find("span", class_="TextWeb__Text")
        link = item.find("a", class_="__productLink")

        if title and price and link:
            products.append({
                "title": title.text.strip(),
                "price": price.text.strip(),
                "url": "https://www.reliancedigital.in" + link.get("href"),
                "source": "Reliance Digital"
            })

    return products


    return products