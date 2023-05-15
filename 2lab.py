def z1():
    password = input('Введите пароль')
    is_upper = False
    is_numeric = False
    is_lower = False
    is_spec = False
    for char in password:
        if char.isnumeric():
            is_numeric = True
        elif char.islower():
            is_lower = True
        elif char.isupper():
            is_upper = True
        elif char in "@#%&":
            is_spec = True
    if len(password) > 4 and is_numeric and is_upper and is_lower and is_spec:
        print('Пароль: проверка пройдена')
    else:
        print('Пароль: проверка НЕ пройдена')


def z2():
    print('Доступны 3 цвета: красный, желтый, синий')
    a, b = input(), input()
    if a != 'красный' and a != 'желтый' and a != 'синий':
        print('Ошибка цвета')
    elif b != 'красный' and b != 'желтый' and b != 'синий':
        print('Ошибка цвета')
    elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
        print('Оранжевый')
    elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
        print('Зелёный')
    elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
        print('Фиолетовый')
    elif a == 'красный' and b == 'красный':
        print('красный')
    elif a == 'желтый' and b == 'желтый':
        print('желтый')
    elif a == 'синий' and b == 'синий':
        print('синий')


def z3():
    print('Определение года')
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Год', year, 'Високосный')
    else:
        print('Год', year, 'Не Високосный')


z1()
z2()
z3()