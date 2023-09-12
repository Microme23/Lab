a = int(input("Введіть а: "))
while (a < 1 or a > 100):
    a = int(input("Введіть а: "))

b = int(input("Введіть b: "))
while (b < 1 or b > 100):
    b = int(input("Введіть b ще раз: "))

if a > b:
    X = (a/b+1)
elif a==b:
    X = -2
else:
    X = ((a-b)/a)
print("Результат очислення виразу: ", X)