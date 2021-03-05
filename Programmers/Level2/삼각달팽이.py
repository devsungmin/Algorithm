"""
참고 자료
https://weejw.tistory.com/442
"""
from itertools import chain

def solution(n):
    maps = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, -1
    idx = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            maps[y][x] = idx
            idx += 1
    
    result = []
    for i in maps:
        for j in i:
            if j != 0:
                result.append(j)
    
    return result
