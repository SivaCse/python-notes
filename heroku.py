'''Deploying on Heroku'''

# Heroku is a container-based cloud Platform as a Service (PaaS).
# Developers use Heroku to deploy, manage, and scale modern apps.

# https://www.heroku.com/
# https://www.airpair.com/heroku/posts/heroku-tips-and-hacks

# You can create a new python 'app' via Heroku's website or via the command
# line. First, make sure you've created an account and downloaded the
# Heroku Command Line Interface (CLI). You can install this with brew:

# $ brew install heroku/brew/heroku

# Next, in the command line, cd to the folder where your main script/program
# file lives and login to heroku using your email, password:

# $ heroku login

# Next, create an app by giving it a name. Note, the name may not be available
# if it's already being used by someone else:

# $ heroku create kusshi

# The URL will be:

# https://kusshi.herokuapp.com/ | https://git.heroku.com/kusshi.git

# You can see all your apps with this command:

# $ heroku apps

# To upload files to heroku, use Git. We'll also use an external library called
# gunicorn. This should be installed in the virtual env.

# $ pip3 install gunicorn
# https://devcenter.heroku.com/articles/python-gunicorn

# Now we need to make sure to include three files before we upload. These
# should be located in the same directory as our main script/program file.

# 1. requirements.txt
#    (see package_management.py or virtual_environments.py)
#    $ pip3 freeze > requirements.txt
#    (remember to do this through your virtual environment)

# 2. Procfile
#    https://devcenter.heroku.com/articles/procfile
#    This is a file (no extension) that tells heroku what web server we want
#    to use with our application. We'll type the following line in the file
#    where myscript is the name of your main python file without the '.py':
#    web: gunicorn myscript:app

# 3. runtime.txt
#    https://devcenter.heroku.com/articles/python-runtimes
#    This tells heroku what python version you would like heroku to run your
#    your app with. If you don't specify, it'll be Python 2.7 (ew!). Check the
#    link above to see which runtime versions are available and enter one:
#    python-3.6.3

# Now let's get our Git set up:
# $ git init
# $ git add -A
# $ git commit -m 'Initial commit'

# Finally, upload to heroku (where kusshi is your app name):
# $ heroku git:remote --app kusshi
# $ git push heroku master

# Provided the push was successful, you can now navigate to the URL in the
# browser (https://kusshi.herokuapp.com/) or using the command line:

# $ heroku open

# When you make changes, you'll want to test them in your local environment.
# When your ready, you'll need to git commit the changes before pushing to
# your 'production' server on heroku.

# You can also get some bits of information by using this command:

# $ heroku info

# The above command is helpful in terms of telling you whether you're
# connected to your app at the moment.

# NOTE: one thing I discovered is heroku doesn't like regular 'http://' links
# to external sources like googlefonts. Instead, change those to 'https://'
# and everything should work fine.

# -----------------------------------------------------------------------------
# Creating a PostgreSQL database on heroku
# -----------------------------------------------------------------------------
# Databases are included as add-ons in heroku. You can create a database
# through the website or (a better way) through the command line. This allows
# you to connect the database to your heroku app.

# $ heroku addons:create heroku-postgresql:hobby-dev --app malaspina

# There are a number of databse options available through heroku, the hobby-dev
# one is free but you are limited to 10,000 rows (records) in your database.

# $ heroku config --app malaspina

# This will print out your database url like:
# DATABASE_URL: postgres://lfhrlgygusjxap:ec6f16796cc41ea29a18251f3dc3ade9e2...

# Copy the URL and paste it into your .py file where you were connecting to
# your PostgreSQL databse. This address would have been something like:
# url = 'postgresql://postgres:cinnamon-sticks@localhost/survey_app'

# Add the following to the end of the heroku databse url string:
# ?sslmode=require

# Keep in mind, this will create an empty database. It will not have any tables
# yet. See the docstring of the Data class in survey_app.

# Note if you want to query the database locally, you'll need to make sure
# the "local psql command path" is updated. To do this type the following:

# $ export PATH=$PATH:/Library/PostgreSQL/10/bin

# Where the path is pointing to your installation of PostgreSQL.

# Once that's in place you can type something like this (where malaspina is
# the name of your app):

# $ heroku pg:psql --app malaspina

# The prompt will look something like this: malaspina::DATABASE=>
# And now you can start querying the database:

# SELECT * FROM data;

# When you're ready to quit this PostrgeSQL utility, type \q
