def solution(a):
    cnt = 2
    
    if len(a)<= 2:
        return len(a)
    
    left = a[0]
    right = a[-1]
    
    for i in range(1, len(a)-1):
        if left > a[i]:
            left = a[i]
            cnt += 1
        if right > a[-1-i]:
            right = a[-1-i]
            cnt += 1
    
    if left == right:
        return cnt - 1
    else:
        return cnt
