```python
import os
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    # Check Python version
    print("Python version")
    print (sys.version)
    print("Version info.")
    print (sys.version_info)

    # Install Django
    print("Installing Django...")
    install('Django')

    # Install psycopg2 for PostgreSQL
    print("Installing psycopg2 for PostgreSQL...")
    install('psycopg2-binary')

    # Install Streamlit
    print("Installing Streamlit...")
    install('streamlit')

if __name__ == "__main__":
    main()
```