# 횟수는 n! -> n*(n-1) -> 팩토리얼을 사용해서 풀이
from math import factorial

def solution(n, k):
    result = []
    people = [i for i in range(1, n+1)]
    
    while n:
        ft = factorial(n-1)
        n -= 1
        idx, remainder = divmod(k, factorial(n))
        if remainder == 0:
            idx -= 1
            
        result.append(people[idx])
        people.remove(people[idx])
        
        k = remainder
        
    return result
