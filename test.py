a = 1
while a == 1:
    try:
        num = int(input("Введите кол-во чисел: "))
        action = input("Выберите действие: +, -, *, /")
        result = 0
        if (action == "+"):
            for i in range(num):
                a = int(input(f'Введите число \n'))
                if (i == 0):
                    result = a
                else:
                    result += int(a)
                    print(result)
        elif (action == "-"):
            for i in range(num):
                a = int(input(f'Введите число \n'))
                if (i == 0):
                    result = a
                else:
                    result -= int(a)
                    print(result)
        elif (action == "*"):
            for i in range(num):
                a = int(input(f'Введите число \n'))
                if (i == 0):
                    result = a
                else:
                    result *= int(a)
                    print(result)
        elif (action == "/"):
            for i in range(num):
                a = int(input(f'Введите число \n'))
                if (i == 0):
                    result = a
                else:
                    result /= int(a)
                    print(result)
        else :
            print("Таких действий нет")
    except Exception as e:
        print(f"Ошибка" ,e)
