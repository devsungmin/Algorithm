"""
참고 자료
https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EC%BF%BC%EB%93%9C%EC%95%95%EC%B6%95-%ED%9B%84-%EA%B0%9C%EC%88%98-%EC%84%B8%EA%B8%B0
"""

def check(s):
    if len(s) == 1:
        return s[0][0]
    
    tmp = [[] for _ in range(len(s)//2)]
    
    for i in range(1, len(s), 2):
        for j in range(1, len(s), 2):
            cnt0 = s[i][j][0] + s[i][j-1][0] + s[i-1][j][0] + s[i-1][j-1][0]
            cnt1 = s[i][j][1] + s[i][j-1][1] + s[i-1][j][1] + s[i-1][j-1][1]
            
            if cnt1 == 0: cnt0 = 1
            if cnt0 == 0: cnt1 = 1
                
            tmp[i//2].append([cnt0, cnt1])
            
    return check(tmp)
    

def solution(arr):
    answer = [[] for _ in range(len(arr)//2)]
    
    for i in range(1, len(arr), 2):
        for j in range(1, len(arr), 2):
            tmp = [arr[i][j], arr[i][j-1], arr[i-1][j], arr[i-1][j-1]]
            cnt1 = tmp.count(1)
            cnt0 = tmp.count(0)
            
            if cnt1 == 0: cnt0 = 1
            if cnt0 == 0: cnt1 = 1
                
            answer[i//2].append([cnt0, cnt1])
    
    return check(answer)
