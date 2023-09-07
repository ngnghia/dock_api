import sys, os
import allure
import pytest
from pytest import  mark
import requests
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

@allure.story('Select user')
def test_select_user():
    url = "https://reqres.in/api/users/4"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


@allure.story('delete user')
@mark.functional
def test_delete_user():
    url = "https://reqres.in/api/users/4"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


@allure.story('update user')
@mark.functional
def test_update_user():
    url = "https://reqres.in/api/users/4"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)



