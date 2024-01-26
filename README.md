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

- **HTTP - Hypertext Transfer Protocol** defines how a client and a server can communicate with each other on the internet.

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

<h2 align="left">Django Project vs Django App</h2>

- In short django project is the entire web app, e.g Instagram.
- And django app exists inside the django project, they are sub modules that represents multiple features of the web app, e.g Instagram Posts, Status, Story, Reels, etc.

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

<h2 align="left">Create Django App</h2>

```bash
python -m django startapp app_name

# Example
python -m django startapp reels
```

<h2 align="left">django-admin vs manage.py</h2>
Both are same, command line utility, but there's a subtle difference. When we run the bellow command separately, we get the same result.

```bash
1. django-admin
2. python manage.py
```

`manage.py` takes in-account of the seetings of the project, whereas, `dajngo-admin` doesn't, that's the reason the following command will throw error:

```bash
django-admin runserver
```

whereas, the following command will run:

```bash
python manage.py runserver
```

```bash
python -m django startapp app_name

# Example
python -m django startapp reels
```
