import sys


def star_function(star):
    matrix = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:
            matrix.append(star[i % len(star)] + " " *
                          len(star) + star[i % len(star)])
        else:
            matrix.append(star[i % len(star)] * 3)
    return(list(matrix))


star = ["***", "* *", "***"]
n = int(sys.stdin.readline())
cnt = 0
while n != 3:
    n = int(n / 3)
    cnt += 1

for i in range(cnt):
    star = star_function(star)
for i in star:
    print(i)
