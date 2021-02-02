# 정규식 사용
import re

def solution(files):
    result = []
    fileName = []
    
    for i in files:
        fileName.append(re.split(r"([0-9]+)", i)) # 정규식을 사용하여 숫자를 기준으로 자름
    result = sorted(fileName, key = lambda x : (x[0].lower(),int(x[1]))) # 0번 소문자로 바꾸고 1번 숫자를 key로 잡음 -> 테스트2 기준 lambda 값은 ('f-', 5)값을 가짐

    
    return ["".join(j) for j in result]
