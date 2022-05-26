import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--use-database",
        action="store_true",
        default=False,
        help="run test that require database",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--use-database") is False:
        skip_database = pytest.mark.skip(reason="need database to run")
        for item in items:
            if "database" in item.keywords:
                item.add_marker(skip_database)
