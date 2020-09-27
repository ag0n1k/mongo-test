from pymongo import *


def clear_collection(db_name, collection_name, host='localhost', port=27017):
    with MongoClient(host, port) as cl:
        db = cl[db_name]
        result = db[collection_name].bulk_write([
            DeleteMany({})
        ])
        print(result.bulk_api_result)


def main():
    clear_collection(db_name='movies', collection_name='rating_date')
    clear_collection(db_name='movies', collection_name='rating')


if __name__ == '__main__':
    main()
