"""
{}으로 되어 있는 것을 list형태로 변경
"""

def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key = lambda x: len(x))
    
    for i in s:
        sp_i = i.split(',')
        
        for j in sp_i:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer
