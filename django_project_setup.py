```python
import os
import subprocess

def create_django_project(project_name):
    try:
        # Create a new Django project
        subprocess.check_call([os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dev_env_setup.py')])

        # Navigate to the directory where you want to create your project
        os.chdir("/path/to/your/directory")

        # Create the Django project
        subprocess.check_call(['django-admin', 'startproject', project_name])

        print(f"Django project '{project_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the Django project: {str(e)}")

if __name__ == "__main__":
    create_django_project("your_project_name")
```