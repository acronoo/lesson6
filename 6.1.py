"""
1. Создать класс TrafficLight (светофор)
и определить у него один атрибут color (цвет)
и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class TrafficLight:
    __color = ""

    def running(self):
        self.__color = "Красный"
        print(self.__color)
        for i in range(7):
            print(f"Осталось {7 - i}")
            time.sleep(1)
        self.__color = "Жёлтый"
        print(self.__color)
        for i in range(2):
            print(f"Осталось {2 - i}")
            time.sleep(1)
        self.__color = "Зелёный"
        print(self.__color)


light = TrafficLight()
light.running()

