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
import csv
import pickle

from discovermovies import db
from discovermovies.mod_movie import Movie


def parse_movie_id_list(movie_id_list):
    pass


def generate_csv_movie_data():
    movies = db.session.query(Movie).all()
    id_correspondance = dict()
    with open("movie_data.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id','description'])
        for idx,i in enumerate(movies):
            data = i.serialize
            writer.writerow([idx,
                             str(data['collections']) + " " +
                             str(data['title']) + " " +
                             str(data['overview']) + " " +
                             str(data['release_date']) + " " +
                             str(data['tagline']) + " " +
                             str(data['actor_list']) + " " +
                             str(data['production_companies']) + " " +
                             str(data['crew']) + " " +
                             str(data['genre'])
                             ])
            id_correspondance[idx] = i.id
    with open("movie_id_data", "wb") as movie_id_data:
        pickle.dump(id_correspondance, movie_id_data, pickle.HIGHEST_PROTOCOL)
