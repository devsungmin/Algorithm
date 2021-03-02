def solution(n, times):
    left, right = 1, max(times) * n
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        do = 0
        for t in times:
            do += mid // t
            if do >= n:
                result = mid
                right = mid -1
                break
        if do < n:
            left = mid + 1
    return result
