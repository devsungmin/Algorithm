weight = int(input()) # n의 무게
box_cnt = 0 #박스 갯수

while True :
    if weight%5 == 0 : # 5kg그램의 박스를 카운터 해주기 위해 if문을 사용하여 구분
        box_cnt += weight/5
        print(int(box_cnt))
        break

    weight = weight - 3 # 5로 나누어 떨어지지 않을 경우 3kg짜리 봉투를 사용하여야 하기 때문에 -3을 해줘서 5에 나누어 떨어지도록 함
    box_cnt += 1 # 파이썬은 증감연산자가 없기 때문에 이렇게 표시한다. / 위의 연산에서 3을 빼주었기 때문에 3kg짜리 봉투를 사용하기 때문에 카운터에 1을 더해줌

    if weight < 0 :
        print("-1")
        break