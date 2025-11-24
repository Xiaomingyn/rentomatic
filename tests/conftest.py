import pytest

from application.app import create_app

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