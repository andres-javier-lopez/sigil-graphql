import os

DATABASE_URL = os.getenv("DATABASE_URL")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", 0)

DB_TEST_USER = os.getenv("DB_TEST_USER")
DB_TEST_PASSWORD = os.getenv("DB_TEST_PASSWORD")
DB_TEST_NAME = os.getenv("DB_TEST_NAME")
DB_TEST_HOST = os.getenv("DB_TEST_HOST")
DB_TEST_PORT = os.getenv("DB_TEST_PORT", 0)
