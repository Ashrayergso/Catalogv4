```python
import streamlit as st
import requests
import json

# Django backend URL
DJANGO_BACKEND_URL = "http://localhost:8000"

def get_products():
    response = requests.get(f"{DJANGO_BACKEND_URL}/products/")
    return response.json()

def display_product_details(product_id):
    response = requests.get(f"{DJANGO_BACKEND_URL}/products/{product_id}/")
    return response.json()

def main():
    st.title("Product Catalog")

    products = get_products()

    for product in products:
        st.subheader(product['name'])
        st.text(product['description'])
        st.text(f"Price: {product['price']}")
        if st.button('View Details'):
            details = display_product_details(product['id'])
            st.text(details)

if __name__ == "__main__":
    main()
```