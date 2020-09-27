import csv
from mongoengine import *

# data at https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv

class MovieMetaCsv(object):
    def __init__(self, list_movie):
        self.adult = list_movie[0]
        self.belongs_to_collection = list_movie[1]
        self.budget = list_movie[2]
        self.genres = list_movie[3]
        self.homepage = list_movie[4]
        self.id = list_movie[5]
        self.imdb_id = list_movie[6]
        self.original_language = list_movie[7]
        self.original_title = list_movie[8]
        self.overview = list_movie[9]
        self.popularity = list_movie[10]
        self.poster_path = list_movie[11]
        self.production_companies = list_movie[12]
        self.production_countries = list_movie[13]
        self.release_date = list_movie[14]  # date format
        self.revenue = list_movie[15]
        self.runtime = list_movie[16]
        self.spoken_languages = list_movie[17]
        self.status = list_movie[18]
        self.tagline = list_movie[19]
        self.title = list_movie[20]
        self.video = list_movie[21]
        self.vote_average = list_movie[22]
        self.vote_count = list_movie[23]

    def to_orm(self):
        return MovieMeta(
            adult=self.adult,
            belongs_to_collection=self.belongs_to_collection,
            budget=self.budget,
            genres=self.genres,
            homepage=self.homepage,
            mongo_id=self.id,
            imdb_id=self.imdb_id,
            original_language=self.original_language,
            original_title=self.original_title,
            overview=self.overview,
            popularity=self.popularity,
            poster_path=self.poster_path,
            production_companies=self.production_companies,
            production_countries=self.production_countries,
            release_date=self.release_date,
            revenue=self.revenue,
            runtime=self.runtime,
            spoken_languages=self.spoken_languages,
            status=self.status,
            tagline=self.tagline,
            title=self.title,
            video=self.video,
            vote_average=self.vote_average,
            vote_count=self.vote_count
        )


class MovieMeta(Document):
    adult = BooleanField()  # "True"
    belongs_to_collection = StringField()
    budget = IntField()
    genres = StringField()
    homepage = StringField()
    mongo_id = IntField()
    imdb_id = StringField()
    original_language = StringField(max_length=2)
    original_title = StringField(max_length=200)
    overview = StringField()
    popularity = FloatField()
    poster_path = StringField()
    production_companies = StringField()
    production_countries = StringField()
    release_date = StringField()  # todo to Date
    revenue = IntField()
    runtime = StringField()
    spoken_languages = StringField()
    status = StringField()
    tagline = StringField()
    title = StringField()
    video = BooleanField()
    vote_average = FloatField()
    vote_count = IntField()


def csv_load_movies_meta(data_path='data/movies_metadata.csv', class_name=MovieMetaCsv):
    movies_list = []

    with open(data_path, newline='') as csvfile:
        movies_ = csv.reader(csvfile, delimiter=',')
        next(movies_)
        for row in movies_:
            try:
                movies_list.append(class_name(row))
            except IndexError:
                pass
    return movies_list


def save_movies_to_mongo(movies_list, database='movies', host='localhost', port=27017, save_one=False,
                         class_name=MovieMeta):
    mongo_list = []
    connect(database, host=host, port=port)
    for movie in movies_list:
        if save_one:
            mongo_list.append(movie.to_orm().save())
        else:
            mongo_list.append(movie.to_orm())
    if not save_one:
        class_name.objects.insert(mongo_list)
    return mongo_list


def read_mongo(database='movies', host='localhost', port=27017):
    connect(database, host=host, port=port)

    movie_meta = MovieMeta.objects()

    print("Type of movie meta {}".format(type(movie_meta)))
    print("Type of movie meta object {}".format(type(movie_meta[0])))
    print("Title [0]: {}".format(movie_meta[0].title))
    movie_meta[0].modify(title='Toy Story 5')  # =
    print("Title [0] updated: {}".format(movie_meta[0].title))
    movie_meta_2 = MovieMeta.objects()
    print("Title [0] old query: {}".format(movie_meta[0].title))
    print("Title [0] new query: {}".format(movie_meta_2[0].title))
    movie_meta[0].save()
    print("Title [0] after save: {}".format(movie_meta_2[0].title))
    print(len(movie_meta))


def main():
    read_mongo()
    # movies = csv_load_movies_meta()
    # print(movies[0].title)
    # print(movies[1].title)
    # save_movies_to_mongo(movies)


if __name__ == '__main__':
    main()
