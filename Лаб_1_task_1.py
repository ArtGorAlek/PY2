from typing import Union
import doctest

class Car:
    """
            Создание объекта "Машина"
            :param name: Название машины
            :param power: Мощность двигателя машины
            :param speed: Скорость машины
            Пример:
            >>> BMW = Car('BMW', 1000, 100)
            """
    def __init__(self, name: str, power: Union[int, float], speed: int):

        if not isinstance(name, str):
            raise TypeError
        self.name = name

        if not isinstance(power, (int, float)):
            raise TypeError
        if not power > 0:
            raise ValueError
        self.power = power

        if not isinstance(speed, int):
            raise TypeError
        self.speed = speed

    def change_speed(self, speed: int) -> None:
        """
        Функция ускорения машины, изменяет текущую скорость
        :param speed: Текущая скорость
        Пример:
        >>> Honda = Car('Honda', 1100, 60)
        >>> Honda.change_speed(60)
        """
        if not isinstance(speed, int):
            raise TypeError("Скорость машины должна быть типа int")
        self.speed += speed

class Vector:
    """
            Создание объекта "вектор"
            :param name: название вектора
            :param x_coordinate: координата по оси х
            :param y_coordinate: координата по оси у
            :param z_coordinate: координата по оси я
            Пример:
            >>> vector_B = Vector('magnetic induction', 5, 4, -5)
            """
    def __init__(self, name: str, x_coordinate: int, y_coordinate: int, z_coordinate: int):

        if not isinstance(name, str):
            raise TypeError
        self.name = name

        if not isinstance(x_coordinate, int):
            raise TypeError
        self.x_coordinate = x_coordinate

        if not isinstance(y_coordinate, int):
            raise TypeError
        self.x_coordinate = y_coordinate

        if not isinstance(z_coordinate, int):
            raise TypeError
        self.x_coordinate = z_coordinate

    def change_vector(self, x_coordinate: int, y_coordinate: int, z_coordinate: int) -> None:
        """
        Функция изменения координат вектора, изменяет координаты вектора
        :param x_coordinate: Новая х коорданата
        :param y_coordinate: Новая y коорданата
        :param z_coordinate: Новая z коорданата
        Пример:
        >>> vector_V = Vector('velocity vector', 10, -3, 0)
        >>> vector_V.change_vector(4, 0, 0)
        """
        if not isinstance(x_coordinate, int):
            raise TypeError("Координата х должна быть типа int")
        if not isinstance(y_coordinate, int):
            raise TypeError("Координата у должна быть типа int")
        if not isinstance(z_coordinate, int):
            raise TypeError("Координата z должна быть типа int")

        ...

class Figures:
    """
            Создание объекта "Фигуры"
            :param name: Название фигуры
            :param color: Цвет
            :param volume: объем
            :param position: место хранения
            Пример:
            >>> ball = Figures('sphere','red', 15, 'cabinet')
            """
    def __init__(self, name: str, color: str, volume: int, position: str):

        if not isinstance(name, str):
            raise TypeError
        self.name = name

        if not isinstance(color, str):
            raise TypeError
        self.color = color

        if not isinstance(volume, int):
            raise TypeError
        if not volume > 0:
            raise ValueError
        self.volume = volume

        if not isinstance(position, str):
            raise TypeError
        self.position = position

    def change_place(self, position: str) -> None:
        """
        Функция перестановки фигуры
        :param position: Новое местоположение
        Пример:
        >>> Toy = Figures('cube', 'green', 6, 'garden')
        >>> Toy.change_place('cupboard')
        """
        if not isinstance(position, str):
            raise TypeError(f"Местоположение фигуры должно быть типа str, а не {type(position)}")
        ...

if __name__ == "__main__":
    doctest.testmod()

