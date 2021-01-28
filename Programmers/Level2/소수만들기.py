# 조합을 사용하기 위해 import
from itertools import combinations

# 소수 구분 함수
def prime_number(a, b, c):
    total_num = a + b + c
    if total_num <= 1:
        return False
    else:
        for j in range(2, total_num):
            if total_num % j == 0:
                return False
    return True

def solution(nums):
    cnt = 0
    # 3개의 수를 더하기
    num = list(combinations(nums, 3))
    
    for i in num:
        if prime_number(i[0], i[1], i[2]):
            cnt += 1
    return cnt