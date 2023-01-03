class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        listed_dict = list(self.dictionary.items())
        if self.index < len(listed_dict):
            step = self.index
            self.index += 1
            return listed_dict[step]
        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
