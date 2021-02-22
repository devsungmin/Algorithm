def solution(s):
    # 모든 문자를 소문자로 변환 
    s = list(s.lower())
    
    # 첫번째 문자가 숫자인지 알파벳인지 구분
    if s[0].isalpha() == True:
        s[0] = s[0].upper()
        
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            s[i]=s[i].upper()
    
    s = ''.join(s)
    
    return s
