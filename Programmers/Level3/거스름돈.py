# dp문제
# dp[y][x] = dp[y-1][x] + dp[y][x-money[y]]
def solution(n, money):
    dp = [[0]*(n+1) for _ in range(len(money))]
          
    for i in range(0, n+1, money[0]):
        dp[0][i] = 1
    
    for j in range(1, len(money)):
        for k in range(n+1):
            if k >= money[j]:
                dp[j][k] = (dp[j-1][k] + dp[j][k-money[j]]) % 1000000007
            else:
                dp[j][k] = dp[j-1][k]
    
    return dp[-1][-1]
