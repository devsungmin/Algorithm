import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

num_sum = 0
tmp = 0

for i in range(n):
    tmp += (num_sum + nums[i])
    num_sum += nums[i]

print(tmp)
