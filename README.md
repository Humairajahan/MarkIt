# MarkIt : Attendance Management System

MarkIt is an attendance management project with the goal to simplify and automate the process of tracking and managing attendance in various settings. 

This branch is dedicated towards building the system with the following : 

🌐 `Django web framework`

🗄️ `Django cache framework` for caching

📝 `PostgreSQL` for database.   

### This project is ⚠️ **Under Construction** ⚠️ right now.

## Run in local setup
1. Clone the branch `dev-django` of this repository.
```python
git clone -b dev-django https://github.com/Humairajahan/MarkIt.git
```

2. Create a virtual environment and activate the environment.

```python
python -m venv <ENV>
source <ENV>/bin/activate
```
This should do it! 

You can get out of the virtual environment by simply deactivating it.
```python
deactivate
``` 

3. Install the requirements.
```python
pip install -r requirements.txt
```

<!-- 4. Follow through this step in case you want to create a new django project.
```python
django-admin startproject <PROJECT>
```

5. Now run the whole django application.
```python
# Run our django application
python backend_server/manage.py runserver

# Run your own django application
python <PROJECT>/manage.py runserver
```

6. You can create new applications under the hood of the django project you just created.
```python
python backend_server/manage.py startapp routers
``` -->

4. Now run our django application in your setup.

```python
python backend_server/manage.py runserver
```

## Run in `docker`
**COMING SOON!!!** 