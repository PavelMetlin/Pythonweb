a = ""
b = int(input("Введите число: "))
while b != 0:
    a = str(b%2) + a
    b //=2
print(a)