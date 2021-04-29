""" 해설 참고
https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A8%EC%96%B4-%EB%B3%80%ED%99%98-DFS-BFS-Python
"""


def solution(begin, target, words):
    cnt = 0
    queue = [begin]

    while True:
        tmp = []

        for word in queue:
            if word == target:
                return cnt

            for idx in range(len(words)-1, -1, -1):
                word2 = words[idx]
                dif = sum(x != y for x, y in zip(word, word2))
                if dif == 1:
                    tmp.append(words.pop(idx))

        if not tmp:
            return 0
        queue = tmp
        cnt += 1
