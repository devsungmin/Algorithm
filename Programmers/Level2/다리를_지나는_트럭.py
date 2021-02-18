'''
=== 페이지 참고===
https://velog.io/@devjuun_s/%EB%8B%A4%EB%A6%AC%EB%A5%BC-%EC%A7%80%EB%82%98%EB%8A%94-%ED%8A%B8%EB%9F%AD-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4
'''

def solution(bridge_length, weight, truck_weights):
    time = 0
    # 다리 길이 만큼 0으로 queue을 채움
    queue = [0] * bridge_length
    
    while len(queue):
        time += 1
        queue.pop(0)
        
        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
        
    return time
