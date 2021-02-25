import heapq

def solution(n, works):
    heap = []
    result = 0
    # works의 총 합이 n보다 작은 경우 0을 반환
    if n >= sum(works):
        return 0
    
    for i in works:
        heapq.heappush(heap, (-i, i))
    
    for _ in range(n):
        do_work = heapq.heappop(heap)
        value = do_work[1] -1
        heapq.heappush(heap, (-value, value))
    
    works = [pow(num[1],2) for num in heap]
    
    return sum(works)
