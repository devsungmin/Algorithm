import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    word = str(input())
    word_len = len(word)
    words.append((word, word_len))

# set을 사용하여 중복된 문자열 제거
words = list(set(words))

words.sort(key = lambda word: (word[1], word[0]))

for w in words:
    print(w[0])
