import sys

# 점화식 : dp[N] = dp[N-1] + dp[N-2]

n = int(sys.stdin.readline())
dp = [0, 1, 2]

for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])


print(dp[n] % 10007)
