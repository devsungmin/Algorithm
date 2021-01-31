def solution(n):
    zero = 0
    one = 1
    
    for i in range(n-1):
        fibo_n = zero + one
        zero = one
        one = fibo_n
    
    return one % 1234567
