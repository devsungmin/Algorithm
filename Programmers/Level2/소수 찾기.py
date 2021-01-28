# 순열을 사용하기 위해 import 해줌
from itertools import permutations

# 소수 구분 함수
def prime_number(num):
    if num <= 1:
        return False
    else:
        for j in range(2, num):
            if num % j == 0:
                return False
    return True

def solution(numbers):
    cnt_prime = []
    cnt = []
    for i in range(len(numbers)):
        cnt_prime.append(numbers[i])

    for j in range(1,len(cnt_prime)+1):
        answer = set(list(permutations(cnt_prime, j)))
        
        for k in answer:
            if prime_number(int(''.join(k))):
                cnt.append(int(''.join(k)))
                
    return len(set(cnt))

# 테스트 코드
# print(solution("17"))
# print(solution("001"))