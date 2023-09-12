N = 30
S = 0
kil = 0
for i in range(1, N+1):
    S = (S + 1/i)
    kil += 1
print("Результат обчислень\nS: ",S, "\nКількість членів ряду: ",kil)
