# 윤년인 경우 1년이 366일
# a: 1~12 b: 1~31
def solution(a, b):
    # 1월 1일 시작이 금요일
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    moonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    result = sum(moonth[:a-1]) + b-1
    
    return day[result % 7]
