def get_primes(numbers: list):
    for number in numbers:
        if number == 2:
            yield number
        for i in range(2, number):

            if number % i == 0:
                break
            else:
                yield number
                break



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))