
def return_iter():
    for i in range(1, 5):
        print("iter_print: {}".format(i))
    return range(1, 5)


def return_generator():
    for i in range(1, 5):
        print("gen_{}".format(i))
        yield i


print(return_generator())

print("---")

print(next(return_generator()))

print("-----")

for i in return_generator():
    print("generator: {}".format(i))

print("-------")

print("type of iter: {}".format(type(return_iter())))
