# B팀이 최대한 많이 이기기 위해선 A팀이 가진 숫자와 차이가 많이 나지 않게 하여 높은 수를 아끼는것이 가장 좋은 방법

def solution(A, B):
    score = 0
    A.sort()
    B.sort()
    
    while A and B:
        if B[-1]>A[-1]:
            score += 1
            B.pop()
        A.pop()
    
    return score
