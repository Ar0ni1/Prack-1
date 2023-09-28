import math
def ar0ni1():
    while True:
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Нахождение квадратного корня")
        print("7. Нахождение факториала")
        print("8. Нахождение синуса")
        print("9. Нахождение косинуса")
        print("10. Нахождение тангенса")
        print("11. Выход из программы")

        usersvibor = input("Выберите действие\n")

        if usersvibor == "11":
            break

        if usersvibor in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
            try:
                PervoeChislo = int(input("Введите первое число: "))
                if usersvibor != "6" and usersvibor != "7" and usersvibor != "8" and usersvibor != "9" and usersvibor != "10":
                    VtoroeChislo = int(input("Введите второе число: "))
            except ValueError:
                print("Ошибка введенно не коректное число.")
                continue

            if usersvibor == "1":
                result = PervoeChislo + VtoroeChislo
            elif usersvibor == "2":
                result = PervoeChislo - VtoroeChislo
            elif usersvibor == "3":
                result = PervoeChislo * VtoroeChislo
            elif usersvibor == "4":
                if VtoroeChislo == 0:
                    print("на ноль делить можно, но нельзя возьми положительное число.")
                    continue
                result = PervoeChislo / VtoroeChislo
            elif usersvibor == "5":
                result = PervoeChislo * PervoeChislo
            elif usersvibor == "6":
                if PervoeChislo < 0:
                    print(" Не вариант так делать, попробуй взять положительное число.")
                    continue
                result = math.sqrt(PervoeChislo)
            elif usersvibor == "7":
                if PervoeChislo < 0:
                    print("Не вариант так делать, попробуй взять положительное число.")
                    continue
                result = math.factorial(int(PervoeChislo))
            elif usersvibor == "8":
                result = math.sin(PervoeChislo)
            elif usersvibor == "9":
                result = math.cos(PervoeChislo)
            elif usersvibor == "10":
                result = math.tan(PervoeChislo)

            print("Результат: ", result)

        else:
            print("Такой операции нет выбирите 1 из 10.")

ar0ni1()