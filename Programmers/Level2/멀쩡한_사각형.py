# 최대 공약수을 활용
from math import gcd
def solution(w,h):
    return (w*h) - (w+h-gcd(w,h))