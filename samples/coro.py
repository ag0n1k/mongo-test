

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


def moduler():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total % count


def sample_coroutine(a):
    print("Started: a = ", a)
    b = yield a
    print("Received: b = ", b)
    c = yield a + b
    print("Received: c = ", c)
    yield a + b + c


def main():
    t = sample_coroutine(1)
    _ = next(t)
    print("Coro2: ", t.send(2))
    print("Coro3: ", t.send(3))


    # sample:
    # import coro
    # coro_avg = coro.averager()
    # next(coro_avg)
    # coro_avg.send(10)
    # coro_avg.send(30)


if __name__ == '__main__':
    main()
