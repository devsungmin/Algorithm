def solution(priorities, location):
    queue = []
    idx = [i for i in range(len(priorities))]
    
    while priorities:
        # 최고 순위인경우
        if priorities[0] == max(priorities):
            queue.append(idx.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))
        
    return queue.index(location)+1
