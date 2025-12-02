import math

class EngineeringCalculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Ошибка: Деление на ноль"
        return x / y

    def sin(self, degrees):
        radians = math.radians(degrees)
        return math.sin(radians)

    def cos(self, degrees):
        radians = math.radians(degrees)
        return math.cos(radians)

    def tan(self, degrees):
        radians = math.radians(degrees)
        return math.tan(radians)

    def log(self, x, base=10):
        if x <= 0:
            return "Ошибка: Логарифм отрицательного числа"
        return math.log(x, base)

    def power(self, base, exponent):
        return math.pow(base, exponent)


calc = EngineeringCalculator()


while True:
    try:
        user_input = input().strip()

        if user_input.lower() == 'exit':
            break

        if not user_input:
            continue

        parts = user_input.split()

        if len(parts) == 3:  # Бинарные операции
            try:
                a = float(parts[0])
                op = parts[1].lower()
                b = float(parts[2])

                if op == '+':
                    result = calc.add(a, b)
                elif op == '-':
                    result = calc.subtract(a, b)
                elif op == '*':
                    result = calc.multiply(a, b)
                elif op == '/':
                    result = calc.divide(a, b)
                elif op == 'power' or op == '^':
                    result = calc.power(a, b)
                else:
                    print(f"Неизвестная операция: {op}")
                    continue

                print(f"= {result}")

            except ValueError:
                print("Ошибка: введите числа корректно!")

        elif len(parts) == 2:  # Унарные операции
            try:
                func = parts[0].lower()
                a = float(parts[1])

                if func == 'sin':
                    result = calc.sin(a)
                elif func == 'cos':
                    result = calc.cos(a)
                elif func == 'tan':
                    result = calc.tan(a)
                elif func == 'log':
                    result = calc.log(a)
                else:
                    print(f"Неизвестная функция: {func}")
                    continue

                print(f"= {result}")

            except ValueError:
                print("Ошибка: введите число корректно!")

        else:
            print("Неправильный формат! Примеры:")
            print("  5 + 3")
            print("  sin 30")
            print("  2 power 3")

    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем")
        break
    except Exception as e:
        print(f"Ошибка: {e}")