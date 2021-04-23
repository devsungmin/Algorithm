""" 풀이 참고
https://infinitt.tistory.com/213
"""
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

result = []
idx = 0

for i in range(n):
    idx += k - 1
    if idx >= len(arr):
        idx = idx % len(arr)

    result.append(str(arr.pop(idx)))

print("<", ", ".join(result)[:], ">", sep='')
