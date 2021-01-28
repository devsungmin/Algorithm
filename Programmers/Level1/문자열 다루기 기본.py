def solution(s):
    
    # isdigit()을 사용하여 숫자인지 문자인지를 구분한다.
    # s의 길이가 4혹은 6인지 구별을먼저 한다.
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False