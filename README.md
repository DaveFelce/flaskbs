## configurations

- create a `local.env` file in the root directory
- add vars as required in `flaskbs.core.config.Config`

## running

- `poetry install`

### api run

- `flask db upgrade`
- `poetry run python -m flask run --host=0.0.0.0`


- `curl -H "Content-Type: application/json" -X POST -d '{"username":"dave","email":"test@test.com"}' http://127.0.0.1:5000/user`
- `curl -X GET http://127.0.0.1:5000/user/dave`

## Docker

- `docker-compose -f .docker/development/docker-compose.yml up --build`

the docker container exposes port 5001