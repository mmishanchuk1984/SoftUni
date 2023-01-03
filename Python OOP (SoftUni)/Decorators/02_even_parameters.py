def even_parameters(f):
    def wrapper(*args):
        for el in args:
            try:
                if el % 2 != 0:
                    return f"Please use only even numbers!"
            except:
                return f"Please use only even numbers!"

        return f(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(add(2, 4))
print(add("Peter", 1))

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
