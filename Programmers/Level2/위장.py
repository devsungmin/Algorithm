# 경우의 수을 이용하여 풀이 진행
# 딕셔너리를 사용하여 종류별로 카운트를 진행
def solution(clothes):
    cnt = 1
    dic = {}
    for cloth in clothes:
        tmp = cloth[1]
        if dic.get(tmp):
            dic[tmp] += 1
        else:
            dic[tmp] = 2 # 의상을 선택하지 않은 경우
            
    for i in dic.values():
        cnt *= i
    return cnt-1 # 하나도 착용 안한 경우를 생각하여 -1을 해줌
