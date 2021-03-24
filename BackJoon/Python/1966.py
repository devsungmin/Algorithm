import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, m = list(map(int, sys.stdin.readline().split()))
    queue = list(map(int, sys.stdin.readline().split()))
    idx = list(range(len(queue)))

    idx[m] = 'target'

    cnt = 0

    while queue:
        if queue[0] == max(queue):
            cnt += 1

            if idx[0] == 'target':
                print(cnt)
                break
            else:
                idx.pop(0)
                queue.pop(0)
        else:
            idx.append(idx.pop(0))
            queue.append(queue.pop(0))
