import collections
input_str = list(input().upper())
cnt_str = collections.Counter(input_str)
cnt_max = []
for i, j in cnt_str.items():
    if j == max(cnt_str.values()):
        cnt_max.append(i)
        if len(cnt_max) > 1:
            print('?')
            break
if len(cnt_max) == 1:
    print(cnt_max[0])