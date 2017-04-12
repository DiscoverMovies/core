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

from discovermovies.core.models import User
from discovermovies.mod_movie.models import Movie, Genre
from discovermovies import db


class Rating(db.Model):
    __tablename__ = "rating"

    username = db.Column(db.String(100),db.ForeignKey('User.username'))
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id'))
    rating = db.Column(db.Integer, db.CheckConstraint)

    db.PrimaryKeyConstraint(username, movie_id)

