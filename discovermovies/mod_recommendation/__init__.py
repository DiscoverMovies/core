"""
    Copyright (C) 2017 Sidhin S Thomas

    This file is part of discovermovie.

    discovermovies is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    discovermovie is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with discovermovie.  If not, see <http://www.gnu.org/licenses/>.
"""
from flask import Blueprint, jsonify
from flask import abort
from flask import request

from discovermovies import db, movie_id_dictionary, movie_recommendation
from discovermovies.mod_movie import Movie
from discovermovies.mod_recommendation.models import Rating
from discovermovies.utlils import get_error_json, check_token

mod_recommendation = Blueprint("mod_recommendation", __name__)


@mod_recommendation.route("/rate/movie/<int:movie_id>", methods=["POST"])
def rate_movie(movie_id):
    try:
        username = check_token(request.form['token'])
        if username is None:
            return get_error_json('Invalid token', 'invalid_token')
    except KeyError:
        return get_error_json('Missing token', 'missing_data')
    try:
        user_rating = request.form['rating']
    except KeyError:
        return get_error_json("Missing rating", "missing_data")
    rating = Rating()
    rating.movie_id = movie_id
    rating.username = username
    rating.rating = int(user_rating)
    db.session.add(rating)
    db.session.commit()
    return jsonify(status="OK")


@mod_recommendation.route("/rating/user/all/<token>", )
def get_all_user_rating(token):
    username = check_token(token)
    if username is None:
        return get_error_json('Invalid token', 'invalid_token')
    ratinglist = Rating.query.filter_by(username=username)
    return jsonify(status="OK", rating_list=[i.serialize for i in ratinglist])

@mod_recommendation.route("/rate/movie/all/<int:movie_id>")
def get_all_movie_rating(movie_id):
    movie_rating_list = Rating.query.filter_by(movie_id=movie_id)
    return jsonify(status="OK", rating_list=[i.serialize for i in movie_rating_list])

@mod_recommendation.route("/rating/user/remove/<int:movie_id>/<token>")
def remove_rating(movie_id,token):
    username = check_token(token)
    if username is None:
        return get_error_json('Invalid token', 'invalid_token')
    rating = Rating.query.filter_by(username=username).filter_by(movie_id=movie_id).first()
    if rating is None:
        abort(404)
    db.session.delete(rating)
    db.session.commit()
    return jsonify(status="OK")

@mod_recommendation.route("/recommendation/movie/<int:movie_id>")
def get_recommendation_movie(movie_id):
    index = movie_id_dictionary[movie_id]
    num = 10
    if "count" in request.args:
        num = int(request.args["count"])
    recommendation_list = movie_recommendation.predict(index,num)
    movie_list = []
    for i in recommendation_list:
        id = movie_id_dictionary[i[1]]
        movie_list.append(db.session.query(Movie).filter_by(id=id).first())
    return jsonify(status="OK", movie_list=[i.serialize for i in movie_list])