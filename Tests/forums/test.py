import requests

from Tests.core.test import base_url

def test_get_all_forum():
    r=requests.get(base_url+'/forum/all')
    return r.text

def test_get_forum(forum_id):
    r=requests.get(base_url+'/forum/get/'+str(forum_id))
    return r.text

def test_search_forum(text):
    r=requests.get(base_url+'/forum/search', params={'q':text})
    return r.text

def test_get_replies(forum_id):
    r = requests.get(base_url+'/forum/reply/get/'+str(forum_id))
    return r.text

def test_create_forum(forum_title,text,token):
    r = requests.post(base_url+'/forum/create', data={'token':token,'title':forum_title,'text':text})
    return r.text

def test_create_reply(forum_id,text,token):
    r = requests.post(base_url+'/forum/reply/post/'+str(forum_id), data={'token':token,'text':text})
    return r.text


def test_delete_forum(forum_id,token):
    r = requests.post(base_url+'/forum/delete/'+str(forum_id), data={'token':token})
    return r.text

def test_update_forum(forum_id,token,title,text):
    r = requests.post(base_url+'/forum/update/'+str(forum_id), data={'token':token,'title':title,'text':text})
    return r.text