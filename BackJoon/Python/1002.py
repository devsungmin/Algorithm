import math
cnt = int(input())

while cnt:
    cnt -= 1
    location = list(map(int, input().split()))
    x1 = location[0]
    y1 = location[1]
    r1 = location[2]
    x2 = location[3]
    y2 = location[4]
    r2 = location[5]

    distance = math.sqrt((x1-x2) ** 2 + (y1- y2) ** 2) # 원의 방정식 -> 두 원의 거리 구하는 공식 사용
    
    # 반지름이 같은 때 / 두 원이 동심원인 경우
    if distance == 0 and r1 == r2:
        print(-1)
    # 내접, 외 접일 때
    elif abs(r1- r2) == distance or r1 + r2 == distance:
        print(1)
    # 두원이 서로 다른 두점에서 만날때
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0) 