def fibonacci():
    f1 = 0
    f2 = 1
    yield f1
    yield f2
    f_1 = f2
    f_2 = f1

    while True:
        fn = f_1 + f_2
        yield fn
        f_2 = f_1
        f_1 = fn


generator = fibonacci()
for i in range(5):
    print(next(generator))
