""" 풀이 참고
https://jeongminhee99.tistory.com/91
"""

import sys 

t = int(sys.stdin.readline())
fibo = [0, 1]

# 문제에서 n의 값을 1,000,000,000으로 제한을 했기 때문에 피보나치 수열을 47까지 사용한다
for i in range(2, 47):
    fibo.append(fibo[i-2] + fibo[i-1])

for j in range(t):
    n = int(sys.stdin.readline())
    n_list = []

    for k in range(len(fibo) - 1, 0, -1):
        if fibo[k] > n:
            continue
        
        n -= fibo[k]
        n_list.append(fibo[k])
    n_list.sort()


    for i in n_list:
        print(i, end = ' ')
    print()
