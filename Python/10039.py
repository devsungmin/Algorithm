score = []
avg = 0
for i in range(5) :
    score_num = int(input())
    # 40점 이상은 자신의 점수를 받아감
    if score_num>=40 :
        score.append(score_num)
    else : # 40점 미만의 점수는 40점으로 측정함
        score.append(40)


print(int(sum(score)/5)) # 평균은 항상 정수이기 때문에 int형으로 출력