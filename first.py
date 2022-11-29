from random import randint

n = int(input("Введите количество элементов для списка: "))
arr = [0] * n
k0 = 0
k1 = 0
for i in range(n):
    arr[i] = randint(0, 1)
    if (arr[i] == 0):
        k0 += 1
    else:
        k1 += 1
print(arr)
print("Вероятность 0 =", k0 / n)
print("Вероятность 1 =", k1 / n)
sum = 0
kol = n + 1
for j in range(2, n):
    kol = kol - 1
    b0 = 0
    b1 = 0
    sum = 0
    for l in range(n - j):
        sum = 0
        for p in range(l, l + j):
            sum += arr[p]
        if sum == 0:
            b0 += 1
        elif sum == j:
            b1 += 1

    lis = '0' * j
    bis = '1' * j
    if ( b0==0 and b1==0 ):
        break
    if (b0!=0):
        print("Вероятность", lis, "=", b0 / kol)
    if (b1!=0):
        print("Вероятность", bis, "=", b1 / kol)