'''
Задание 2.
Функции, методы, тайпинги.
'''


# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def string_behind(text: str):
    return (text[::-1])


# Реализовать фунекцию, которая принимает два параметра: число и степень - и возвращает это число,
# возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.
def multiply_numbers(number: int, mupltiply: int):
    if mupltiply is None:
        return number ** 2
    return number ** mupltiply


# Реализовать функцию, которая принимает произвольный набор параметров и возвращает кортеж, содержащий
# типы переданных параметров.
def type_of_value(*args) -> tuple:
    a = []
    for i in args:
        a.append(type(i))
    return a


# Реализовать функцию, которая принимает произвольный набор именованных параметров и возвращает их
# группировку по типу в виде словаря.
# Например, если входные параметры заданы как `a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0`,
# то необходимо вернуть словарь следующего вида:
# {
#   int: [['a', 34], ['c', 2]],
#   str: [['b', 'some text']],
#   float: [['d', 1.3], ['f', -3.0]],
#   dict: [['e', {1: 2}]]
# }
def group_value(**kwargs):
    result = {}
    for key, val in kwargs.items():
        if result.get(type(val)):
            result[type(val).__name__].append([key, val])
        else:
            result[type(val).__name__] = [key, val]
    return result

# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.
import re

def foo(value, *args, **kwargs):
    final_string = value.replace("**", "*")
    list_string = final_string.split()

    for name in list_string:
        if re.match("\*(-?)\d+\*", name):
            final_string = final_string.replace(name, str(args[int(name.strip("*"))]))
        if re.match("\*[A-z]+\*", name):
            final_string = final_string.replace(name, str(kwargs[name.strip("*")]))

    return final_string
