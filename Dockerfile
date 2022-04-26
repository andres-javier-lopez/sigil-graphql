FROM python:3.9 AS base

RUN pip install --upgrade pip && \
pip install poetry

WORKDIR /usr/src/app

FROM base AS req

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-dev

FROM req AS code

COPY . .

FROM code AS app

CMD ["scripts/launch.sh"]

FROM req AS dev

RUN poetry install

COPY . .
