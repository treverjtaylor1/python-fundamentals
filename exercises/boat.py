class feet:

    def __init__(self, length1):
        self._length = length1

    def get_length(self):
        return self._length

    def set_length(self, value):
        self._length = value

    def del_length(self):
        del self._length

    length = property(get_length, set_length, del_length)
measure = feet(10)
print(measure._length, 'feet long')

class width:

    def __init__(self, width1):
        self._width = width1

    def get_width(self):
        return self._width

    def set_width(self, value2):
        self._width = value2

    def del_width(self):
        del self._width

    width = property(get_width, set_width, del_width)

measure1 = width(7)
print(measure1.width, 'feet wide')

class speed:
    def __init__(self, speed1):
        self._speed = speed1

    def get_speed(self):
        return self._speed

    def set_speed(self, value3):
        self._speed = value3

    def del_speed(self):
        del self._speed

measure2 = speed(40)
print(measure2._speed, 'mph top speed')





