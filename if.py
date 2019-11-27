number = int(input('Введите ваш возраст!'))
def age(number):
    if number <=6:
        return('Иди в детский сад!')
    elif 7 <= number <= 17:
        return('Иди в школу!')
    elif 18 <= number <= 22:
        return('Иди в ВУЗ!')
    else:
        return('Иди на завод!')
a = age(number)
print(a)




