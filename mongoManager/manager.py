from pymongo import MongoClient
from contextlib import contextmanager
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne


class MongoManager(object):
    def __init__(self, host, port):
        print("Initialize the class context manager")
        self.client = MongoClient(host, port)

    def __enter__(self):
        print("Enter the class context manager")
        return self.client

    def __exit__(self, type, value, traceback):
        print("Close the class context manager")
        self.client.close()


class MongoManagerInheritance(MongoClient):
    def __init__(self, host='localhost', port=27017):
        print("Initialize the Inheritance class context manager")
        super().__init__(host, port)
    pass


@contextmanager
def open_client(host, port):
    print("Initialze the context manager")
    client = MongoClient(host, port)
    try:
        print("Enter the context manager")
        yield client
    finally:
        print("Close the context manager")
        client.close()


def clear_collection(db_name, collection_name, host='localhost', port=27017):
    with open_client(host, port) as cl:
        db = cl[db_name]
        result = db[collection_name].bulk_write([
            DeleteMany({})
        ])
        print(result.bulk_api_result)
