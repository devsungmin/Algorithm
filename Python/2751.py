"""
문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성 하시오
입력 : 첫째 줄에 수의 갯수가 주어지고 둘째줄부터 N개의 수가 주어진다. 이 수는 절대 값이 1,000,000보다 작거나 같은 정수이고 중복되지 않는다.
출력 : 첫째 줄 부터 N개의 줄에 오른차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
def sorting_num(num_list):
  num_list = sorted(num_list)
  return num_list

def main():
  cnt_num = int(input())
  num_list = list()

  for _ in range(cnt_num) :
    num = int(input())
    num_list.append(num)

sorting_num(num_list)

if __name__ == "__main__":
    main()