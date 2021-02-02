# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Heap을 사용
import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville) # 힙 생성
    
    while scoville:
        one = heapq.heappop(scoville) # 첫번째에 있는 원소
        
        if one >= K:
            break
        elif len(scoville) <= 0:
            return -1
        else:
            two = heapq.heappop(scoville) # 두번째에 있던 원소
            heapq.heappush(scoville, one + two * 2)
            cnt += 1
            
    return cnt
