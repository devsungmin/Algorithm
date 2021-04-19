import sys

n = int(sys.stdin.readline())
if n ** 0.5 % 1 != 0:
    result = int(n**0.5) + 1
else:
    result = int(n**0.5)
print(result)
