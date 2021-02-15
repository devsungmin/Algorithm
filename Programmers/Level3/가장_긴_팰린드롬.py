def palindrome(s):
    return s == s[::-1]

def solution(s):
    cnt = 0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            if palindrome(s[i:j]):
                if cnt < len(s[i:j]):
                    cnt = len(s[i:j])
    return cnt
