# 10872번 팩토리얼 문제는 재귀 형태를 사용해서 풀이를 해서 성공함
def factorial(input_cnt) :
    if input_cnt < 1 :
        return 1
    return input_cnt * factorial(input_cnt-1)

def main() :
    input_cnt = int(input())
    print(factorial(input_cnt))

if __name__ == "__main__":
    main()