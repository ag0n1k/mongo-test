from mongoengine import *
from datetime import datetime

import orm_movies

# data at https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv


class RatingCsv(object):
    user_id: int
    movie_id: int
    rating: float
    timestamp: int
    release_date: datetime

    def __init__(self):
        pass


class Rating(Document):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
