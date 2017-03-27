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
from sqlalchemy.ext.declarative import declarative_base

from discovermovies import db

Base = declarative_base()

Base.metadata.reflect(db.engine)


class Movie(Base):
    __table__ = Base.metadata.tables['movie']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'imdb': self.imdbid,
            'collections_id': self.collection_id,
            'language': self.language,
            'original_title': self.original_title,
            'overview': self.overview,
            'popularity': self.popularity,
            'poster_url': self.poster_url,
            'release_date': self.release_date,
            'runtime': self.runtime,
            'tagline': self.tagline,
            'title': self.title,
            'vote_avg': self.vote_avg,
            'vote_count': self.vote_count
        }


class Genre(Base):
    __table__ = Base.metadata.tables['genre']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Actors(Base):
    __table__ = Base.metadata.tables['actors']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class AppearsOn(Base):
    __table__ = Base.metadata.tables['appears_on']


class Collections(Base):
    __table__ = Base.metadata.tables['collections']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'poster_url': self.poster_url
        }


class Crew(Base):
    __table__ = Base.metadata.tables['crew']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'deptid': self.deptid
        }


class Department(Base):
    __table__ = Base.metadata.tables['department']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class MovieGenre(Base):
    __table__ = Base.metadata.tables['movie_genre']


class ProducedBy(Base):
    __table__ = Base.metadata.tables['produced_by']


class ProductionCompanies(Base):
    __table__ = Base.metadata.tables['production_companies']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class WorkedOn(Base):
    __table__ = Base.metadata.tables['worked_on']