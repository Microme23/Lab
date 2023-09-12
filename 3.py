N = int(input("Введіть ціле число від 1 до 9: "))
while (N < 1 or N > 9):
    N = int(input("Введіть ціле число від 1 до 9: "))
for i in range(1, N+1):
    num = i
    for j in range(1,N+1):
        if j < i:
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num += 1
    print("")