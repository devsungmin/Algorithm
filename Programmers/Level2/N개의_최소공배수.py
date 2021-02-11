from math import gcd

# 최소 공배수 함수
def lcm(a,b):
    return a*b//gcd(a,b)

def solution(arr):
    while(True):
        arr.append(lcm(arr.pop(),arr.pop()))
        if len(arr) == 1:
            return arr[0]
