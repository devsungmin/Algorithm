def fibo(n):
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    elif n == 2:
        print(1, 1)
    else:
        tmp = 0
        current = 1
        before = 0
        for j in range(n - 1):
            tmp = current
            current = before + tmp
            before = tmp

        print(before, current)


num = int(input())

for _ in range(num):
    num1 = int(input())
    fibo(num1)
