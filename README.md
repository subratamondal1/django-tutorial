<h1 align="center">Django Tutorial</h1>
<p align="center">
  <img src="https://img.shields.io/badge/python-3.11.0-blue" alt="python@3.11.0">
  <img src="https://img.shields.io/badge/pip-23.3.2-moccasin" alt="pip@23.3.2">
  <img src="https://img.shields.io/badge/poetry-1.7.1-orange" alt="poetry@1.7.1">
  <img src="https://img.shields.io/badge/django-5.1-papayawhip" alt="django@5.1">
</p>

<h1 align="left">Introduction</h1>
<h2 align="left">Why Django?</h2>

- Free and Open Source Framework for Web Development
- Fast
- Feature-Rich
- Secure
- Scalable
- Batteries Included Web Framework. **Why?** Because it provides lot of futures out of the box so that we don't have to code them from scratch, such as
  - Admin Site
  - ORM - Object Relational Mapper
  - Authentication
  - Caching

**Note** Django comes with a lot of features but you don't have to use them all, use it to your convenience.

<h2 align="left">Frontend & Backend</h2>
Every web app has two main parts (apps) - Frontend & Backend.

- **Frontend** is the part (app) that is loaded in the browser on the **client** side. It's the part that the user sees and interacts with.
- **Backend** is the part (app) that is loaded on the **web server**. It's the part that is responsible for data processing, validating business rules and others.

- **URL - Uniform Resource Locator** is a way to locate resources on the internet. Resources can be a web page, image, audio, video, pdf and others.

- **HTTP - Hypertext Transfer Protocol** is a Request-Response protocol, it defines how a client and a server can communicate with each other on the internet.

- **API - Application Programming Interface** Server is a gateway to the data for the Client, the Server provides an API through which the Client interacts with the Server.

<h2 align="left">Client-Server Model</h2>

- **Client** is a program that runs on the local machine requesting service from the server. A client program is a finite program that starts and terminates when the service is completed.

  - Next
  - React
  - Angular
  - Vue

- **Server** is a program that runs on the remote machine providing services to the clients. A server program is an infinite program that runs all the time and waits for the incoming requests from the clients.
  - Django
  - Express
  - Node
  - Asp.net

Some of the advantages of the Client-Server Model are:

- **Centralized**: All the data is stored in a single place, which makes it easier to back up, secure, and maintain.

- **Performance**: The use of a dedicated server increases the speed of sharing resources and reduces the network congestion.

- **Scalability**: The capacity of the client and server can be changed separately, and new elements can be added to the network at any time.

Some of the disadvantages of the Client-Server Model are:

- **Vulnerability**: Clients and servers are prone to various attacks, such as viruses, Trojans, worms, denial of service, phishing, spoofing, and man-in-the-middle.

- **Dependency**: Clients depend on the availability and functionality of the server. If the server is down or overloaded, the client requests cannot be met.

- **Cost**: Servers require high-end hardware and software, which can be expensive to purchase and maintain.

<h2 align="left">3-Tier Architecture</h2>

The 3-Tier Architecture is a software design pattern that divides an application into three logical and physical layers: the presentation tier, the application tier, and the data tier. Each layer has its own responsibilities and communicates with the other layers through well-defined interfaces.

- The **presentation tier** is the user interface layer that displays information to and collects input from the user. It can be a web browser, a desktop application, or a mobile app. The presentation tier communicates with the application tier through HTTP requests or other protocols.

- The **application tier** is the logic layer that processes data and implements the business rules of the application. It can be written in any programming language, such as Python, Java, or PHP. The application tier communicates with the data tier through APIs or database queries.

- The **data tier** is the storage layer that manages the data associated with the application. It can be a relational database, a NoSQL database, or a file system. The data tier stores and retrieves data for the application tier.

The benefits of the 3-Tier Architecture are:

- **Scalability:** The architecture allows each layer to be scaled independently to meet the demand of the application.

- **Flexibility:** The architecture allows each layer to be replaced or upgraded without affecting the other layers. For example, the presentation tier can use different frameworks or technologies, such as React or Angular, while the application tier and the data tier remain unchanged.

- **Reusability:** The architecture allows each layer to be reused across different applications. For example, the application tier can provide APIs for multiple presentation tiers, or the data tier can serve multiple application tiers.

<h1 align="left">Fundamentals</h1>

<h2 align="left">Django-admin</h2>

`django-admin` is a command-line tool that helps you manage your Django projects. It also provides a web interface for data administration, called the Django admin site.

Some of the tasks that you can perform with django-admin are:

- Create and configure a new Django project and its apps.
- Run the development server and test your application locally.
- Create and apply database migrations to update the data schema.
- Create a superuser account and access the admin site.
- Customize the admin site to suit your needs and preferences.
- Test your application with unit tests and report errors or failures.
- Deploy your application and collect static files for web serving.

Django-admin is a powerful and versatile tool that simplifies the development and administration of Django projects.

<h2 align="left">Create Django Project</h2>

```bash
django-admin startproject project_name .

# Example
django-admin startproject instagram .
```

**Note** The `.` at the end tells django-admin to use the current directory as the project directory.

When you run the above command inside "instagram" folder, we get:

```bash
├── instagram
│   ├── instagram        # core of our application
│   │   ├── __init__.py  # defines this directory as package
│   │   ├── asgi.py      # related to deployment
│   │   ├── settings.py  # define our application settings
│   │   ├── urls.py      # define the urls of our application
│   │   └── wsgi.py      # related to deployment
│   └── manage.py    # wrapper around django-admin
```

<h2 align="left">Django Project vs Django App</h2>

- Django project is the entire web app, e.g Instagram.
- Django apps are sub modules inside the django project that represents multiple features of the web app, e.g Instagram Posts, Status, Story, Reels, etc.

<h2 align="left">Create Django App</h2>

```bash
python -m django startapp app_name

# Example
python -m django startapp reels
```

<h2 align="left">django-admin vs manage.py</h2>

Both are **command line utility**. When we run the bellow command separately, we get the same result.

```bash
1. django-admin
2. python manage.py
```

- But there's a subtle difference the django-admin and manage.py.

`manage.py` takes in-account of the settings of the project, whereas, `dajngo-admin` doesn't, that's the reason the following command will throw error:

```bash
django-admin runserver
```

whereas, the following command will run successfully:

```bash
python manage.py runserver
```

```bash
python manage.py startapp app_name

# Example
python manage.py startapp reels
```

```bash
.
├── instagram
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── reels
    ├── __init__.py
    ├── admin.py   # Here we configure our admin interface of the app
    ├── apps.py    # Here we configure our app
    ├── migrations # For generating database tables of our app
    │   └── __init__.py
    ├── models.py  # Here we define model classes for our app, model classes pull out data from the database and present to the user
    ├── tests.py # Here we write our unittest for our app
    └── views.py # It's a Request Handler and not related to html, template or frontend
```

**Note:** everytime you create an app, you need to define it in the `settings.py` of the django-project in the `INSTALLED_APPS` variable list.

<h2 align="left">Django Views</h2>

The views function is responsible for the logic, or the business rules, of the application. It takes a request from the user and returns a response, usually a web page rendered with a template.

- We know that **HTTP** is a **Request-Response** Protocol. So, every data exchange involves Request-Response. This is where we use views in Django.

In the `views.py` module of our app we define our `views` (action) or `view funtion` that takes in `Request` and returns `Response`, hence called **Request Handler**. We can define our view functions to:

- pull data from db.
- transform data.
- send emails

**Note:** we need to map our view in the `urls.py` module so whenever the url is used the user gets the result retuned by the views.

<h2 align="left">Map URLS to Views</h2>

First create `urls.py` module inside your project-app, it should look like this:

```python
"""Map Urls to the View Functions"""
from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    path('hello/', views.say_hello) # new url
]
```

Then modify the `urls.py` module of the project, it should be something like this:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')) # new url
]
```

The final url would be `.../playground/hello/`

<h2 align="left">Rendering Template</h2>

Although we can render template using DTL - Django Template Language but we use Django mostly to built API that sent data and not HTML.

<h2 align="left">Data Model</h2>

A data model in Django is a way of defining the structure and behavior of the data that you want to store in a database. A data model is represented by a `Python class` that inherits from `django.db.models.Model`. Each attribute of the class corresponds to a field in the database table, and each instance of the class represents a row in the table.

- **Models** are used to **store** and **retrieve** data.
- Each **django-project** has multiple apps that represents different functionalities and each of those apps has their own Data Model.

* Make sure that each app is **self-contained** i.e they are not dependend on others.

* A good design is one with **minimal coupling (dependency)** and
  **high cohesion (focus)**.

<h2 align="left">Django Model Field types</h2>

- Django model field types are the classes that define the structure and behavior of the data that you want to store in a database using Django.

- Each field type corresponds to a column type in the database, and each attribute of the field class represents an option or constraint for the column.

- For example, a CharField is a field type that stores text-based values, and it has attributes like max_length, blank, and choices that affect how the text is stored and validated.

* There are many field types available in Django, such as **IntegerField, BooleanField, DateField, ForeignKey**, and **FileField**.

* Each field type has its own set of arguments, methods, and properties that you can use to customize its functionality.

* You can also create your own custom field types by subclassing the Field class or any of its subclasses.

```python
from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
```

- **Note:** By default Django creates an **Id Key** that acts as **Primary Key** for each Data Model Class until and unless you create an attribute in the Data Model Class with argument `primary_key=True`.

* After migrations this class model, in our database: class **Product** becomes the **Table name** and all the **attributes** become the **Column name** and the arguments as **Column Constraints**.

<h2 align="left">Django Choice Fields</h2>

Choice Fields in Django are a way of defining a list of available options for a model field or a form field. They are useful for fields that have a limited set of valid values, such as gender, status, category, etc. They are also helpful for displaying human-readable names for the values, instead of using the raw values in the database or the user interface.

To use Choice Fields in Django, you need to provide a mapping or an iterable of two-item tuples, where the first item is the actual value to be stored in the database, and the second item is the human-readable name to be displayed. For example:

```python
GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
)

gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
```

This will create a model field called gender, which can only store one of the three values: "M", "F", or "O". It will also use a select box as the default form widget, with the options "Male", "Female", and "Other" for the user to choose from.

You can also use variables or constants to define the choices, instead of hard-coding the values. This can help you avoid errors and improve readability. For example:

```python
MALE = "M"
FEMALE = "F"
OTHER = "O"

GENDER_CHOICES = (
    (MALE, "Male"),
    (FEMALE, "Female"),
    (OTHER, "Other"),
)

gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
```

This will have the same effect as the previous example, but it will allow you to use the variables MALE, FEMALE, and OTHER in your code, instead of the strings "M", "F", and "O".

<h2 align="left">Django One to One Realtionship between Model Classes</h2>

A Django `OneToOneField` is a field type that creates a one-to-one relationship between two models. A one-to-one relationship means that each record in one model is linked to exactly one record in another model. For example, each user has one profile and each profile belongs to one user.

To use a OneToOneField, you need to specify the `name` of the related model and the `on_delete` option, which defines what happens when the related record is deleted. For example:

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

In this example, the Profile model has a user field that references the User model using a OneToOneField. The `on_delete=models.CASCADE` option means that if a User object is deleted, the Profile object associated with it will also be deleted automatically.

You can access the related object using the dot notation. For example, you can get the user's name from the profile object like this:

```python
profile = Profile.objects.get(id=1)
user_name = profile.user.name
```

You can also access the profile object from the user object using the lowercased model name. For example, you can get the user's bio from the user object like this:

```python
user = User.objects.get(id=1)
user_bio = user.profile.bio
```

<h2 align="left">Django One to Many Realtionship between Model Classes</h2>

A one to many relationship is a type of database relationship where one record in a table can be associated with multiple records in another table. For example, in an ecommerce store, one product can have many reviews, and one review belongs to one product. So the relationship between products and reviews is a one to many relationship.

To create a one to many relationship in Django, you use the `ForeignKey` class from `django.db.models`. You need to specify the name of the related model and the `on_delete` option, which defines what happens when the related record is deleted. For example:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
```

In this example, the Review model has a product field that references the Product model using a foreign key. The on_delete=models.CASCADE option means that if a Product object is deleted, all the Review objects related to it will also be deleted automatically.

You can access the related objects using the dot notation. For example, you can get the product's name from the review object like this:

```python
review = Review.objects.get(id=1)
product_name = review.product.name
```

You can also access the reverse relationship using the lowercased model name followed by \_set. For example, you can get all the reviews for a product object like this:

```python
product = Product.objects.get(id=1)
reviews = product.review_set.all()
```

<h2 align="left">Django Many to Many Realtionship between Model Classes</h2>

A many to many relationship is a type of database relationship where multiple records in one table can be associated with multiple records in another table. For example, in an ecommerce store, one product can belong to multiple categories, and one category can have multiple products. So the relationship between products and categories is a many to many relationship.

To create a many to many relationship in Django, you use the ManyToManyField class from django.db.models. You need to specify the name of the related model and optionally the through option, which defines the intermediate table that stores the association data. For example:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField('Category', through='ProductCategory')

class Category(models.Model):
    name = models.CharField(max_length=50)

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
```

In this example, the Product model has a categories field that references the Category model using a many to many field. The through option specifies the ProductCategory model as the intermediate table that stores the product and category ids. This allows us to add extra fields to the association, such as a timestamp or a rank.

You can access the related objects using the dot notation. For example, you can get the product's categories from the product object like this:

```python
product = Product.objects.get(id=1)
categories = product.categories.all()
```

You can also access the reverse relationship using the lowercased model name followed by \_set. For example, you can get all the products for a category object like this:

```python
category = Category.objects.get(id=1)
products = category.product_set.all()
```

<h2 align="left">Resolve Circular Realtionship between Model Classes</h2>

A circular relationship in Django is a situation where two models depend on each other, creating a circular import error. For example, if model A has a foreign key to model B, and model B has a foreign key to model A, then importing either model will cause an error.

To resolve a circular relationship in Django, you can use a string-based specification of the related model, instead of importing it directly. This way, Django will defer the resolution of the model until it is needed, avoiding the circular import error. For example, instead of writing:

```python
from app.models import B

class A(models.Model):
    b = models.ForeignKey(B, on_delete=models.CASCADE)
```

You can write:

```python
class A(models.Model):
    b = models.ForeignKey('app.B', on_delete=models.CASCADE)
```

This will tell Django to look for the model B in the app module, without importing it at the time of definition.

<h2 align="left">Django Generic Realtionship between Model Classes</h2>

A Django Generic relationship is a way of creating a flexible relationship between a model(app) and any other model(app) in the database, without knowing the exact type of the related model in advance. This is useful for scenarios where you want to associate a model with different kinds of objects, such as comments, tags, ratings, etc.

To create a Generic relationship in Django, you use the `GenericForeignKey` class from `django.contrib.contenttypes.fields`. You also need to add two fields to your model: `content_type` and `object_id`, which store the type and the id of the related object, respectively. For example:

```python
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
```

In this example, the Comment model has a content_object field that references any other model using a generic foreign key. The content_type field stores the type of the related model, such as Product, Category, or User. The object_id field stores the id of the related object, such as 1, 2, or 3.

You can access the related object using the dot notation. For example, you can get the content of the comment object like this:

```python
comment = Comment.objects.get(id=1)
comment_content = comment.content
```

You can also access the reverse relationship using the GenericRelation class from `django.contrib.contenttypes.fields`. This allows you to query the related objects from the other model. For example, you can add a comments field to the Product model like this:

```python
from django.contrib.contenttypes.fields import GenericRelation

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comments = GenericRelation(Comment)
```

This will allow you to get all the comments for a product object like this:

```python
product = Product.objects.get(id=1)
comments = product.comments.all()
```
