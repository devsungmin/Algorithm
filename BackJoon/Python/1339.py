n = int(input())
words = []

# 각 문자별 곱해야하는 수를 딕셔너리화 하여 계산
alpha_dic = {}


for _ in range(n):
    words.append(input())

for word in words:
    i = len(word) - 1
    for j in word:
        if j in alpha_dic:
            alpha_dic[j] += pow(10, i)
        else:
            alpha_dic[j] = pow(10, i)
        i -= 1

nums = []

for v in alpha_dic.values():
    nums.append(v)

nums.sort(reverse=True)

result, t = 0, 9

for i in range(len(nums)):
    result += nums[i] * t
    t -= 1
print(result)
