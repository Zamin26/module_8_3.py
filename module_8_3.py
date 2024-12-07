class IncorrectVinNumber(Exception):                                # Класс исключений
    def __init__(self, message, ):
        self.message = message                                      # вывод сообщения


class IncorrectCarNumbers(Exception):                               # Класс исключений
    def __init__(self, message):
        self.message = message                                      # вывод сообщения



class Car:
    def __init__(self, model, vin, numbers):            # создание класса с атрибутами
        self.model = model                              # название автомобиля, приватный уровень
        self.__vin = vin                                # vin номер автомобиля, приватный уровень
        self.__numbers = numbers                        # номер автомобиля
        self.__is_valid_vin(vin)                        # подходящий vin номер автомобиля
        self.__is_valid_numbers(numbers)                # подходящий номер автомобиля

    def __is_valid_vin(self, vin_number):               # принимает vin_number и проверяет его на корректность
        if not isinstance(vin_number, int):                                     # условие
            raise IncorrectVinNumber('Некорректный тип vin номер')              # исключение
        else:
            if not 1000000 <= vin_number <= 9999999:                            # условие
                raise IncorrectVinNumber('Неверный диапазон для vin номера')    # исключение
            return True

    def __is_valid_numbers(self, numbers):                  # принимает numbers и проверяет его на корректность
        if not isinstance(numbers, str):                                        # условие
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')    # исключение
        else:
            if not len(numbers) == 6:                                           # условие
                raise IncorrectCarNumbers('Неверная длина номера')              # исключение
            return True


# Примеры

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')