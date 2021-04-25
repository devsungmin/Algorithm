def check(left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def palindrome(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if check(left + 1, right) or check(left, right - 1):
                return 1
            return 2
    return 0


t = int(input())

for _ in range(t):
    word = list(input())
    print(palindrome(word, 0, len(word) - 1))
