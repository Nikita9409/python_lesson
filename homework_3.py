# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.



def div():
    try:
        arg1 = int(input("Первое число:"))
        arg2 = int(input("Второе число:"))
    except ValueError:
        return
    except ZeroDivisionError:
        return
    if arg2 == 0:
        print ("Ошибка! Деление на ноль невозможно.")
    else:
        return arg1 / arg2



print (f'Результат = {div()}')



# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def info(name, surname, year, city, email, telephone):
    print(f'{name} {surname} {year} {city} {email} {telephone}')


print(info(input('Имя -'), input('Фамилия -'), input('Год рождения -'), input('Город проживания -'),  input('email -'), input('Телефон -')))


# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    return(sum(total))

print(f'Результат = {my_func(5, -9, 3)}')



# Программа принимает действительное положительное число x
# и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.

# Способ решения без **

def my_fun(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(my_fun(float(input("х = ")), int(input("y = "))))


# Способ решения с **

def my_fun(x, y):
    return  x ** abs(y)
print(my_fun(float(input("х = ")), int(input("y = "))))


# Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
# после этого завершить программу.

def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел или нажмите Q - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма ровна = {sum_res}')
    print(f'Итоговая сумма ровна = {sum_res}')


my_sum()


# Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total


print(my_func(input("Введите строку -")))

