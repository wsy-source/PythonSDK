from typing import Callable


def setup(func: Callable) -> Callable:
    def wrap():
        print('*' * 20)
        func()
        print('*' * 20)

    return wrap


@setup
def demo():
    print('+' * 20)


demo()
