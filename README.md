# DummyJSON 接口自动化测试

![API Test](https://github.com/9TuoSh/api-test-demo/actions/workflows/test.yml/badge.svg)

基于 pytest + requests 的接口自动化测试框架，被测对象为 [DummyJSON](https://dummyjson.com) 公开 API。

## 技术栈

| 技术 | 用途 |
| --- | --- |
| pytest | 测试框架 |
| requests | HTTP 请求库 |
| PyYAML | YAML 数据驱动 |
| Allure | 测试报告 |
| GitHub Actions | 持续集成 |

## 项目结构
demo/
├── api/ # 接口层：封装请求，不写断言
│ ├── login_api.py
│ └── user_api.py
├── config/ # 配置层：环境地址、路径
│ └── settings.py
├── data/ # 数据层：YAML 测试数据
│ └── login_data.yaml
├── testcases/ # 用例层：只写断言
│ ├── test_login.py
│ └── test_userinfo.py
├── conftest.py # 全局 fixture（session 级 token）
├── pytest.ini # pytest 配置
├── requirements.txt # 依赖清单
└── .github/workflows/
└── test.yml # CI 配置


## 设计要点

- **分层架构**：配置层 / 接口层 / 数据层 / 用例层职责分离
- **单一数据源**：`BASE_URL` 统一由 `config/settings.py` 管理
- **session 级 token fixture**：整个测试会话只登录一次，所有用例共享
- **数据驱动**：登录失败场景通过 YAML + `@pytest.mark.parametrize` 驱动
- **统一超时**：所有请求设置 `timeout=10`，避免网络异常导致用例挂起
- **报告可读**：Allure 按 feature/story 分组，用例标题中文化

## 环境要求

- Python 3.11+
- 依赖安装：

```bash
pip install -r requirements.txt