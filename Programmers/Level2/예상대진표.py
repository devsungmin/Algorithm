# 항상 이긴다고 가정
def solution(n,a,b):
    cnt = 0
    while a!=b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        cnt += 1
    
    return cnt
