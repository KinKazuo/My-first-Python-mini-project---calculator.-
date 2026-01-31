a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

op = input("Введите операцию (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Неизвестная операция")
