# Django Tutorial

## Why Django?

- Fast
- Feature-Rich
- Secure
- Scalable

## 3-Tier Architecture

The 3-Tier Architecture is a software design pattern that divides an application into three logical and physical layers: the presentation tier, the application tier, and the data tier. Each layer has its own responsibilities and communicates with the other layers through well-defined interfaces.

- The **presentation tier** is the user interface layer that displays information to and collects input from the user. It can be a web browser, a desktop application, or a mobile app. The presentation tier communicates with the application tier through HTTP requests or other protocols.
- The **application tier** is the logic layer that processes data and implements the business rules of the application. It can be written in any programming language, such as Python, Java, or PHP. The application tier communicates with the data tier through APIs or database queries.
- The **data tier** is the storage layer that manages the data associated with the application. It can be a relational database, a NoSQL database, or a file system. The data tier stores and retrieves data for the application tier.

The benefits of the 3-Tier Architecture are:

- **Scalability:** The architecture allows each layer to be scaled independently to meet the demand of the application.
- **Flexibility:** The architecture allows each layer to be replaced or upgraded without affecting the other layers. For example, the presentation tier can use different frameworks or technologies, such as React or Angular, while the application tier and the data tier remain unchanged.
- **Reusability:** The architecture allows each layer to be reused across different applications. For example, the application tier can provide APIs for multiple presentation tiers, or the data tier can serve multiple application tiers.

# Django Project vs Django App

- In short django project is the entire web app, e.g Instagram.
- In short django app exists inside the django project, they are sub modules that represents multiple features of the web app, e.g Posts, Status, Story, Reels, etc.

## Create Django Project

```bash
django-admin startproject project_name

# Example
django-admin startproject instagram
```

## Create Django App

```bash
python -m django startapp app_name

# Example
python -m django startapp reels
```
