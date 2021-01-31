# 다시 한번 풀어 보기!!
# lambda식을 사용 할 것!
# x*3을 사용하는 이유는 numbers의 조건이 1000이하이기 때문에 사용
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
