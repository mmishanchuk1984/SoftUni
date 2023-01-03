def make_bold(f):
    def wrapper(*args):
        return f"<b>{f(*args)}</b>"
    return wrapper


def make_italic(f):
    def wrapper(*args):
        return f"<i>{f(*args)}</i>"
    return wrapper


def make_underline(f):
    def wrapper(*args):
        return f"<u>{f(*args)}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
