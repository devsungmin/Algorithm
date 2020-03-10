# 3월 10일 작성본.. -> 미완성
#  피보나치 수열
def fibonacci(n) :
    if n == 0:
        print('0')
    elif n == 1:
        print('1')
    else:
        fibonacci(n-1) + fibonacci(n-2)
    return n

def main() :
    num = int(input())
    for i in range(num) :
        n = int(input())
        print(fibonacci(n))

if __name__ == "__main__":
    main()