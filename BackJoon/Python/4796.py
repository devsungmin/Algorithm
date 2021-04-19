import sys

case_cnt = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break

    result = (V//P)*L + min((V % P), L)

    print("Case %d: %d" % (case_cnt, result))
    case_cnt += 1
