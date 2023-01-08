## configurations

- create a `local.env` file in the root directory
- add vars as required in `flaskbs.core.config.Config`

## running

- `poetry install`

### api run

- `flask db upgrade`
- `poetry run python -m flask run --host=0.0.0.0`

## Docker

- `docker-compose -f .docker/development/docker-compose.yml up --build`

