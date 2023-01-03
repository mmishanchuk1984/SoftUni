class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            i = self.counter
            self.counter += 1
            return self.sequence[i % len(self.sequence)]
        else:
            return StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


