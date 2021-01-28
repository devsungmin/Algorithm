def solution(answers):
    student_answers = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]*2000, [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]*1250, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*10000]
    
    score_count = [0,0,0]
    
    for i in range(3):
        for j in range(len(answers)):
            if student_answers[i][j] == answers[j]:
                score_count[i] += 1
                
    # Return 값이 배열이기 때문에 max함수를 사용하여 append하여 return 해준다
    max_score = []
    for k in range(3):
        if score_count[k] == max(score_count):
            max_score.append(k+1)
    
    return max_score