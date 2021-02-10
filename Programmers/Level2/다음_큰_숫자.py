def solution(n):
#     bin을 사용할 경우 앞에 0b가 붙기 때문에 [2:]을 해준다
    b = str(bin(n))[2:]
    
    # 2진수에서 1갯수 카운터 하기
    for i in range(n, 1000000):
        i += 1
        if str(bin(i)[2:]).count('1') == str(bin(n)[2:]).count('1') :
               return i
