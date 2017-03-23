import requests

base_url = 'http://localhost:8080'


def test_auth(username, password):
    r = requests.post(base_url + '/user/auth', data={'username': username, 'password': password})
    return r.text


def test_create_user(username, password, email, phone):
    r = requests.post(base_url + '/user/create', data={
        'username': username,
        'password': password,
        "email": email,
        "phone": phone
    })
    return r.text


def test_user_check(username):
    r=requests.get(base_url+'/user/check',params={'username':username})
    return r.text

def test_user_search(username):
    r=requests.get(base_url+'/user/search',params={'username':username})
    return r.text