def solution(n):
    cnt = 0
    
    for i in range(1, n+1, 1):
        sum_num = 0
        for j in range(i, n+1):
            sum_num += j
            if sum_num == n:
                cnt += 1
                break
            if sum_num >= n:
                break
    return cnt
