from pymongo import MongoClient

with MongoClient() as cl:
    db = cl.movies
    print(db.movie_meta.count())
