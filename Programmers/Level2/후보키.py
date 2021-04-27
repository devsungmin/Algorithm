""" 풀이 참고
https://ljw538.tistory.com/73
"""
from itertools import combinations


def solution(relation):
    rows = len(relation)
    cols = len(relation[0])

    candidates = []
    final = []

    for i in range(1, cols+1):
        candidates.extend(combinations(range(cols), i))

    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == rows:
            final.append(keys)

    answer = set(final[:])

    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)
