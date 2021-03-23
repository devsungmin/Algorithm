import sys


def stack_sequence(n, sequence):
    stack = []
    num = 1
    idx = 0
    op = []

    while True:
        if len(stack) == 0:
            stack.append(num)
            op.append('+')
            num += 1

        elif sequence[idx] == stack[-1]:
            stack.pop()
            op.append('-')
            idx += 1
            if idx == n:
                break
        else:
            if n < num:
                print("NO")
                break
            stack.append(num)
            op.append('+')
            num += 1

    if len(stack) == 0:
        for o in op:
            print(o)


sequence = []
n = int(sys.stdin.readline())
for _ in range(n):
    sequence.append(int(sys.stdin.readline()))
stack_sequence(n, sequence)
