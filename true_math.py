# В true_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)


def divide(first, second):
    from math import inf
    if second == 0:
        return inf
    else:
        return (first / second)
