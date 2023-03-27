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
    UNITS = 'm'
    SCALE = 1.0

    def __init__(self, value):
        self.value = value * self.SCALE

    def __str__(self):
        return f'{self.value / self.SCALE} {self.UNITS}'

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __add__(self, other):
        if type(other) in {float, int}:
            return type(self)(self.value + other / self.SCALE)
        return type(self)(self.value + other.value)

    def __iadd__(self, other):
        if type(other) in {float, int}:
            self.value += other / self.SCALE
        self.value += other.value
        return self

    def __sub__(self, other):
        if type(other) in {float, int}:
            return type(self)(self.value - other / self.SCALE)
        return type(self)(self.value - other.value)

    def __isub__(self, other):
        if type(other) in {float, int}:
            self.value -= other / self.SCALE
        self.value -= other.value
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(self.value * other / self.SCALE)
        return type(self)(self.value * other.value)

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.value *= other / self.SCALE
        self.value *= other.value
        return self

    # Нашел что в py3 вместо __div__ есть __floordiv__(//) деление без остатка
    def __floordiv__(self, other):
        if type(other) in {float, int}:
            return type(self)(self.value / other / self.SCALE)
        return type(self)(self.value / other.value)

    def __idiv__(self, other):
        if type(other) in {float, int}:
            self.value /= other / self.SCALE
        self.value /= other.value
        return self


class Millimeters(LengthUnits):
    UNITS = 'mm'
    SCALE = 1000.0

    def __init__(self, value):
        super(Millimeters, self).__init__(value)


class Centimeters(LengthUnits):
    UNITS = 'cm'
    SCALE = 100.0

    def __init__(self, value):
        super(Centimeters, self).__init__(value)


class Meters(LengthUnits):
    UNITS = 'm'
    SCALE = 1.0

    def __init__(self, value):
        super(Meters, self).__init__(value)


class Kilometers(LengthUnits):
    UNITS = 'km'
    SCALE = 0.001

    def __init__(self, value):
        super(Kilometers, self).__init__(value)


class Inches(LengthUnits):
    UNITS = 'ich'
    SCALE = 39.37

    def __init__(self, value):
        super(Inches, self).__init__(value)


#
class Feets(LengthUnits):
    UNITS = 'fe'
    SCALE = 3.28

    def __init__(self, value):
        super(Feets, self).__init__(value)


class Yards(LengthUnits):
    UNITS = 'ya'
    SCALE = 1.09

    def __init__(self, value):
        super(Yards, self).__init__(value)


class Miles(LengthUnits):
    UNITS = 'mil'
    SCALE = 0.00062

    def __init__(self, value):
        super(Miles, self).__init__(value)


class Fen(LengthUnits):
    UNITS = 'fen'
    SCALE = 269.179004

    def __init__(self, value):
        super(Fen, self).__init__(value)


class Chi(LengthUnits):
    UNITS = 'chi'
    SCALE = 3.0003

    def __init__(self, value):
        super(Chi, self).__init__(value)


class In(LengthUnits):
    UNITS = 'in'
    SCALE = 0.03125

    def __init__(self, value):
        super(In, self).__init__(value)
