# 테스트는 통과 했지만 효율성 문제로 불통과한 코드
def solution(n, works):
    result = 0
    pow_list = []
    # works의 총 합이 n보다 작은 경우 0을 반환
    if n >= sum(works):
        return 0
    
    # 일을 골고루 분활하고 n번 진행 함
    # 일을 할때 마다 1을 빼줌
    for _ in range(n):
        works.sort()
        works[-1] -= 1
    
    # 각 항을 제곱하여 list 추가
    for i in works:
        pow_list.append(pow(i,2))
    
    # list의 합을 반환
    return sum(pow_list)
