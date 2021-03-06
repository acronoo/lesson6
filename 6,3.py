"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income = {}

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


kassir = Position("vasya", "ivanov", 1000, 1200)
director = Position("petr", "smirnov", 4000, 5000)
print(kassir.get_full_name())
print(kassir.get_total_income())
print(director.get_full_name())
print(director.get_total_income())
