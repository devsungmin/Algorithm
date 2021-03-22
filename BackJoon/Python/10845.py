import sys


def push(n):
    queue.append(n)


def queue_pop():
    if queue:
        return queue.pop(0)
    else:
        return -1


def size():
    return len(queue)


def empty():
    if not queue:
        return 1
    else:
        return 0


def front():
    if not queue:
        return -1
    else:
        return queue[0]


def back():
    if not queue:
        return -1
    else:
        return queue[-1]


cnt = int(input())


queue = []

for _ in range(cnt):
    input_comm = sys.stdin.readline().rstrip().split()

    command = input_comm[0]

    if command == "push":
        push(input_comm[1])
    elif command == "pop":
        print(queue_pop())
    elif command == "size":
        print(size())
    elif command == "empty":
        print(empty())
    elif command == "front":
        print(front())
    elif command == "back":
        print(back())
