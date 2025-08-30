# Welcome to Garner
Garner is a self-hostable self-reflection journal designhed to help you in your career. 

## Development
Garner is a Django project. Django was picked due to it's modular nature as this means that new functionality can be built as separate apps which can then be included in the distributed app once they're at a level of maturity to do so and should elimate the need for a bunch of feature flags.

Work on the project will be tracked on https://github.com/users/colinfwren/projects/5/views/1

### Set up
Set up is relatively simple
- Run `python3 -m venv venv` to create a new Virtualenv
- Run `source venv/bin/activate` to activate that virtualenv
- Run `pip install -r dev-requirements.txt` to install the dependencies 
- Run `pre-commit install` to install the pre-commit hooks

### Running things locally
In order to run Garner locally you'll need Docker set up. You'll then need to do the following:

1. Run `docker compose up --build` which will pull down the Postgres image and build the Garner image
2. Hit up [http://localhost:8000](localhost:8000) to verify that the server is working
3. Run `docker compose run garner python manage.py migrate` to run the database migrations against the Postgres database