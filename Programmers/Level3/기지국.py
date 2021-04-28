# 기지국 설치 최대 영역 (2 * w + 1)
def solution(n, stations, w):
    answer = 0
    idx = 0
    start = 1

    while start <= n:
        if idx < len(stations) and start >= stations[idx] - w:
            start = stations[idx] + w + 1
            idx += 1
        else:
            start += 2 * w + 1
            answer += 1
    return answer
