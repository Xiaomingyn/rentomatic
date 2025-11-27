import pytest

from application.app import create_app
from manage import read_json_configuration

"""
Fixtures can be defined directly in your test file, but if we want a fixture to be globally available
the best place to define it is the file tests/conftest.py, which is automatically loaded by pytest.

There is a great deal of automation with this definition. If you are not aware of it you might be surprised
by the results, or frustrated by the errors.
"""
@pytest.fixture
def app():
    app = create_app("testing")

    return app

def pytest_addoption(parser):
    parser.addoption(
        "--integration", action="store_true", help="run integration tests"
    )

def pytest_runtest_setup(item):
    if "integration" in item.keywords and not item.config.getvalue("integration"):
        pytest.skip("need --integration option to run")
            
@pytest.fixture(scope="session")
def app_configuration():
    # Hardcoded the name of the configuration file for simplicity. 
    # It could be treated as an environment variable in the management script and read it from here.
    return read_json_configuration("testing")            