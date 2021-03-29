import sys

cnt = int(sys.stdin.readline())

# n = 1 / n = 2 / n = 3일때의 갯수
dp = [1, 2, 4]
input_list = []

for _ in range(cnt):
    input_list.append(int(sys.stdin.readline()))

# 3까지의 값이 있기 때문에 3부터 시작
for i in range(3, max(input_list)):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in input_list:
    print(dp[i-1])
