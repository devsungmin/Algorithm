# 우측의 표와 같이 자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후, 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다. 이 표에서는 10이 H-지수가 되는 것입니다. 다시 말하여, 이 연구원은 논문 인용횟수가 10이 넘는 논문이 적어도 10편이 된다는 것을 의미합니다.
# [0,0,0] 0인 경우를 다시 생각 할 것
def solution(citations):
    citations.sort()
    h_cnt = len(citations)
    
    for i in range(h_cnt):
        if citations[i] >= h_cnt-i: 
            return h_cnt-i
    return 0
