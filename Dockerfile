FROM python:3.9 AS base

RUN pip install --upgrade pip && \
pip install pipenv

WORKDIR /usr/src/app

FROM base AS req

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv lock --requirements > requirements.txt && \
pip install -r requirements.txt

FROM req AS code

COPY . .

RUN pip install -e .

FROM code AS app

CMD ["scripts/launch.sh"]

FROM code AS dev

RUN pipenv lock --dev --requirements > requirements.txt && \
pip install -r requirements.txt
