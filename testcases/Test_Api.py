#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/2/7 14:10
 @功能模块:
 @模块备注:接口测试调试
"""
import requests
import pytest
import jsonpath

class TestApi():

    apiId = ""

    def test01_select_api_list(self):
        url = "http://10.145.11.63:30102/api/all"
        json = {
            "currentPage":1,
            "pageSize":10,
            "apiName":"测试链接"
        }
        response = requests.post(url, json=json)
        print(response.json())
        print ("\n")
        # TestApi.apiId = response.json()['apiId']
        response01 = response.json()
        TestApi.apiId = jsonpath.jsonpath(response01,'$.data.list[0].id')
        print(response.content)
        print(TestApi.apiId)
        print ("\n")
    def test02_select_detail_api(self):
        url = "http://10.145.11.63:30102/api/detail"
        params = {
            "apiId":TestApi.apiId
        }
        response = requests.get(url, params)
        # response01 =repr(response.json()).decode('string_escape')
        # print(response.json())
        # print(response01)
        print('--------------------含笑半步颠--------------------')
        print(response.content)

if __name__ == '__main__':
        pytest.main()
