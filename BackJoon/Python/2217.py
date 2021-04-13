import sys

n = int(sys.stdin.readline())
result = 0
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

for i in range(n):
    tmp = arr[i] * (i+1)
    if tmp > result:
        result = tmp
print(result)
