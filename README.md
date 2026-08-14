# 🛒 PriceHunt - Wishlist Product Price Comparison Website

PriceHunt is a **Django-based product price comparison web application** that helps users search for products and compare prices across multiple e-commerce platforms from a single interface.

The application uses **SerpAPI** to retrieve product information from online shopping platforms and presents the results in an easy-to-use interface. Users can search for products, view available prices, compare sellers, and access the original product pages.

---

## 📌 Project Overview

Online shoppers often need to visit multiple e-commerce websites to compare prices for the same product. This process can be time-consuming and may cause users to miss better deals.

**PriceHunt** provides a centralized platform where users can search for products and view price information from multiple online stores.

### Main Features

* 🔐 User registration and login
* 🔎 Product search
* 💰 Price comparison
* 🏪 Multiple e-commerce sources
* 📊 Results sorted by price
* 🖼️ Product image display
* 🔗 Direct links to seller websites
* 📄 Pagination for search results
* 📱 Responsive web interface
* 🌐 SerpAPI integration
* 🐍 Django backend
* 💾 Local browser-based login state for the current academic implementation

---

## 🎯 Objectives

The main objectives of PriceHunt are:

1. Provide a centralized product price comparison platform.
2. Reduce the time required to compare prices across different stores.
3. Help users identify lower-priced products.
4. Retrieve product information automatically through an API.
5. Provide direct access to the original seller's website.
6. Create a foundation for future wishlist and price-alert functionality.

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │       User           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   PriceHunt Frontend │
                    │ HTML / CSS / JavaScript
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Django Backend    │
                    │      views.py        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  SerpAPI Service     │
                    │ Product Search API   │
                    └──────────┬───────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │     E-Commerce Search Data      │
              │ Amazon / Flipkart / Croma / etc │
              └───────────────┬─────────────────┘
                              │
                              ▼
                    ┌──────────────────────┐
                    │ Price Processing     │
                    │ & Sorting            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Search Results Page  │
                    └──────────────────────┘
```

---

## 🧰 Technology Stack

| Component                | Technology               |
| ------------------------ | ------------------------ |
| Frontend                 | HTML5, CSS3, JavaScript  |
| Backend                  | Python                   |
| Web Framework            | Django                   |
| Product Search           | SerpAPI                  |
| Data Processing          | Python                   |
| Price Extraction         | Custom Python utility    |
| Pagination               | Django Paginator         |
| Authentication Prototype | JavaScript Local Storage |
| Development OS           | Windows / Linux          |
| Version Control          | Git / GitHub             |

---

## 📁 Project Structure

```text
PriceHunt/
│
├── manage.py
│
├── pricehunt/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── scraper/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   ├── serpapi_service.py
│   ├── utils.py
│   │
│   └── templates/
│       └── scraper/
│           ├── index.html
│           ├── search.html
│           └── results.html
│
├── static/
│   └── images/
│       └── hero.jpg
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> The exact directory structure may vary depending on the final Django application configuration.

---

# ⚙️ Core Modules

## 1. User Authentication Module

The authentication interface allows users to register and log in before accessing the product search functionality.

### Functions

* User registration
* User login
* Login validation
* Logout
* Login-protected search access

> **Important:** The current academic implementation stores login information in browser `localStorage`. This is suitable only as a prototype. A production application should use Django's built-in authentication system with hashed passwords and server-side sessions.

---

## 2. Product Search Module

Users can enter a product name or keyword in the search interface.

Example:

```text
iPhone 17 Pro Max
Samsung Smart TV
Sony Headphones
Laptop
```

The search request is sent to the Django backend.

---

## 3. Price Comparison Module

The backend sends the product search request to SerpAPI and processes the returned product information.

The application can display:

* Product name
* Product price
* Product image
* Seller/source
* Product URL

Results are sorted according to the extracted product price.

Example:

```text
Search: iPhone

1. Apple iPhone 14     ₹59,999    Amazon
2. Apple iPhone 13     ₹52,999    Flipkart
```

---

## 4. SerpAPI Integration

PriceHunt uses **SerpAPI** to obtain product search information.

The basic flow is:

```text
User Search
     │
     ▼
Django View
     │
     ▼
SerpAPI Service
     │
     ▼
Product Search Results
     │
     ▼
Price Extraction
     │
     ▼
Price Sorting
     │
     ▼
Django Results Page
```

The API key should **never be hardcoded in source code or committed to GitHub**.

Use an environment variable:

```text
SERPAPI_KEY=your_api_key_here
```

Add `.env` to `.gitignore`:

```text
.env
```

If an API key has ever been accidentally pushed to a public repository, revoke or regenerate it. Secrets have a remarkable ability to escape into the internet and then become everyone else's problem.

---

# 🔍 Search and Result Processing

The Django backend follows this basic process:

```python
query = request.GET.get("query")
```

The query is passed to the SerpAPI service:

```python
results = search_products_serpapi(query)
```

Prices are extracted using the application's utility function:

```python
results = sorted(
    results,
    key=lambda x: extract_price(x.get("price"))
)
```

The results are then divided into pages using Django's paginator:

```python
paginator = Paginator(results, 5)
```

This allows the application to display five products per page.

---

# 🖥️ Application Pages

## Home Page

The home page introduces the PriceHunt application and provides navigation options for:

* About
* Login
* Register
* Start Searching

---

## Registration Page

New users can enter:

* Username
* Password

The prototype stores registration information in browser local storage.

---

## Login Page

Registered users can enter their credentials to access the search page.

Successful authentication redirects the user to:

```text
/search/
```

---

## Search Page

The search page provides a search box where users can enter product keywords.

Example:

```text
Search iPhone, Samsung TV, Sony Headphones...
```

---

## Search Results Page

The results page displays:

* Product title
* Price
* Product image
* Seller/source
* View Product button
* Pagination

Users can click **View on Seller** to open the original product listing.

---

# 🧪 Testing

The application can be tested using multiple testing approaches.

### Unit Testing

Individual functions and components are tested independently.

Examples:

* Price extraction
* API service
* Search processing
* Pagination

### Integration Testing

Tests communication between:

```text
Django → SerpAPI → Result Processing → Results Page
```

### Functional Testing

Tests complete user functionality:

* Registration
* Login
* Search
* Product result display
* Seller links
* Pagination
* Logout

### System Testing

Tests the complete application as an integrated system.

### Black Box Testing

The application is tested through inputs and outputs without considering its internal implementation.

### Acceptance Testing

The final application is checked against the required project functionality and expected user experience.

---

# 🚀 Installation

## Prerequisites

Install the following software:

* Python 3.10+
* pip
* Git
* Django
* SerpAPI account/API key

Check Python:

```bash
python --version
```

Check pip:

```bash
pip --version
```

---

# 📥 Clone the Repository

```bash
git clone https://github.com/your-username/pricehunt.git
```

Move into the project:

```bash
cd pricehunt
```

---

# 🐍 Create Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate:

```powershell
.\venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django requests python-dotenv
```

---

# 🔐 Configure Environment Variables

Create a `.env` file in the project root:

```text
SERPAPI_KEY=your_serpapi_key
```

Example Django configuration:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
```

Do not commit `.env`.

---

# 🗄️ Run Django Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# ▶️ Start the Development Server

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

---

# 🔎 Using the Application

### Step 1

Open the application in a browser.

### Step 2

Register a user account.

### Step 3

Login.

### Step 4

Enter a product name.

Example:

```text
iPhone 17 Pro Max
```

### Step 5

Click **Search**.

### Step 6

Review the returned products and prices.

### Step 7

Click the seller link to view the product on the original e-commerce platform.

---

# 📊 Example Workflow

```text
             START
                │
                ▼
          Open PriceHunt
                │
                ▼
          User Registration
                │
                ▼
              Login
                │
                ▼
         Enter Product Name
                │
                ▼
        Send Search Request
                │
                ▼
         Django Backend
                │
                ▼
             SerpAPI
                │
                ▼
       Retrieve Product Data
                │
                ▼
        Extract Product Price
                │
                ▼
          Sort by Price
                │
                ▼
        Display Search Results
                │
                ▼
       Open Seller Product Page
                │
                ▼
               END
```

---

# 🔒 Security Considerations

The current implementation is an academic prototype. For production deployment, the following improvements are recommended:

* Use Django authentication instead of browser `localStorage`.
* Hash passwords using Django's authentication framework.
* Store API keys in environment variables.
* Never commit secrets to Git.
* Configure Django `SECRET_KEY` through environment variables.
* Disable `DEBUG` in production.
* Configure `ALLOWED_HOSTS`.
* Enable HTTPS.
* Implement CSRF protection.
* Validate and sanitize user input.
* Apply API rate limiting.
* Secure external API requests.
* Implement proper database access controls.

---

# 📈 Future Enhancements

The project can be extended with the following features.

## Wishlist Management

Users can:

* Add products to a wishlist.
* Remove products.
* Manage multiple wishlist items.
* Track product prices.

## Price Drop Alerts

Users can configure a target price.

Example:

```text
Current Price: ₹65,000
Target Price:  ₹55,000
```

When the price reaches the target, the system can notify the user.

---

## Price History

Store historical prices and display them using graphs.

Example:

```text
Date          Price
--------------------
01-Aug-2026   ₹70,000
05-Aug-2026   ₹68,000
10-Aug-2026   ₹64,000
14-Aug-2026   ₹61,000
```

---

## AI-Based Recommendations

Machine learning can be introduced to recommend:

* Similar products
* Alternative products
* Frequently viewed products
* Personalized deals
* Best products based on user preferences

---

## Price Prediction

Historical price information can be used to build models that estimate possible future price movements.

Potential use:

```text
Current Price: ₹60,000

Predicted Trend:
Price may decrease during the upcoming sale period.
```

---

## Mobile Application

The system can be extended into:

* Android application
* iOS application

Features could include:

* Push notifications
* Wishlist synchronization
* Price-drop alerts
* Mobile authentication

---

## More E-Commerce Platforms

Future versions can integrate additional shopping platforms and data providers.

The architecture can be designed so that each external source is handled through a separate service or API adapter.

---

# 📚 Project Advantages

* Saves users' time.
* Simplifies price comparison.
* Provides centralized product information.
* Helps users identify better deals.
* Reduces the need to manually visit multiple websites.
* Provides direct access to seller pages.
* Can be extended with price tracking and notifications.
* Provides a foundation for intelligent shopping recommendations.

---

# ⚠️ Current Project Limitations

The current academic implementation has some limitations:

1. The wishlist functionality described in the project report is not fully represented in the supplied Django code.
2. Price-drop notifications are proposed as a future enhancement.
3. Authentication currently uses browser `localStorage` rather than Django's server-side authentication.
4. Product information depends on the availability and structure of the external API.
5. API usage may be subject to SerpAPI limits and pricing.
6. Product prices can change after the search result is retrieved.
7. The application is primarily intended as an academic prototype rather than a production-scale shopping platform.

Being explicit about limitations is preferable to claiming the application has features that exist only in Chapter 9 of a report written at 2 a.m.

---

# 🎓 Academic Project

**Project Title:**
**WISHLIST PRODUCT PRICE COMPARISON WEBSITE**

**Application Name:**
**PriceHunt**

**Student:**
**MASUNURI BAVAJAN**

**Registration Number:**
**24F6F00001**

**Degree:**
Master of Computer Applications (MCA)

**Academic Year:**
2025–2026

**Institution:**
Siddharth Institute of Engineering & Technology (Autonomous)

**Department:**
Department of Master of Computer Applications

**University:**
JNTUA, Ananthapuramu

---

# 📜 License

This project was developed for academic and educational purposes.

If reused or modified, appropriate credit should be given to the original project author.

---

# 👨‍💻 Author

**MASUNURI BAVAJAN**

MCA Student
Siddharth Institute of Engineering & Technology

---

## ⭐ Project Summary

PriceHunt demonstrates how **Django, Python, HTML, CSS, JavaScript, and external product-search APIs** can be integrated to build a practical price comparison platform.

The project provides a foundation for developing a more advanced shopping assistant with **wishlist management, historical price tracking, price-drop notifications, recommendation systems, analytics, and mobile support**.

http://127.0.0.1:8000/about/
