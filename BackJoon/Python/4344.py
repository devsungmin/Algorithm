cnt = int(input()) # 프로그램 반복 횟수

for i in range(cnt) :
    student = list(map(int, input().split()))
    avg = sum(student[1:])/student[0]
    rank = 0
    for j in student[1:] : #student[0]의 경우 과목 갯수가 들어가므로 [1:]을 사용한다.
        if j > avg :
            rank += 1
    print('%.3f' % round(rank /student[0] * 100, 3) + '%')