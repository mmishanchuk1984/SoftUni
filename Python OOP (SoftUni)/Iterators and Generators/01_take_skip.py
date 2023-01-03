class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.numbers = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.numbers < self.count:
            result = self.numbers
            self.numbers += 1
            return self.step * result
        else:
            raise StopIteration()




numbers = take_skip(2, 6)
for number in numbers:
    print(number)


