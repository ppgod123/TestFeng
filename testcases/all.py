#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/7 16:19
 @功能模块:接口用例
 @模块备注:
"""
import pytest


if __name__ == '__main__':
    # pytest.main(['-vs','test_login.py'])
    #pytest.main(['-vs','./main/first.py'])
      # pytest.main(['-vs', './testcases/test_login.py::test_01_baili01'])
    pytest.main(['-vs', './testcases/test_login.py::TestLogin::test_01_baili'])