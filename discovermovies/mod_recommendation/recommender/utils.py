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

from collections import defaultdict

from discovermovies import db
from discovermovies.mod_movie import Movie
import re

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
            collections = str([k['name'] for k in data['collections']]);
            actor_list = [k['name'] for k in data['actor_list']]
            p_companies = [k['name'] for k in data['production_companies']]
            crew = [k['name'] for k in data['crew']]
            genre = [k['name'] for k in data['genre']]
            writer.writerow([idx,
                             re.sub("[{}()\"'\[\]]"," ",collections) + " " +
                             re.sub("[{}()\"']", " ",str(data['title'])) + " " +
                             re.sub("[{}()\"']", " ",str(data['overview'])) + " " +
                             re.sub("[{}()\"']", " ",str(data['release_date'])) + " "  +
                             re.sub("[{}()\"']", " ",str(data['tagline'])) + " " +
                             re.sub("[{}()\"']", " ",str(actor_list)) + " " +
                             re.sub("[{}()\"']", " ",str(p_companies)) + " " +
                             re.sub("[{}()\"']", " ",str(crew)) + " " +
                             re.sub("[{}()\"']", " ",str(genre))
                             ])
            id_correspondance[idx] = i.id
    with open("movie_id_data", "wb") as movie_id_data:
        pickle.dump(id_correspondance, movie_id_data, pickle.HIGHEST_PROTOCOL)

def partition(data, min_num):
    """
    This methods divides the entire list to a subset where the content have apears greater than a specified value.


    data contains the list of IDs
    min_num is the threshold used to partition it into sets.

    :param data: list
    :param min_num: integer
    :return: list
    """
    count = defaultdict(int)
    for i in data:
        count[i] += 1
    final_set = []
    for i in count.keys():
        if count[i] > min_num:
            final_set.append(i)
    return final_set