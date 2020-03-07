cnt = int(input()) # 과목수 카운트
sum_score = 0
score = list(map(int, input().split())) #점수를 list형식으로 입력 받음
max_score = max(score) # 최대 점수

for i in range(cnt) :
    score[i] = score[i]/max_score*100
    sum_score += score[i]

avg_score = sum_score / cnt
print(avg_score)