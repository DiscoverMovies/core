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

from discovermovies import db
from discovermovies.mod_movie.models import Movie, MovieGenre

mod_movie = Blueprint('movie',__name__)

@mod_movie.route('/movie/get/<int:movie_id>')
def get_movie(movie_id):
    movie = db.session.query(Movie).filter_by(id=movie_id).first()
    if movie is None:
        abort(404)
    return jsonify(status='OK', movie=movie.serialize)

@mod_movie.route('/movie/search', methods=['GET'])
def search_movie():
    q = request.args.get('q','')
    movie_list = db.session.query(Movie).filter(Movie.title.ilike("%"+q+"%")).order_by(Movie.vote_count.desc()).limit(10).all()
    return jsonify(status='OK', movie_list=[i.serialize for i in movie_list])

@mod_movie.route('/movie/popular/<int:genre_id>')
def get_popular_genre_movie(genre_id):
    movie_list = db.session.query(MovieGenre)