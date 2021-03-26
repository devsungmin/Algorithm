num = input()

# 입력한 수 쪼개기
num = [int(n) for n in num]

# 내림 차순으로 정렬
nums = sorted(num, reverse=True)

for n in nums:
    print(n, end = "")
