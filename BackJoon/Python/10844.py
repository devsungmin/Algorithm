"""
점화식 유추를 위해 https://youtu.be/nwqOSTa2c58 강의 참고
"""

import sys

n = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(n)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#  점화식: dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1]
for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# 1,000,000,000으로 나눈 나머지 값 출력
print(sum(dp[n-1]) % 1000000000)
