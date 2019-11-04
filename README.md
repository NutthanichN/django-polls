## Django Polls Application

Web Application that user can vote a poll from Django Tutorial parts 1-5 in [Django Getting Started](https://docs.djangoproject.com/en/2.2/intro/)

## Requirements

* Python 3.6 or newer
* Django 2.1.2 or newer
* Python add-on modules as in [requirements.txt](requirements.txt)

## How to install

1. Access `django-polls` directory

2. Install required packages <pre class=output>pip install -r requirements.txt</pre>

3. Create `.env` in the root directory for setting configurations (`SECRET_KEY` and `DEBUG`)

4. Create the database <pre class=output>python manage.py migrate</pre>

## How to run

1. Access `django-polls` directory

2. Run server <pre class=output>python manage.py runserver</pre>