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

from discovermovies import db
from discovermovies.mod_movie.models import AppearsOn, Genre, Crew, MovieGenre, WorkedOn, Movie
from discovermovies.mod_recommendation import Rating
from discovermovies.mod_recommendation.recommender.utils import partition
from dm_recommendation_engine import UserRecommendationGenerator


class NotEnoughRatingError(Exception):
    pass


def get_feature_sets():
    actor_list = db.session.query(AppearsOn).all()
    actor_list = partition([i.aid for i in actor_list], 5)
    genre_list = db.session.query(Genre).all()
    genre_list = [i.id for i in genre_list]
    crew_list = db.session.query(Crew).filter(Crew.dept.ilike("%Director%"))
    crew_list = [ i.id for i in crew_list]
    return actor_list, genre_list, crew_list


def train_recommender(username):
    ratings = Rating.query.filter_by(username=username).all()
    if len(ratings) < 10:
        raise NotEnoughRatingError
    feature_sets = get_feature_sets()
    feature_matrix_actors = [[0 for j in feature_sets[0]] for i in ratings]
    feature_matrix_genre = [[0 for j in feature_sets[1]] for i in ratings]
    feature_matrix_director = [[0 for j in feature_sets[2]] for i in ratings]
    user_rating = []
    for idx,i in enumerate(ratings):
        actor_list = db.session.query(AppearsOn).filter_by(mid=i.movie_id)
        actor_list = [ i.aid for i in actor_list]
        for j in range(len(feature_sets[0])):
            if feature_sets[0][j] in actor_list:
                feature_matrix_actors[idx][j] = 1
        genre_list = db.session.query(MovieGenre).filter_by(mid=i.movie_id)
        genre_list = [ i.gid for i in genre_list]
        for j in range(len(feature_sets[1])):
            if feature_sets[1][j] in genre_list:
                feature_matrix_genre[idx][j] = 1
        movie_directors = db.session.query(WorkedOn).filter_by(mid=i.movie_id)
        director_list = db.session.query(Crew).filter(Crew.dept.ilike("%Director%")).filter(
            Crew.id.in_([i.cid for i in movie_directors])
        )
        director_list = [i.id for i in director_list]
        for j in range(len(feature_sets[2])):
            if feature_sets[2][j] in director_list:
                feature_matrix_director[idx][j] = 1
        user_rating.append(i.rating)

    r = UserRecommendationGenerator()
    r.train(user_rating,feature_matrix_actors,feature_matrix_genre,feature_matrix_director)
    return r, feature_sets

def predict_rating(r, feature_sets):
    movie_list = db.session.query(Movie).all()
    user_movie_rating = {}
    for movie in movie_list:
        feature_matrix_actors = [0 for j in feature_sets[0]]
        feature_matrix_genre = [0 for j in feature_sets[1]]
        feature_matrix_director = [0 for j in feature_sets[2]]
        actor_list = db.session.query(AppearsOn).filter_by(mid=movie.id)
        actor_list = [i.aid for i in actor_list]
        for j in range(len(feature_sets[0])):
            if feature_sets[0][j] in actor_list:
                feature_matrix_actors[j] = 1
        genre_list = db.session.query(MovieGenre).filter_by(mid=movie.id)
        genre_list = [i.gid for i in genre_list]
        for j in range(len(feature_sets[1])):
            if feature_sets[1][j] in genre_list:
                feature_matrix_genre[j] = 1
        movie_directors = db.session.query(WorkedOn).filter_by(mid=movie.id)
        director_list = db.session.query(Crew).filter(Crew.dept.ilike("%Director%")).filter(
            Crew.id.in_([i.cid for i in movie_directors])
        )
        director_list = [i.id for i in director_list]
        for j in range(len(feature_sets[2])):
            if feature_sets[2][j] in director_list:
                feature_matrix_director[j] = 1

        rating = r.predict(feature_matrix_actors,feature_matrix_genre,feature_matrix_director)
        if rating > 0:
            user_movie_rating[movie.id] = rating
    return user_movie_rating