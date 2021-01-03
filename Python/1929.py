"""
소수를 구하기에 가장 많이 알려진 방법중 하나인 에라토스테네스의 체 기법을 사용한다
에라토스테네스의 체 기법은 아래 링크를 통해 알 수 있다.
https://ko.wikipedia.org/wiki/에라토스테네스의_체
"""


def prime_num(m, n):
    primeNumber = [True]*(n+1)
    num = int((n+1)**0.5)

    for i in range(2, num+1):
        if primeNumber[i] == True:
            for j in range(i+i, n+1, i):
                primeNumber[j] = False

    result = [i for i in range(2, n+1) if primeNumber[i] == True]
    return result


def main():
    m, n = map(int, input().split())
    result = prime_num(m, n)

    for i in range(len(result)):
        if result[i] >= m:
            print(result[i])


if __name__ == "__main__":
    main()
