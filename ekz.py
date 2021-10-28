# 1 Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

# def card():
#     num = str(input("Enter a number by card "))
#     for i in num:
#         return("X" * (len(num)-4) + num[-5:-1])
#
#
# print(card())


# 2 Напишите функцию, которая проверяет: является ли слово палиндромом

# def poli():
#     word = str(input("Enter your word: "))
#     if word == word[::-1]:
#         return("YES")
#     else:
#         return("NO")
#
# print(poli())

# 3
class Tomato:

    def init(self, index):
        self._index = index
        self._state = 0


#     #Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
    def grow(self, st):
        if st == 1:
            print("the first stage of grow")
        elif st == 2:
            print("the second stage of grow")
        elif st == 3:
            print("the third stage of grow")
        else:
            print("the stage incorrect")

# #Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
    def is_ripe(self, st):
        if st == 3:
            print("the tomato is ripe")

# Создайте класс TomatoBush
class TomatoBush(Tomato):

    def __init__(self, num):
        super().init()
        self.numbers = num
        print(f'Number of tomato is {self.numbers}%')

#  Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
    def grow_all(self, stages):
        if stages == 1:
            print("the first stage of grow")
        elif stages == 2:
            print("the second stage of grow")
        elif stages == 3:
            print("the third stage of grow")
        else:
            print("the stage incorrect")

#Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
#списка стали спелыми
    def all_are_ripe(self):
        self.ripe = True
