"""
참고 자료
https://lily.sunmoon.ac.kr/MainPortal.aspx#
"""

def solution(N, number):
    cnt = -1
    dp = []
    
    for i in range(1, 9):
        num = { int(str(N) * i) }
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j -1]:
                    num.add(x + y)
                    num.add(x - y)
                    num.add(x * y)
                    
                    if y != 0:
                        num.add(x // y)
        if number in num:
            return i
        
        dp.append(num)
    return cnt
