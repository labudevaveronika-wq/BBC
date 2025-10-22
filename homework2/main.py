def Level1(level):
    metod = str(input("Введите метод (): "))
    text = str(input("Введике текст: "))
    if metod == "upper":
        return text.upper()
    if metod == "lower":
        return text.lower()
    if metod == "capitalize":
        return text.capitalize()
def Level2(level):
    metod = str(input("Введите метод (): "))
    text = str(input("Введите текст: "))
    if metod == "find":
        pod_text = str(input("Введите подстроку: "))
        return text.find(pod_text)
    if metod == "replace":
        zamena_1 = str(input("Введите то, что хотите заменить: "))
        zamena_2 = str(input("Введите то, на что хотите заменить: "))
        return text.replace(zamena_1, zamena_2)
    if metod == "count":
        simbol = str(input("Введите то, что хотите посчитать: "))
        return text.count(simbol)
def Level3(level):
    metod = str(input("Введите метод (): "))
    text = str(input("Введите текст: "))
    if metod == "split":
        simbol = str(input("Введите символ: "))
        return text.split(simbol)
    if metod == "join":
        simbol = str(input("Введите символ: "))
        return simbol.join(text)
def Level4(level):
    metod = str(input("Введите метод (): "))
    text = str(input("Введите текст: "))
    if metod == "isdigit":
        if text.isdigit(): return "Ура, строка состоит только из цифр"
        else: return 0
    if metod == "isalpha":
        if text.isdigit(): return "Ура, строка состоит только из букв"
        else: return 0
    if metod == "strip":
        simbol = str(input("Введите символ: "))
        return text.strip(simbol)
def Level5(level):
    metod = str(input("Введите метод (): "))
    text = str(input("Введите текст: "))
    if metod == "isdigit":
        if text.isdigit(): return "Ура, строка состоит только из цифр"
        else: return 0
    if metod == "isalpha":
        if text.isdigit(): return "Ура, строка состоит только из букв"
        else: return 0
    if metod == "strip":
        simbol = str(input("Введите символ: "))
        return text.strip(simbol)

level = int(input("Введите номер уровня: "))
if level == 1:
    print(Level1(level))
if level == 2:
    print(Level2(level))
if level == 3:
    print(Level3(level))
if level == 4:
    print(Level4(level))
