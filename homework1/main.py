'''import math
import operator
class CalculatorERROR(Exception):
    pass

class Engineering_calculator:
    def __init__(self):
        self.history = []
        self.operators = {"+": operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow}
        self.math = {"sin": math.sin, "cos": math.cos, "tg": math.tan, "sqrt": math.sqrt, "abs": math.fabs, "!": math.factorial}
    def proverka_na_chislo(self, number):
        if isinstance(number, int) == True or isinstance(number, float) == True:
            return number
        else:
            raise CalculatorERROR("Введенное значение не является числом.")
    def add(self, num1, num2):
        self.proverka_na_chislo(num1)
        self.proverka_na_chislo(num2)
        summ = self.operators["+"](num1, num2)
        self.history.append(f"{num1} + {num2} = {summ}")
        return summ
    def sub(self, num1, num2):
        self.proverka_na_chislo(num1)
        self.proverka_na_chislo(num2)
        raznost = self.operators["-"](num1, num2)
        self.history.append(f"{num1} - {num2} = {raznost}")
        return raznost
    def mul(self, num1, num2):
        self.proverka_na_chislo(num1)
        self.proverka_na_chislo(num2)
        proizvedenie = self.operators["*"](num1, num2)
        self.history.append(f"{num1} * {num2} = {proizvedenie}")
        return proizvedenie
    def truediv(self, num1, num2):
        self.proverka_na_chislo(num1)
        self.proverka_na_chislo(num2)
        if num2 == 0:
            raise CalculatorERROR("Деление на ноль невозможно.")
        delenie = self.operators["/"](num1, num2)
        self.history.append(f"{num1} / {num2} = {delenie}")
        return delenie
    def pow(self, num, x):
        self.proverka_na_chislo(num)
        stepen = self.operators["**"](num, x)
        self.history.append(f"{num} ** {x} = {stepen}")
        return stepen
    def sin(self, num):
        self.proverka_na_chislo(num)
        rad = math.radians(num)
        result = self.math["sin"](rad)
        self.history.append(f"sin({num}) = {result}")
        return result
    def cos(self, num):
        self.proverka_na_chislo(num)
        rad = math.radians(num)
        result = self.math["cos"](rad)
        self.history.append(f"cos({num}) = {result}")
        return result
    def tg(self, num):
        self.proverka_na_chislo(num)
        if num % 180 == 90: raise CalculatorERROR("Тангенс не определен для углов 90+180n, n принадлежащее R.")
        rad = math.radians(num)
        result = self.math["tg"](rad)
        self.history.append(f"tg({num}) = {result}")
        return result
    def sqrt(self, num):
        self.proverka_na_chislo(num)
        if num < 0: raise CalculatorERROR("Квадратный корень не определен для отрицательных чисел.")
        koren = self.math["sqrt"](num)
        self.history.append(f"sqrt({num}) = {koren}")
        return koren
    def factorial(self, num):
        self.proverka_na_chislo(num)
        if num < 0: raise CalculatorERROR("Факториал не определен для отрицательных чисел.")
        factorial = self.math["!"](num)
        self.history.append(f"{num}! = {factorial}")
        return factorial
    def abs(self, num):
        self.proverka_na_chislo(num)
        modul = self.math["abs"](num)
        self.history.append(f"abs({num}) = {modul}")
        return modul
    def get_history(self):
        if len(self.history) == 0: return "История операций пуста."
        return self.history
    def clear_history(self):
        self.history = []
        return "История операций была очищена."


def main():
    calculator = Engineering_calculator()
    print("Добро пожаловать в Инженерный Калькулятор!")
    while True:
        try:
            user = input("Введите операцию: ").lower()
            if user == "exit":
                print("До свидания!")
                break
            if user == "clear history":
                calculator.clear_history()
                continue
            if user == "get history":
                print(calculator.get_history())
                continue
            parts = user.split()
            if len(parts) == 0: continue'''

import math

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Ошибка: Деление на ноль!"
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def sqrt(self, x):
        if x < 0:
            return "Ошибка: Нельзя извлечь корень из отрицательного числа!"
        return math.sqrt(x)

    def sin(self, x):
        return math.sin(x)

    def cos(self, x):
        return math.cos(x)

    def tan(self, x):
        if math.cos(x) == 0:
            return "Ошибка: Тангенс не определен для данного угла!"
        return math.tan(x)
"""
    def log(self, x):
        if x <= 0:
            return "Ошибка: Логарифм определен только для положительных чисел!"
        return math.log(x)

    def log10(self, x):
        if x <= 0:
            return "Ошибка: Логарифм определен только для положительных чисел!"
        return math.log10(x)

    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            return "Ошибка: Факториал определен только для неотрицательных целых чисел!"
        return math.factorial(n)
"""
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Введите корректное число.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Введите корректное целое число.")

def display_menu():
    print("\n--- Инженерный Калькулятор ---")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (sqrt)")
    print("7. Синус (sin) (в радианах)")
    print("8. Косинус (cos) (в радианах)")
    print("9. Тангенс (tan) (в радианах)")
#    print("10. Натуральный логарифм (log)")
#    print("11. Десятичный логарифм (log10)")
#    print("12. Факториал (factorial)")
    print("0. Выход")
    print("-----------------------------")

def main():
    calc = Calculator()
    last_result = None

    while True:
        display_menu()
        choice = input("Выберите операцию (введите номер): ")

        if choice == '0':
            print("Выход из калькулятора. До свидания!")
            break

        result = None
        try:
            if choice in ('1', '2', '3', '4', '5'):
                num1 = get_float_input("Введите первое число: ")
                num2 = get_float_input("Введите второе число: ")

                if choice == '1':
                    result = calc.add(num1, num2)
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                elif choice == '4':
                    result = calc.divide(num1, num2)
                elif choice == '5':
                    result = calc.power(num1, num2)

            elif choice in ('6', '7', '8', '9', '10', '11'):
                num = get_float_input("Введите число: ")

                if choice == '6':
                    result = calc.sqrt(num)
                elif choice == '7':
                    print("Внимание: Угол должен быть в радианах.")
                    print("Если у вас градусы, введите 'degrees' или 'deg'.")
                    angle_unit = input("Введите 'rad' (радианы) или 'deg' (градусы): ").lower()
                    if angle_unit == 'deg':
                        num = math.radians(num)
                    result = calc.sin(num)
                elif choice == '8':
                    print("Внимание: Угол должен быть в радианах.")
                    print("Если у вас градусы, введите 'degrees' или 'deg'.")
                    angle_unit = input("Введите 'rad' (радианы) или 'deg' (градусы): ").lower()
                    if angle_unit == 'deg':
                        num = math.radians(num)
                    result = calc.cos(num)
                elif choice == '9':
                    print("Внимание: Угол должен быть в радианах.")
                    print("Если у вас градусы, введите 'degrees' или 'deg'.")
                    angle_unit = input("Введите 'rad' (радианы) или 'deg' (градусы): ").lower()
                    if angle_unit == 'deg':
                        num = math.radians(num)
                    result = calc.tan(num)
#                elif choice == '10':
#                    result = calc.log(num)
#                elif choice == '11':
#                    result = calc.log10(num)

            elif choice == '12':
                num = get_int_input("Введите неотрицательное целое число: ")
                result = calc.factorial(num)

            else:
                print("Некорректный ввод. Пожалуйста, выберите операцию из меню.")
                continue
            if  result is not None:
                print(f'Результат: {result}')
                last_result = result
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
            last_result = None



if __name__ == "__main__":
    main()




