FROM python:3.9

RUN pip install --upgrade pip && \
pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv lock --requirements > requirements.txt && \
pip install -r requirements.txt

COPY . .

RUN pip install -e .

CMD ["scripts/launch.sh"]
