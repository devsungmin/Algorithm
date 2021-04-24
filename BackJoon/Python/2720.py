t = int(input())


for _ in range(t):
    c = int(input())
    c_25 = c//25
    c %= 25
    c_10 = c//10
    c %= 10
    c_5 = c // 5
    c %= 5
    print("%d %d %d %d " % (c_25, c_10, c_5, c))
