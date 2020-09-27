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

    def __init__(self, list_: list):
        self.user_id = int(list_[0])
        self.movie_id = int(list_[1])
        self.rating = float(list_[2])
        self.timestamp = int(list_[3])
        self.release_date = self.__convert_to_date()
        self.__test_field = hash(self)

    def get_test_field(self):
        return self.__test_field

    def __convert_to_date(self):
        return datetime.fromtimestamp(self.timestamp)

    def to_orm(self):
        return Rating(
            user_id=self.user_id,
            movie_id=self.movie_id,
            rating=self.rating,
            timestamp=self.timestamp,
            release_date=self.release_date
        )


class Rating(Document):
    user_id = IntField()
    movie_id = IntField()
    rating = FloatField()
    timestamp = IntField()
    release_date = DateTimeField()


def main():
    g = movies.csv_load_movies_meta(data_path='data/ratings_small.csv', class_name=RatingCsv)
    for i in range(1, 5):
        print(g[i].__dict__)
        # print(g[i]._RatingCsv__test_field)
        #
        # print(g[i].get_test_field())
        #
        # g[i]._RatingCsv__test_field = 4
        #
        # print(g[i]._RatingCsv__test_field)
        #
        # print(g[i].get_test_field())
    h = movies.save_movies_to_mongo(g, class_name=Rating, save_one=False)
    # h = movies.save_movies_to_mongo(g, class_name=Rating, save_one=True)
    # for i in range(1, 5):
    #     print(h[i].__dict__)


if __name__ == '__main__':
    main()
