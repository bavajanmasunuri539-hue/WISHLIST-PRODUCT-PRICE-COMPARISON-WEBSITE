import re

def extract_price(price_str):
    """
    Converts '₹79,999' → 79999
    """
    if not price_str:
        return float('inf')

    digits = re.sub(r'[^\d]', '', price_str)
    return int(digits) if digits else float('inf')
