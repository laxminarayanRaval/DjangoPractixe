# DjangoPractixe
Practising Django Web Framework ( Python ) ... 
---
## Learning Django step by step

___
0. Install/ Update Python

___
1. Installing Django
   - install/ upgrade pip 
   
   ``` $ python3 -m pip install --upgrade pip```
   
   - make venv and activate it
	
   ``` $ python3 -m venv .venv```
	
   ``` $ source .venv/bin/activate```
   
   - install Django
	
   ``` $ python3 -m pip install Django```
   
   - verify installation
	
   ``` $ python3 -m django --version```

___
2. Creating a project
   - cd into your project directory and then install django project
	
   ```$ django-admin startproject projectlx```
   - above code will return nothing on success
   - see what inside the *'projectlx'*

--------------------------------
> projectlx/      # outer directory; root directory; container for project; name doesn't matter; rename if you want to

    | projectlx/     # actual python package for project; 
        | __init__.py	# every python package contains this empty file;
        | settings.py	# settings/ configurations for this project;
        | urls.py		# URL declarations for this project; aka 'table of content'; 
        | asgi.py		# entry point for ASGI-compatible web servers to serve proj.; Asynchronous Server Gateway Interface;
        | wsgi.py		# entry point for WSGI-compatible web servers to serve proj.; Web Server Gateway Interface;
    | manage.py		# command-line utility; interact with project; eg.: runserver
---------------------------------

___
3. Start The development server
   - cd into your project root directory
   - execute runserver command from manage.py
	
   ``` $ python3 manage.py runserver```
   
   - now visit http://127.0.0.1:8000/ ; this is production server; for deployment use apache
   - changing port numbers; use port number as argument
	
   ``` $ python manage.py runserver 8080```
   
   - if you want to change ip too send it as argument; 0 for 0.0.0.0
	
   ``` $ python manage.py runserver 0:8080```
   
   - production server reloads automatically; need to reload in case of adding file

---
4. Creating the Polls app
   - Each application you write in Django consists of a Python package
   - An app is a web application that does something.;  An app can be in multiple projects.; Your apps can live anywhere on your Python path
   - A project is a collection of configuration and apps for a particular website.; A project can contain multiple apps
   - create poll app
	
   ``` $ python3 manage.py startapp polls```
   
   - this will return nothing on success
--------------------------------
> projectlx/		# root directory;

    | polls/			# app directory;
    	| __init__.py
    	| admin.py
    	| apps.py
    	| migrations/
            | __init__.py
    	| models.py
    	| tests.py
    	| views.py
--------------------------------

---
5. Writing your first view
   - open the file 'polls/views.py' and put some code in it
   - now do some url mapping; make a new file 'urls.py'
