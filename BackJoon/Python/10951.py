# 이 문제는 문제상으로 봤을 경우 무한 반복하는 문제이지만 예외처리를 안해줄 경우 런타임 에러가 발생함 
import sys

while True :
    try :
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    except :
        break