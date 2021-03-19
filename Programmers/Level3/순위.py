def solution(n, results):
    cnt = 0
    win = {w: set() for w in range(1, n+1)}
    lose = {l: set() for l in range(1, n+1)}
    
    # 이긴 경우와 진 경우를 나누어 딕셔너리 형태로 저장
    for w, l in results:
        win[w].add(l)
        lose[l].add(w)
    
    # 반복 하여 돌면서 이긴 경우를 선별
    for i in range(1, n+1):
        for w in lose[i]:
            win[w].update(win[i])
        for l in win[i]:
            lose[l].update(lose[i])
    
    # win과 lose의 합이 n-1인 경우 순위를 확인함
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            cnt += 1
    
    return cnt
