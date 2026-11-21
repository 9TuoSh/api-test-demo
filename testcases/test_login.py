import pytest
import yaml
import allure
from api.login_api import login
from config.settings import DATA_DIR


with open(DATA_DIR / "login_data.yaml", encoding="utf-8") as f:
    CASES = yaml.safe_load(f)["cases"]


@allure.feature("登录模块")
@allure.story("登录成功场景")
@allure.title("登录成功-{username}")
@pytest.mark.parametrize(
    "username, password",
    [("emilys", "emilyspass"), ("EMILYS", "emilyspass")],
    ids=["正常账号", "用户名大写"],
)
def test_login_success(username, password):
    r = login(username, password)
    assert r.status_code == 200
    body = r.json()
    assert "accessToken" in body
    assert body["accessToken"] != ""
    assert "message" not in body


@allure.feature("登录模块")
@allure.story("登录失败场景")
@allure.title("{case[name]}")
@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_login_fail(case):
    r = login(case["username"], case["password"])
    assert r.status_code == 400
    body = r.json()
    assert body["message"] == case["expect_msg"]
    assert "accessToken" not in body