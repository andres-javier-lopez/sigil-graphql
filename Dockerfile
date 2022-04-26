FROM python:3.9 AS base

RUN pip install --upgrade pip && \
pip install poetry

WORKDIR /usr/src/app

FROM base AS req

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-dev --no-root

FROM req AS code

COPY . .
RUN poetry install --no-dev

FROM code AS app

CMD ["scripts/launch.sh"]

FROM req AS dev

RUN poetry install --no-root

COPY . .
RUN poetry install
