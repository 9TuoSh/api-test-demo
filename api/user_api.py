import requests
from config.settings import BASE_URL

ME_URL = f"{BASE_URL}/auth/me"


def get_me(token=None):
    """
    获取当前登录用户信息。

    token=None  : 不携带 Authorization 头（模拟完全未登录）
    token=""    : 携带 Authorization: Bearer （空值）
    token="abc" : 携带 Authorization: Bearer abc（无效值）
    """
    headers = {}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"

    return requests.get(ME_URL, headers=headers, timeout=10)