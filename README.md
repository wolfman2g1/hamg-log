![Tests](https://github.com/wolfman2g1/hamg-log/actions/workflows/django.yml/badge.svg)  ![CodeQL](https://github.com/wolfman2g1/hamg-log/actions/workflows/codeql-analysis.yml/badge.svg)
# hamg-log
basic django app to log ham radio contacts

## install
clone repo and install requirements

```bash
git clone git@github.com:wolfman2g1/hamg-log.git
pip install poetry
poetry shell
poetry install
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
all views and models most have a test
test files must begin with test. test functions but begin with test
```bash
python manage.py test
```