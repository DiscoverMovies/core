import pickle
from discovermovies.core.models import User,db
from discovermovies.mod_recommendation.recommender import predict_rating,train_recommender

user_list = db.session.query(User).all()

for user in user_list:
    r,f = train_recommender(user.username)
    rating = predict_rating(r,f)
    with open("user_rating_data/"+user.username, "wb") as movie_id_data:
        pickle.dump(rating, movie_id_data, pickle.HIGHEST_PROTOCOL)