import sys


def push(n):
    stack.append(n)


def pop():
    if not stack:
        return -1
    else:
        return stack.pop()


def stack_size():
    return len(stack)


def empty():
    if stack:
        return 0
    else:
        return 1


def top():
    if stack:
        return stack[-1]
    else:
        return -1


cnt = int(input())

stack = []

for _ in range(cnt):
    input_comm = sys.stdin.readline().rstrip().split()

    command = input_comm[0]

    if command == "push":
        push(input_comm[1])
    elif command == "pop":
        print(pop())
    elif command == "size":
        print(stack_size())
    elif command == "empty":
        print(empty())
    elif command == "top":
        print(top())
