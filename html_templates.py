```python
from django.shortcuts import render

# This is the template for the product list view
def product_list(request):
    return render(request, 'product_catalog/product_list.html', {})

# This is the template for the product detail view
def product_detail(request, pk):
    return render(request, 'product_catalog/product_detail.html', {'pk': pk})

# This is the template for the product create view
def product_create(request):
    return render(request, 'product_catalog/product_form.html', {})

# This is the template for the product update view
def product_update(request, pk):
    return render(request, 'product_catalog/product_form.html', {'pk': pk})

# This is the template for the product delete view
def product_delete(request, pk):
    return render(request, 'product_catalog/product_confirm_delete.html', {'pk': pk})
```