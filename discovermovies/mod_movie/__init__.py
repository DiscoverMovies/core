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

from discovermovies.mod_movie.models import Movie

mod_movie = Blueprint('movie',__name__)

@mod_movie.route('/movie/get/<int:movie_id>')
def get_movie(movie_id):
    movie = Movie.query.get(id=movie_id)
    return jsonify(status='OK')