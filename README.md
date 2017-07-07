## django portfolio template
Template for quickly building a portfolio

## Prerequisites
Built using python2.7.
Clone this repository and delete the .git folder.
````
git clone django-portfolio-template
rm -rf django-portfolio-template/.git
````
Download the virtualenv package.
````
pip install virtualenv
````
Create and activate a  virtual environment on the cloned template folder for development.
````
virtualenv django-portfolio-template
source django-portfolio-template/bin/activate
````
Then in the virtual environment run the following;
````
(django-portfolio-template)[user@host~]$ pip install requirements.txt
(django-portfolio-template)[user@host~]$ cd django-portfolio-template
````
Then run these commands;
````
(django-portfolio-template)[user@host~]$ python manage.py collectstatic
You have requested to collect static files at the destination
location as specified in your settings:

		/path/on/your/machine/staticfiles

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes
...
(django-portfolio-template)[user@host~]$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, portfolio, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
...
(django-portfolio-template)[user@host~]$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
July 07, 2017 - 09:38:59
Django version 1.10.5, using settings 'portfolio_template.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

````
## Quick start
On your favourite browser go to http://127.0.0.1:8000/create_portfolio and fill the form with 
your details.
Note: By default the form is disabled as soon as you submit your details, so make them count or 
customize this behavior.

## Deployment
Since it has been made to be easily deployable to heroku simply do the following if you have an account
and have heroku-cli installed;
Add the following to settings.py in project_template folder,
````
ALLOWED_HOSTS = [
	u'127.0.0.1',
	u'appname.herokuapp.com', # appname here is the name of your app in heroku
	]
````
Then run the following commands,
````
git init
git add .
git commit -m "Your portfolio"
heroku login
heroku create appname
git push heroku master
````

