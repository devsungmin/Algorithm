# 이 문제는 input대신 sys.stdin.readline을 사용하는것이 중요한 문제이다.
import sys

num = int(input())

for i in range(num) :
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
