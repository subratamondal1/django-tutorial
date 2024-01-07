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
