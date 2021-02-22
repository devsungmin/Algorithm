def solution(people, limit):
    people.sort()
    cnt = len(people)
    start, end = 0, len(people)-1
    
    while start < end:
        if people[start] + people[end] <= limit:
            cnt -= 1
            start += 1
            end -= 1
        else:
            end -= 1
            
    return cnt
