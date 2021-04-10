import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

# 입력 받는 모든 문자는 대문자로 취급
input_str = sys.stdin.readline().upper()

for i in range(len(input_str)):
    for j in dial:
        if input_str[i] in j:
            time += dial.index(j) + 3

print(time)
