import sys

n = int(sys.stdin.readline())
jan = [0]

for _ in range(n):
    jan.append(int(sys.stdin.readline()))

dp = [0]
dp.append(jan[1])

if n > 1:
    dp.append(jan[1] + jan[2])
    for i in range(3, n+1):
        result = max(dp[i-3]+jan[i-1]+jan[i], dp[i-2]+jan[i], dp[i-1])
        dp.append(result)

print(dp[n])
