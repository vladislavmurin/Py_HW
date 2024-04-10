import math
from abc import ABC, abstractmethod
CM_TO_IN = 0.393701
PX_TO_IN = 0.010377

# HW2

# 1 - Case convertation.

def camel_case_to_snake_case3(line: str) -> str:
    result = []
    for idx, char in enumerate(line):
        if char.isupper() and idx:
            result.append("_")
        result.append(char.lower())
    return "".join(result)

# name, surname = map(str, full_name_str.split("_"))


# 2 - Repeats.

class Person:
    def __init__(self, name=None, surname=None):
        self._name = name
        self._surname = surname
        self._age = None

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_full_name(self): # getting name+surname
        return self.get_name() + ' ' + self.get_surname()

    def set_age(self, Age): # setting age
        self._age = Age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    #   self.fullname = name, surname
    @property
    def fullname(self):
        # return self._name + ' ' + self._surname
        return f"{self._name} {self._surname}"


# 3 - Non-abstract forms.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, side1=None, side2=None):
        self._side1 = side1
        self._side2 = side2

    @property
    def side1(self):
        return self._side1

    @property
    def side2(self):
        return self._side2

    def area(self):
        return self._side1 * self._side2

    def perimeter(self):
        return self._side1 + self._side2


class Circle(Shape):
    def __init__(self, rad=None):
        self._rad = rad

    def perimeter(self):
        return self._rad * 2 * math.pi

    def area(self):
        return math.pi * self._rad**2


# 4 - Sum mistake.

class SecretResultReached(ValueError):
    # def __init__(self, a=None, b=None):
    pass


def add(a1, b1):
    sum = a1 + b1
    if sum == 42:
        raise SecretResultReached('You found a secret result')
    return sum

try:
    add(20, 15)
except ValueError as be:
    pass
    assert isinstance(be, SecretResultReached)


# 5* - Screen resolution.

class Screen:
    def __init__(self, diagonal=None, pix_w=None, pix_h=None):
        self._diagonal = diagonal
        self._pix_w = pix_w
        self._pix_h = pix_h

        self._height = None
        self._width = None
        self._height_cm = None
        self._width_cm = None
        self._area = None
        self._area_cm = None
        self._aspect_ratio = None

    @property
    def aspect_ratio(self):   #AR = width / height
        self._aspect_ratio = self._pix_w / self._pix_h
        return self._aspect_ratio

    @property
    def height(self):
        self._height = self._pix_h * PX_TO_IN
        return self._height

    @property
    def width(self):
        self._width = self._pix_w * PX_TO_IN
        return self._width

    @property
    def height_cm(self):
        self._height_cm = self.height / CM_TO_IN
        return self._height_cm


    @property
    def width_cm(self):
        self._width_cm = self.width / CM_TO_IN
        return self._width_cm

    @property
    def area(self):
        self._area = self.height * self.width
        return self._area

    @property
    def area_cm(self):
        self._area_cm = self.height_cm * self.width_cm
        return self._area_cm


# 6* - Valid staples.

def valid_p(line: str):
    temp_list = []
    open_p = ['(', '{', '[']
    closed_p = [')', '}', ']']
    for symbol in line:
        if symbol in open_p:
            temp_list.append(symbol)
        if symbol in closed_p:
            if closed_p.index(symbol) == open_p.index(temp_list[-1]):
                temp_list.pop()
            else:
                return False
    return False if len(temp_list) != 0 else True


if __name__ == '__main__':
    # 1
    # print(camel_case_to_snake_case3("AnnieIsGreatMentor"))

    # 2
    bb2 = Person('Sam', 'Lake')
    # print(bb2.fullname)
    # print(type(bb2))
    bb = Person('Sam', 'Lake')
    bb.set_age(20)
    # print(bb._age)
    # print(bb.get_name(), bb.get_surname(), bb.get_full_name())
    new_bb = Person(surname='Anderson')
    new_bb.set_age(80)
    # print(new_bb.fullname)
    # noviy_bb.fullname = 'bobbbb', 'biiibbb'
    new_bb.name = 'Tom'
    # print(new_bb.fullname)

    # 3
    rectangle = Rectangle(4, 6)
    rectangle.area()
    # print(rectangle.area())
    rectangle.perimeter()
    # print(rectangle.perimeter())

    circle = Circle(30)
    a = circle.area()
    # print(a)
    b = circle.perimeter()
    # print(b)

    # 4
    add(40, 2)

    # 5
    diagonaly = 17
    pix_wi = 1980
    pix_hi = 720
    dwh = Screen(diagonaly, pix_wi, pix_hi)

    # print(dwh.aspect_ratio)
    # print(dwh._aspect_ratio)
    # print(dwh.width_cm)
    # print(dwh.height_cm)
    # print(dwh.width)
    # print(dwh.height)
    # print(dwh.area)
    # print(dwh.area_cm)

    # 6
    staples = '{ } ( ) [ { } ]'
    bb3 = valid_p(staples)
    # print(bb3)