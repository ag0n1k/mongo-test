from mongoManager import manager as m
import datetime
import pprint
from random import randint


def gen_post(number: str):
    names = [
        "Andrey",
        "Nataliy",
        "Valeria"
    ]
    return {
        "author": "{}".format(names[randint(0, 2)]),
        "text": "My {iter} blog post!".format(iter=number),
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    }


def use_context_function(num, host='localhost', port=27017):
    print("Enter the function")
    with m.open_client(host, port) as cl:
        db = cl.test_database
        print("database obj: {}".format(db))
        posts = db.posts
        post_id = posts.insert_one(gen_post(num)).inserted_id
        print('Close the connection')
    return post_id


def use_context_class(num, host='localhost', port=27017):
    print("Enter the class function")
    with m.MongoManager(host, port) as cl:
        db = cl.test_database
        print("database obj: {}".format(db))
        posts = db.posts
        post_id = posts.insert_one(gen_post(num)).inserted_id
        print('Close the connection')
    return post_id


def use_mongo_class(num, host='localhost', port=27017):
    print("Enter the class function")
    with m.MongoManagerInheritance(host, port) as cl:
        db = cl.test_database
        print("database obj: {}".format(db))
        posts = db.posts
        post_id = posts.insert_one(gen_post(num)).inserted_id
        print('Close the connection')
    return post_id


def bulk_sample():
    from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne
    cl = m.MongoManagerInheritance()
    db = cl.bulk_test
    result = db.bulk.bulk_write([
        DeleteMany({}),
        InsertOne({'_id': 1}),
        InsertOne({'_id': 2}),
        InsertOne({'_id': 3}),
        UpdateOne({'_id': 1}, {'$set': {'foo': 'bar'}}),
        UpdateOne({'_id': 4}, {'$inc': {'j': 1}}, upsert=True),
        ReplaceOne({'j': 1}, {'j': 2})
    ])
    return result


def find_one(host='localhost', port=27017):
    with m.MongoManager(host, port) as cl:
        db = cl.test_database
        print("database obj: {}".format(db))
        posts = db.posts
        pprint.pprint(posts.find())



def main():
    m.clear_collection(db_name='movies', collection_name='movie_meta')
    # use_context_function('first')
    # use_context_class('second')
    # use_context_class('third')
    # use_mongo_class('fourth')
    # print(bulk_sample().bulk_api_result)
    # find_one()
    # print("Exit")


if __name__ == '__main__':
    main()

# ORM - Object-relation mapping
