class Car:

    def __init__(self, model, vin, numbers):
        self.model = str(model)
        self.__vin = int(vin)
        self.__numbers = str(numbers)
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)
        if self.__is_valid_vin(vin) == True and self.__is_valid_numbers(numbers) == True:
            print(f' {self.model} успешно создана')

    # @property
    # def vin(self):
    #     return self.__vin
    #
    # @vin_chek.setter
    # def vin(self, vin):
    #     if self.__is_valid_vin(vin):  # если метод проверки True
    #         self.__vin = vin
    #         return self.__vin


    def __is_valid_vin(self, vin_number):
        if type_vin(vin_number) and range_vin(vin_number):
            return True

    def __is_valid_numbers(self, car_number):
        if type_numbers(car_number) and range_numbers(car_number):
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def type_vin(vin):
    if isinstance(vin, int) == False:
        raise IncorrectVinNumber('Некорректный тип vin номера', vin)
        return False
    else:
        return True

def range_vin(vin):
    if vin < 1000000 or vin > 9999999:
        raise IncorrectVinNumber('Неверный диапазон для vin номера', vin)
        return False
    else:
        return True

class IncorrectCarNumbers(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def type_numbers(numbers):
    if isinstance(numbers, str) == False:
        raise IncorrectVinNumber('Некорректный тип данных для номеров', numbers)
        return False
    else:
        return True

def range_numbers(numbers):
    if len(numbers) != 6:
        raise IncorrectVinNumber('Неверная длина номера', numbers)
        return False
    else:
        return True

try:
    first = Car('Model1', 1000000, 'f123dj')
    second = Car('Model2', 300, 'т001тр')
    third = Car('Model3', 2020202, 'нет номера')

except IncorrectVinNumber as exc:
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Дополнительная информация: {exc.extra_info}')