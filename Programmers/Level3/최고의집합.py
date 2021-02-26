# 최고의 집합 => s/2한 값을 이용함
def solution(n, s):
    answer = []
    # divmod을 사용하여 몫과 나머지를 구함
    share, remainder = divmod(s, n)
    
    if n > s:
        return [-1]
    
    for i in range(n):
        answer.append(share)
    
    for i in range(remainder):
        idx = len(answer) - 1 - i
        answer[idx] = answer[idx] + 1
        
    return answer
