```python
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Database details
database_name = "product_catalog_db"
user = "postgres"
password = "password"

# Connect to PostgreSQL server
conn = psycopg2.connect(dbname="postgres", user=user, password=password)

# Create new database
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name)))
cur.close()
conn.close()

# Configure Django to use the new database
with open("django_project_setup.py", "a") as file:
    file.write("\n")
    file.write("DATABASES = {\n")
    file.write("    'default': {\n")
    file.write("        'ENGINE': 'django.db.backends.postgresql',\n")
    file.write(f"        'NAME': '{database_name}',\n")
    file.write(f"        'USER': '{user}',\n")
    file.write(f"        'PASSWORD': '{password}',\n")
    file.write("        'HOST': 'localhost',\n")
    file.write("        'PORT': '',\n")
    file.write("    }\n")
    file.write("}\n")
```