import sys

cnt = int(sys.stdin.readline())
score = []
jump = []

for i in range(0, cnt):
    score.append(int(sys.stdin.readline()))


# 점화식: dp[i] = max(dp[i-2] + score[i], dp[i-3]+score[i-1]+score[i])

if cnt == 1:
    print(score[0])
elif cnt == 2:
    print(score[cnt-1] + score[cnt-2])
else:
    jump.append(score[0])
    jump.append(jump[0] + score[1])
    jump.append(max(jump[0] + score[2], score[2] + score[1]))

    for i in range(3, cnt):
        jump.append(max(score[i] + score[i-1] +
                        jump[i-3], score[i] + jump[i-2]))

    print(jump[-1])
