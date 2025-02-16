class Car:
    """
         Создание объекта "Автомобиль"

            :param brand: Бренд автомобиля
            :param color: Цвет автомобиля
            :param petrol: Количество бензина

            Пример:
            >>> car1 = Car("BMW", "красный", 3000)
    """

    def __init__(self, brand: str, color: str, petrol: int) -> None:
        self.brand = brand
        self.color = color
        self.petrol = petrol

    def __str__(self) -> str:
        return f"Марка автомобиля: {self.brand}. Цвет: {self.color}. Количество бензина: {self.petrol}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, color={self.color!r}, petrol={self.petrol})"

    def change(self, new_color: str) -> None:
        """
            Функция, которая меняет цвет машины

            :param new_color: Название нового цвета

            Пример:
            >>> car1 = Car("BMW", "красный", 3000)
            >>> car1.change("синий")
        """
        self.color = new_color

    def AddPetrol(self) -> None:
        """
            Функция, которая увеличивает количество бензина на 2000

            Пример:
            >>> car1 = Car("BMW", "красный", 3000)
            >>> car1.AddPetrol()
        """
        self.petrol += 2000

class PassengerCar(Car):
    """
         Создание объекта "Легковой автомобиль"

            :param brand: Бренд автомобиля
            :param color: Цвет автомобиля
            :param petrol: Количество бензина
            :param count_passenger: Количество пассажиров

            Пример:
            >>> car1 = PassengerCar("Kia", "жёлтый", 2500, 3)
    """
    def __init__(self, brand: str, color: str, petrol: int, count_passenger: int) -> None:
        super().__init__(brand, color, petrol)
        self.count_passenger = count_passenger

    def __str__(self) -> str:
        return f"Марка автомобиля: {self.brand}. Цвет: {self.color}. Количество бензина: {self.petrol}. Количество пассажиров: {self.count_passenger}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, color={self.color!r}, petrol={self.petrol}, count_passenger={self.count_passenger})"

    def change(self, new_color: str, new_count_passenger: int) -> None:
        """
            Функция, которая меняет цвет машины и количество пассажиров в ней

            :param new_color: Название нового цвета
            :param new_count_passenger: Новое количество пассажиров

            Данная функция была перезагружена из базового класса Car. Была добавлена возможность изменения количества пассажиров,
            т.к такой параметр появился в дочернем классе PassengerCar.

            Пример:
            >>> car1 = PassengerCar("Kia", "жёлтый", 2500, 3)
            >>> car1.change("синий", 1)
        """
        self.color = new_color
        self.count_passenger = new_count_passenger

    def AddPetrol(self) -> None:
        """
           Функция, которая увеличивает количество бензина на 2000

           Данная функция была унаследована из базового класса Car.

            Пример:
            >>> car1 = PassengerCar("Kia", "жёлтый", 2500, 3)
            >>> car1.AddPetrol()
        """
        super().AddPetrol()



