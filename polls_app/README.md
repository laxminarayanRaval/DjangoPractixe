# Polls App
### Learning Django Project step by step
___
#### 0. Install/ Update Python
___
#### 1. Installing Django
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
#### 2. Creating a project
   - cd into your project directory and then install django project
	
   ```$ django-admin startproject projectlx```
   - above code will return nothing on success
   - see what inside the *'projectlx'*

> projectlx/      # outer directory; root directory; container for project; name doesn't matter; rename if you want to

    | projectlx/     # actual python package for project; 
        | __init__.py	# every python package contains this empty file;
        | settings.py	# settings/ configurations for this project;
        | urls.py		# URL declarations for this project; aka 'table of content'; 
        | asgi.py		# entry point for ASGI-compatible web servers to serve proj.; Asynchronous Server Gateway Interface;
        | wsgi.py		# entry point for WSGI-compatible web servers to serve proj.; Web Server Gateway Interface;
    | manage.py		# command-line utility; interact with project; eg.: runserver
___
#### 3. Start The development server
   - cd into your project root directory
   - execute runserver command from manage.py
	
   ``` $ python3 manage.py runserver```
   
   - now visit http://127.0.0.1:8000/ ; this is production server; for deployment use apache
   - changing port numbers; use port number as argument
	
   ``` $ python manage.py runserver 8080```
   
   - if you want to change ip too send it as argument; 0 for 0.0.0.0
	
   ``` $ python manage.py runserver 0:8080```
   
   - production server reloads automatically; need to reload in case of adding file

___
#### 4. Creating the Polls app
   - Each application you write in Django consists of a Python package
   - An app is a web application that does something.;  An app can be in multiple projects.; Your apps can live anywhere on your Python path
   - A project is a collection of configuration and apps for a particular website.; A project can contain multiple apps
   - create poll app
	
   ``` $ python3 manage.py startapp polls```
   
   - this will return nothing on success
   
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
___
#### 5. Writing your first view
   - open the file 'polls/views.py' and put some code in it
   - now do some url mapping; make a new file 'urls.py'

___
#### 6. Setting up Database
   - open 'setting.py' of project package (here projectlx); It is a normal python module with module-level variables representing django settings.
   - for database by default configuration are for 'sqlite3'
   - if you wish to use anyother database, install the appropriate database bindings and change the following keys in the ```DATABASE```, ```'default'``` item \
      -- ```ENGINE``` - Either \
                  ```django.db.backends.sqlite3``` \
                  ```django.db.backends.postgresql``` \
                  ```django.db.backends.mysql``` \
                  ```django.db.backends.oracle``` or \
                  etc. \
      -- ```NAME``` - The name of your Database. If you are using sqlite, the database will be saved in project root directory.
   - run the command to create table database

   ```$ python3 manage.py migrate```

___
#### 7. Create Models
   - You can create any number of models in models directors's situated inside app
   - while making a Model you need to create a class for that model, which extends the ```models.Model```, which you need to import from ```django.db``` 
   - eg.: \
      class Question(models.Model): \
      ---- que_text = models.CharField(max_length=200) \
      ---- pub_date = models.DateTimeField('date published')

___
#### 8. Activating Models
   - first we need to tell our project that app in installed.
   - to include the app in our project, we need to add reference to its configuration class in the `INSTALLED_APPS` setting.
   - edit `INSTALLED_APPS` on settings.py inside project directory
   - add app's config (`PollsConfig`) class situated in 'apps.py' file in apps directory, so add the ```polls.apps.PollsConfig``` in the `INSTALLED_APPS` list 
   - now make migrations for our app
   
   ```$ python3 manage.py makemigrations polls```
   - newly generated migration lives inside 'migrations' directory named '0001_initail.py' 
   - now run `sqlmigrate` command from 'manage.py' with newly generaated migration name as argument

   ```$ python3 manage.py sqlmigrate 0001```
   - now migrate again, to create these model tables in database

___
### Introducing Django Admin
#### 9. Creating Superuser (Admin)
   - to create a superuser we need to run 'createsuperuser' command from 'manage.py' \
   ```$ python3 manage.py createsuperuser```
   > Username: admin \
   Email Address: admin@email.com \
   Password: ******* \
   Password (again): *******

   - with the help of above command we have created superuser or admin side login
   - now in your production server ``https://127.0.0.1:8000/admin`` login with above credentials
   - if we want to use 'Question objects' from admin interface.
   - register '`Question`' Model in 'admin.py' in app directory; reload admin side to see effects.

___
#### 10. Explore the free admin funcionality
   - here you can perform operations adding Question
   - editing and deleting existing Questions can be done, easyly

___
#### 11. Making New Views
   - Create new Views and pass question id to it; (detail, results, vote) new views
   - open 'views.py' in your app directory, and make three functions/ views \
      `syntax:- def view_name(request, *args): return HttpsResponse("sample text")`
   
___
#### 12. Making new Routes for above Views
   - now make new routes (detail, results, vote), for that open 'urls.py' of your app directory
      *( Make sure your app's 'urls.py' is linked to the package's 'urls.py')*
   - add path function with three parameters: \
      eg.: ``path('<int:que_id>/', views.details, name='detail')`` \
      *Parameter 1.* route or path, that is going to be accessed  \
      *Parameter 2.* view name. (function that you created in 'view.py') \
      *Parameter 3.* naming the route  

___
#### 13. Using Django's Template System
   - make a new directory name 'template' in your app directory
   - make another directory inside 'template/' same name as app directory
   - here in this directory put your all html pages
      eg.: ``app_directory/template/app_name_directory/*.html``
   - to render templates in views import loader/render from django.template/django.shortcuts respectively
   - sending some data in templates \
      I. using `loader` object's, methods `'get_template('path_for_template')'`\
           eg.:\
         ```template = loader.get_('polls/index.html').render({'data':"Some Data"}, request)``` \
         ```return HttpsResponse(template)``` \
      II. using `render()` shortcut helper \
           eg.: ```return render(request, 'polls/index.html', {'data': "Some Data"})```

___
### 14. Using Model for Retriving Data
   - import Models(eg. Question or Choice) from '.model'. To use them to get data.
   - Here you can use , 'Model.objects' query or django's shortcut method that accept model as first argument.
   - to use djangos shortcut method ('get_object_or_404()') you need to import it from django.shortcuts.

___
### 15. Removing hardcoded URLs in templates
   - here we use route names that we created earlier (ref.12. Parameter 3)
   - using url tag template; ``{% url 'route_name' %}``
   - add ``app_name = 'polls'`` in 'urls.py' of application directory.

___
### 16. Using Form in Django 
   - use django's url tag (ref.15. 1st point) in form's action
   - add csrf_token (cross-site request forgery token is used to prevent xss(cross-site site scripting)) eg.: ``{% csrf_token %}``
   - you can use 'forloop.counter' as counter variable eg.: ``{{ forloop.counter }}``
   - and you can use 'widthratio'; syntax: ``{% widthratio max min total %}`` it will be evaluated as (max * min / total)

___
### 17. Getting Forms Values in View
   - use 'request.POST' a dictionary like object eg.: ``request.POST['choice']``
   - always return '`HttpResponseRedirect(reverse())`', when dealing with POST method 
      - import HttpResponseRedirect from django.http 
      - import reverse from django.shortcut 
      - `reverse(P1, P2)` P1: template name (eg.: 'polls:results') and P2: data inside tuple as args  
      - eg.: ``reverse('polls:results', args=(data_id, data_name))`` 

___
### 18. Generic Views
   - we create genric views when we don't want to perform same operation of data retrivation, as we can see in our existing views
   - they are accepting que_id, for making database operation
   - this is very common web development practise 
      - getting data from DB according to a parameer passed in the urls, 
      - loading template and returning rendered template 
   - to make your views generic you need amend you 'views.py', use django's 'generic view' shortcuts
   - generic views abstract common patterns to the point where don't need to write code to make an app.
   - for that we need to perform some tasks 
      - Convert URLconf 
      - Delete old views, that we are going to make generic. 
      - Introduce new views based on django's generic views. 

___
### 19. Making Generic Views
   - Amend URLconf, via updating application 'urls.py'
      - change path string (route) parameter to 'pk'. before:'< int:que_id>' after:'< int:pk>'
      - ('DetailView' expects the primary key captured from URL to be called 'pk')
   - Amend Views, via updating applications 'views.py'
   - to make generic view follow these steps: 
      - import generic class from django.views 
      - make new classes for views. (Always PostFix 'View' eg.: ResultView) 
      - inherit generic class according to your requirements eg.: generic.ListView or generic.DetailView 
         - (We are using only two generic views here) 
         - ([ListView: Display List of Objects] and [DetailsView: Display a detail page for particular type of object]) 
      - change default settings of that view.
         - by default, DetailView uses a template called '< app name>/< model name>_detail.html'. we can set it using 'template_name' property 
         - by default, both generic views passes context object same as model name. for that we'll set 'context_object_name' property.
         - eg.:
         
           class IndexView(generic.ListView): \
                template_name = 'polls/detail.html' \
                context_object_name = 'latest_ques_list'