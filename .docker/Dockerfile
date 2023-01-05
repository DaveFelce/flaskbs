FROM python:3.11 as base

WORKDIR /src
ADD .. .
RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry build

from base as builder

WORKDIR /app
ARG wheel=flaskbs-*-py3-none-any.whl
COPY --from=base /src/dist/$wheel .
RUN pip install $wheel && rm $wheel
RUN apt update && apt -y install postgresql
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
