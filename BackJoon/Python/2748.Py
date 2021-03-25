import sys

cnt = int(sys.stdin.readline())
fibo_list = [0 for _ in range(cnt+1)]
fibo_list[1] = 1

for i in range(2, cnt+1):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

print(fibo_list[-1])
