import sys
cnt = int(input())
# 메모리 초과 대비
num_list = [0 for _ in range(10000)]

for _ in range(cnt):
    num_list[(int(sys.stdin.readline()))-1] += 1


for idx in range(len(num_list)):
    if num_list[idx] > 0:
        sys.stdout.write((str(idx+1) +'\n')*num_list[idx])