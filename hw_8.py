# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extr(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extr(self.day_month_year)}'


today = Data('20 - 12 - 2020')
print(today.valid(20, 12, 2020))
print(today.extr('20 - 12 - 2020'))

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivisionByZero:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def my_function(num_1, num_2):
        try:
            return (num_1 / num_2)
        except:
            return (f"Деление на ноль невозможно")



print(DivisionByZero.my_function(2, 0))


# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                yes_or_no = input(f'Попробовать еще раз? Y/N ')
                if yes_or_no == 'Y' or yes_or_no == 'y':
                    print(try_except.my_input())
                elif yes_or_no == 'N' or yes_or_no == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())


# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        ''' добавляем в словарь обьект по его названию, в значении
        будет список экземпляров этого оборудования'''
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        ''' извлекаем из значения обьект по названию группы.
        дальше можно расширить поиск по серии, марки или еще чему либо'''
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


class Xerox(Sklad):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)



sklad = Sklad()
scaner = Scaner('hp', '250', 19)
sklad.add_to(scaner)
scaner = Scaner('hp', '350', 20)
sklad.add_to(scaner)
printer = Printer('e-320', 'sony', 126, 2018)
sklad.add_to(printer)
print(sklad._dict)
sklad.extract('Scaner')
print()
print(sklad._dict)


# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, real):
        self.complex = complex(real)

    def __add__(self, other):
        if isinstance(other, Complex):
            other = other.complex

        complex_ = self.complex + other
        return Complex(complex_.real)

    def __mul__(self, other):
        if isinstance(other, Complex):
            other = other.complex

        complex_ = self.complex * other
        return Complex(complex_.real)

    def __str__(self):
        return self.complex.__str__()


if __name__ == '__main__':
    c1 = Complex(6)
    c2 = Complex(3)

    print(c1 + c2, complex(2, -3) + complex(5))
    print(c1 * c2, complex(2, -3) * complex(5))








