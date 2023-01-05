## configurations

- create a `local.env` file in the root directory
- add vars as required in `flaskbs.core.config.Config`

## running

- `poetry install`

### api run

- `poetry run python wsgi.py`

## Docker

- docker build -t flaskbs .
- docker run -d --name flaskbs_container -p 5001:5001 flaskbs

