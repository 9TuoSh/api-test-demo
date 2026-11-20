import requests
from config.settings import BASE_URL,USERNAME,PASSWORD


LOGIN_URL = f"{BASE_URL}/auth/login"


def login(username, password):
    """登录接口：一个函数对应一个接口，只负责发请求"""
    return requests.post(LOGIN_URL, json={"username":username, "password":password},timeout=10)