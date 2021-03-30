import sys

hight = int(sys.stdin.readline())
triangle = []

for _ in range(hight):
    triangle.append(list(map(int, sys.stdin.readline().split())))

k = 2

# 점화식: dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
for i in range(1, hight):
    for j in range(k):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif i == j:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = max(triangle[i-1][j-1],
                                 triangle[i-1][j]) + triangle[i][j]
    k += 1
print(max(triangle[hight-1]))
