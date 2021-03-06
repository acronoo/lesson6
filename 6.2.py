"""
2. Реализовать класс Road (дорога),
в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length: int
    _width: int
    _mass_asphalt = 25  # масса асфальта для покрытия одного кв метра дороги
    _thickness = 5  # толщина полотна

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        x = self._length * self._width * Road._mass_asphalt * Road._thickness
        return x


new_road = Road(10000, 20)
print(f"{new_road.mass_calc()} кг")
print(f"{new_road.mass_calc() / 1000} т")
