import requests

base_url = 'http://localhost:8080'


def test_rate_movie(movie_id, rating, token):
    r = requests.post(base_url + '/rate/movie/' + str(movie_id), data={'rating': rating, 'token': token})
    return r.text
