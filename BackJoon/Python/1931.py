import sys

n = int(sys.stdin.readline())
conference_time = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    conference_time.append([start, end])

conference_time = sorted(conference_time, key=lambda x: (x[1], x[0]))

last = 0
cnt = 0

for i, j in conference_time:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
