import sys

pay_money = 1000 - int(sys.stdin.readline())
changes = [500, 100, 50, 10, 5, 1]
result = 0

for i in changes:
    result += pay_money // i
    pay_money %= i

print(result)
