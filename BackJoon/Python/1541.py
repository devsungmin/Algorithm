import sys
input = sys.stdin.readline()

# -을 기준을 split()
a = input.split('-')
num = []

for i in a:
    cnt = 0
    # +을 기준으로 split()
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)
