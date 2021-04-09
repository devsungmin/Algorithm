import sys

k = int(sys.stdin.readline())
nums = []

for _ in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        nums.append(num)
    else:
        del nums[-1]

print(sum(nums))
