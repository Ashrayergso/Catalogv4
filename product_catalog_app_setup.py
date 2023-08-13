```python
# Import necessary modules
import os
import django

# Set the environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project_name.settings')

# Start Django
django.setup()

# Import necessary modules
from django.core.management import call_command

# Create a new Django app
call_command('startapp', 'product_catalog_app')

# Print success message
print("Product Catalog App has been successfully created.")
```