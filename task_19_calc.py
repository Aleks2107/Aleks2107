# Простейший калькулятор c введёнными двумя числами вещественного типа. 
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.  
# Обработать ошибку: “Деление на ноль” 
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def calc(a, b):
    symb = input("Enter operation: ")
    if symb == "+":
        return a + b
    elif symb == "-":
        return a - b
    elif symb == "/":
        return a / b
    elif symb == "*":
        return a * b

try:
    print(calc(2.5, 2))

except ZeroDivisionError:
    pass