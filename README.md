## About the Project

* Grand Slam Collections is a baseball card
collectors app. The app was built for
collectors to better organize and catalog
their collection of baseball cards. Users can
register an account on the site and find
existing cards by browsing by players or by
card sets. A user has the ability to add a
player, card, or set to the database, if they do
not currently exist. In the 'My Collections' tab,
a user can view cards added to their
collection, delete cards from the collection,
or edit any notes they may have. The 'Set'
and 'Player' tabs both have filtering
functionality to make finding a specific card
much easier.

## Project Definition

* FULL STACK application written in PYTHON using DJANGO framework
* Ability to create, read, update, and delete user-specific data

## Setup

Steps to get started:
1. `git clone git@github.com:ChaseSully222/Backend-Capstone.git`
1. `cd` into directory created and `cd` into `baseballcardapp` directory where the `manage.py` file is; set up your virtual environment:

#### Mac users, run the following:
```sh
python -m venv baseballcardenv
source ./baseballcardenv/bin/activate
pip install django
pip freeze > requirements.txt
```
#### Windows users, run the following:
```sh
python -m venv baseballcardenv
source ./baseballcardenv/Scripts/activate
pip install django
pip freeze > requirements.txt
```
> Note the separate formats for the `source` command between Windows and Mac users. You will use this command each time you activate your virtual environment for this project.

3. Run a database migration using the `migrate` command, below, to create a set of tables that Django maintains for user management.

```sh
python manage.py makemigrations baseballcardapp
python manage.py migrate
```

4. Load Performance Rights Organization fixtures by using command, `python manage.py loaddata PROs`
4. Start application using command, `python manage.py runserver`
4. Navigate browser to [http://localhost:8000](http://localhost:8000)