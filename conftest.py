import pytest
from api.login_api import login


@pytest.fixture(scope="session")
def token():
    r = login("emilys", "emilyspass")
    return r.json()["accessToken"]