# https://codedrive.tistory.com/129 참고
# SJF 스케줄링 방법 사용
# 힙 사용
import heapq
def solution(jobs):
    start = -1
    now, time, cnt = 0, 0, 0
    wait = []
    
    while cnt < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(wait, [job[1],job[0]])
        if len(wait) > 0:
            current = heapq.heappop(wait)
            start = now
            now += current[0]
            time += (now - current[1])
            cnt += 1
        else:
            now += 1
    return time // len(jobs)
