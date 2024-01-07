# Django Tutorial

## Why Django?
* Django is a `rapid` web development framework for python.
* Django is said to be `batteries included` framework because it's a fully functional framework and need nothing else.
* Django makes it `easy to switch` from one database to another.
* Django has `built-in admin interface`.

## Django Architecture
* Django is based on `Model View Template (MVT) Architecture`. MVT has three components: **Model**, **View** and **Template**.

### Model
* The **Model** is your `Logical Data Structure` behind the entire application and is generally represented by the **Database**.
* The **Model** is responsible for maintaining your data and acts an interface to the data.

### View
* The **View** is what you see in your browser when you render the website. It is represented by HTML/CSS/Javascript and Jinja files. 
* The **View** executes the `business logic` and `interacts with the model` to carry data and renders the template.

### Template
* The **Template** consists of static parts of the desired HTML output as well as `some special syntax` describing how dynamic content will be inserted. 
* The **Template** handles the layout and structure of the user-facing application.

## Create Django Project
### `django-admin startproject WorldTour`
* This command creates your starter project named `WorldTour` in the `present working directory (pwd)` and `manage.py` module.

 `manage.py`: This is a command-line utility that lets you interact with your Django project in various ways. It's a command center for your project and performs the function of `django-admin` like: it can **run the server, make migrations, handle exceptions**, and more.

- `Europe/`: This is the actual Python package for your project. It's a lower-level folder that represents your management app. It contains the following files:

    - `__init__.py`: This empty file tells Python that this directory should be considered a Python package.

    - `settings.py`: This file contains all the `configuration` of your Django installation. This is where you’d put all the settings that are specific to this particular Django instance.

    - `urls.py`: This file is responsible for **mapping** the routes and paths in your app to the associated view functions.

    - `asgi.py` or `wsgi.py`: These files serve as an **entry-point** for WSGI-compatible web servers to serve your project.

This structure helps in better organization of your code, especially for large projects⁴. It's important to understand this structure as it gives you a clear view of where you should be writing your code.

## Create Django Project

### Create Main Project
* `django-admin startproject WorldTour`: This command is used to create a new Django project named WorldTour. A project represents the whole application and is a collection of settings for an instance of Django, including database configuration, Django-specific options, and application-specific settings.

### Create Sub-Project
* `python manage.py startapp Europe`: This command is used to create a new Django application named Europe within an existing Django project. An application is a module within a project that does something. An application encapsulates a specific functionality of the project.

### Run Django Project
* `python3 manage.py runserver`: starts a lightweight web server on your local machine @ [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

