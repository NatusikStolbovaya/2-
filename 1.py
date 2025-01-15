# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Window:
    def init(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        self.width = width
        self.height = height

    def open(self) -> None:
        """
        Открыть окно.
        :return: None
        """
        ...

    def close(self) -> None:
        """
        Закрыть окно.
        :return: None
        """
        ...

    def clean(self) -> None:
        """
        Очистить стекло окна.
        :return: None
        """
        ...

class Wardrobe:
    def init(self, shelves: int, material: str):
        if shelves <= 0:
            raise ValueError("The number of shelves must be a positive integer.")
        if not material:
            raise ValueError("Material must be specified.")
        self.shelves = shelves
        self.material = material

    def open_door(self) -> None:
        """
        Открыть дверцы шкафа.
        :return: None
        """
        ...

    def close_door(self) -> None:
        """
        Закрыть дверцы шкафа.
        :return: None
        """
        ...

    def organize_items(self) -> None:
        """
        Организовать предметы на полках шкафа.
        :return: None
        """
        ...

class Wind:
    def init(self, speed: float, direction: str):
        if speed < 0:
            raise ValueError("Speed cannot be negative.")
        if not direction:
            raise ValueError("Direction must be specified.")
        self.speed = speed
        self.direction = direction

    def change_direction(self, new_direction: str) -> None:
        """
        Изменить направление ветра.

        :param new_direction: Новое направление ветра.
        :type new_direction: str
        :return: None

        Пример:
        >>> wind = Wind(10.5, "north")
        >>> wind.change_direction("south")
        """
        ...

    def increase_speed(self, increment: float) -> None:
        """
        Увеличить скорость ветра.

        :param increment: Величина увеличения скорости.
        :type increment: float
        :return: None

        Пример:
        >>> wind = Wind(10.5, "north")
        >>> wind.increase_speed(5.0)
        """
        ...

    def decrease_speed(self, decrement: float) -> None:
        """
        Уменьшить скорость ветра.

        :param decrement: Величина уменьшения скорости.
        :type decrement: float
        :return: None

        Пример:
        >>> wind = Wind(10.5, "north")
        >>> wind.decrease_speed(3.0)
        """
        ...
if name == "main":
    doctest.testmod()  # тестирование примеров, которые находятся в документации



