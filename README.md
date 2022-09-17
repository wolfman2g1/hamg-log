![Tests](https://github.com/wolfman2g1/hamg-log/actions/workflows/django.yml/badge.svg)  ![CodeQL](https://github.com/wolfman2g1/hamg-log/actions/workflows/codeql-analysis.yml/badge.svg)
# hamg-log
basic django app to log ham radio contacts

## install
clone repo and install requirements

```bash
git clone git@github.com:wolfman2g1/hamg-log.git
cd hamg_log
pip install poetry
poetry shell
poetry install
```
# run database migrations
you should do this everytime you do a `git pull` this will keep your data model current in the event that I make db changes
```bash
./manage.py migrate
```

## to run
```bash
python manage.py runserver
```
or depending on set up

```bash
./manage.py runserver
```

## testing. 
all views and models must have a test
test files must begin with test. test functions but begin with test
```bash
python manage.py test
```
I'm writing the tests now. basically when you write your views  you can run the test to make sure it does what you expect