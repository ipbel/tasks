'''
Задание 3.
Классы. Наследование, волшебные методы.
'''


# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами
# измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.
# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения,
# например "1 км", "2.35 мили" и т. д.
# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.
# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве
# аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число,
# то оно трактуется, как количество текущих единиц измерения.
# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.
# Требуется реализовать методы __div__ и __idiv__, принимающиwе как числовое значение, так и любой класс
# единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат
# возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.
# Требуется добавить способ конвертации из одной системы единиц в другую (желательно с использованием
# __init__.
# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут
# приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность
# реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит
# для этого.


class LengthUnits:
    def __init__(self, value, convert, default_union, default_num=1):
        self.value = value
        self.convert = convert
        self.default_union = default_union
        self.default_num = default_num

    def __eq__(self, other):
        return self.default_num == other.default_num

    def __lt__(self, other):
        return self.default_num < other.default_num

    def __add__(self, other):
        if type(other) in {float, int}:
            return f'{self.value.__add__(other)} {self.default_union}'
        return f'{self.default_num.__add__(other.default_num)} м'

    def __iadd__(self, other):
        if type(other) in {float, int}:
            self.value += other
            return f'{self.value} {self.default_union}'
        else:
            self.default_num += other.default_num
            return f'{self.default_num} м'

    def __sub__(self, other):
        if type(other) in {float, int}:
            return f'{self.value.__sub__(other)} {self.default_union}'
        return f'{self.default_num.__sub__(other.default_num)} м'

    def __isub__(self, other):
        if type(other) in {float, int}:
            self.value -= other
            return f'{self.value} {self.default_union}'
        else:
            self.default_num -= other.default_num
            return f'{self.default_num} м'

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return f'{self.value.__mul__(other)} {self.default_union}'
        raise TypeError('Takes only number of arguments')

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.value *= other
            return f'{self.value} {self.default_union}'
        raise TypeError('Takes only number of arguments')

    # Нашел что в py3 вместо __div__ есть __floordiv__(//) деление без остатка
    def __floordiv__(self, other):
        if type(other) in {float, int}:
            return f'{self.value.__floordiv__(other)} {self.default_union}'
        return f'{self.default_num.__floordiv__(other.default_num)} м'

    def __idiv__(self, other):
        if type(other) in {float, int}:
            self.value /= other
            return f'{self.value} {self.default_union}'
        else:
            self.default_num /= other.default_num
            return f'{self.default_num} м'


class Millimeters(LengthUnits):

    def __init__(self, default_num, convert=1000):
        super(Millimeters, self).__init__(default_num, convert, default_union='мм')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class Centimeters(LengthUnits):
    def __init__(self, default_num, convert=100):
        super(Centimeters, self).__init__(default_num, convert, default_union='cm')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class Meters(LengthUnits):
    def __init__(self, default_num, convert=1):
        super(Meters, self).__init__(default_num, convert, default_union='м')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class Kilometers(LengthUnits):

    def __init__(self, default_num, convert=0.001):
        super(Kilometers, self).__init__(default_num, convert, default_union='km')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class Inches(LengthUnits):

    def __init__(self, default_num, convert=39.37):
        super(Inches, self).__init__(default_num, convert, default_union='inc')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


#
class Feets(LengthUnits):

    def __init__(self, default_num, convert=3.28):
        super(Feets, self).__init__(default_num, convert, default_union='feets')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class Yards(LengthUnits):

    def __init__(self, default_num, convert=1.09):
        super(Yards, self).__init__(default_num, convert, default_union='ya')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class Miles(LengthUnits):

    def __init__(self, default_num, convert=0.00062):
        super(Miles, self).__init__(default_num, convert, default_union='mi')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class Fen(LengthUnits):

    def __init__(self, default_num, convert=269.179004):
        super(Fen, self).__init__(default_num, convert, default_union='fen')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class Chi(LengthUnits):

    def __init__(self, default_num, convert=3.0003):
        super(Chi, self).__init__(default_num, convert, default_union='chi')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'


class In(LengthUnits):

    def __init__(self, default_num, convert=0.03125):
        super(In, self).__init__(default_num, convert, default_union='in')
        self.default_num = self.value / convert
        self.convert = convert

    def __str__(self):
        return f'{self.value} {self.default_union}'
