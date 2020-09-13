from contextlib import contextmanager


class MongoManager(object):
    # необходимо реализовать класс - менеджер контекста
    def __init__(self):
        self.client = ""


class MongoManagerInheritance:
    # необходимо реплизовать класс - наследуемый от MongoClient
    def __init__(self):
        print("Initialize the Inheritance class context manager")


@contextmanager
def open_client():
    # необходимо с помощью функции реализовать менеджер контекста, используя генераторы
    pass


def clear_collection(db_name, collection_name, host='localhost', port=27017):
    # необходимо реализовать полную очистку коллеции через операцию bulk_write
    pass
