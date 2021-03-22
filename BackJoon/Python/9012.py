cnt = int(input())

for _ in range(cnt):
    ps = list(input())

    left, right = 0, 0

    for i in ps:
        if i == '(':
            left += 1
        elif i == ')':
            right -= 1

        if left + right < 0:
            print('NO')
            break

    if left + right > 0:
        print('NO')
    elif left + right == 0:
        print('YES')
