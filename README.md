## djangoProject
Django blog is a beginner friendly blog application. This project illustrate Django Class Based views, How to use django models with custom
model manager, how to use custom template tags, django Forms and model form, how to send mail with django, how to add rss syndication,
and generate sitemap and unit test for model, view, form and template tags and also how to seed database with Factory Boy, Faker and management commands.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installing
```
git clone git@github.com:AJ-Se7eN/djangoProject.git
```

#### or simply download using the https below
```
https://github.com/AJ-Se7eN/djangoProject.git
```

## Requirements
```
Create a virtual environment and active it
and install requirements type:
pip install -r requirements.txt
```

### In this project i have used postgres as a database, change db information in settings with your database information
## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```

## Static files collection
```
python manage.py collectstatic
```

## Creating Superuser
```
python manage.py createsuperuser
```

## For sharing post with email change the email configuration
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your email password'
```

## For authentication with google change the google_oauth2 configuration
```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'google oauth2 key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'google oauth2 secret key'
```

## To run the program in local server use the following command
```
python manage.py runserver
Then go to http://127.0.0.1:8000 in your browser
```

## Project snapshot

### Home Page
![image](/images/home.png)

### Detail Page
![image](/images/detail.png)

### Comment Page
![image](/images/comment.png)

### Post share page
![image](/images/post_share.png)

### Support
If you have any difficulties or questions about using the package, create
[discussion][] in this repository or write to the email
<jetigeenn@gmail.com>.
