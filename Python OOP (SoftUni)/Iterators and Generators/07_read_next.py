def read_next(*args):
    for el in args:
        for i in el:
            yield i

for item in read_next('string', (2,)):
    print(item, end='')
