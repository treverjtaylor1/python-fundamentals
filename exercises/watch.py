class finish:

    def __init__(self, finish1):
        self._finish = finish1

    def get_finish(self):
        return self._finish

    def set_finish(self, type):
        self._finish = type

    def del_finish(self):
        del self._finish

    finish = property(get_finish, set_finish, del_finish)
outer = finish('gold')
print(outer._finish)

class material:

    def __init__(self, material1):
        self._material = material1

    def get_material(self):
        return self._material

    def set_material(self, material):
        self._material = material

    def del_material(self):
        del self._material

    material = property(get_material, set_material, del_material)

inner = material('stainless steel')
print(inner._material)

class waterresistance:
    def __init__(self, water1):
        self._water = water1

    def get_water(self):
        return self._water

    def set_water(self, value):
        self._water = value

    def del_water(self):
        del self._water

    water = property(get_water, set_water, del_water)

resistance = water1(40)
print(resistance._water)