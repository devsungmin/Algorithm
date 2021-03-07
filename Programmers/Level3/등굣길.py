"""
참고 자료
https://codingspooning.tistory.com/80
"""

def solution(m, n, puddles):
    result = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    result[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                result[i][j] = 0
            else:
                result[i][j] += result[i-1][j] + result[i][j-1]
    
    return result[-1][-1] % 1000000007
