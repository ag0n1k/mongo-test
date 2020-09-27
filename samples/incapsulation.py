class A:
    # необходимо реплизовать класс - наследуемый от MongoClient
    def __init__(self):
        print("Initialize the Inheritance class context manager")
        self.list = []
        self._list = []
        self.__list = []

    def list_some(self):
        return self.__list_some()

    def _list_some(self):
        return filter(lambda x: x % 2, self.list)

    def __list_some(self):
        return filter(lambda x: x % 2, self.list)


def gen_post(a: int):
    return "integer: {}".format(a)


def gen_post(a: str):
    return "string: {}".format(a)


print(gen_post(2))
print(gen_post("second"))
a = "2"
print(type(a))
a = 2
print(type(a))
a = A()
print("a.list: {}".format(a.list))
print("a._list: {}".format(a._list))
try:
    print("a.__list: {}".format(a.__list))
except Exception:
    print("a.__list is private")
print(a.list_some())
try:
    print("a.__list: {}".format(a.__list()))
except Exception:
    print("a.__list() is private")
