import pytest
import allure
from api.user_api import get_me


@allure.feature("用户模块")
@allure.story("鉴权校验")
@allure.title("有效token-获取用户信息成功")
def test_me_with_valid_token(token):
    with allure.step("携带有效 token 请求 /auth/me"):
        r = get_me(token)
    with allure.step("断言状态码为 200"):
        assert r.status_code == 200
    with allure.step("断言返回的 username 为 emilys"):
        assert r.json()["username"] == "emilys"


@allure.feature("用户模块")
@allure.story("鉴权校验")
@allure.title("不带token-提示缺少凭证")
def test_me_without_token():
    with allure.step("不携带 Authorization 头请求 /auth/me"):
        r = get_me()
    with allure.step("断言返回 401 且提示缺少凭证"):
        assert r.status_code == 401
        assert r.json()["message"] == "Access Token is required"


@allure.feature("用户模块")
@allure.story("鉴权校验")
@allure.title("无效token-{token}")
@pytest.mark.parametrize("token", ["", "abc"], ids=["空token", "无效token"])
def test_me_invalid_token(token):
    with allure.step(f"携带无效 token（token={token!r}）请求 /auth/me"):
        r = get_me(token)
    with allure.step("断言返回 401 且提示凭证无效"):
        assert r.status_code == 401
        assert r.json()["message"] == "Invalid/Expired Token!"