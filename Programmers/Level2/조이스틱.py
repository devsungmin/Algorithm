# https://jgrammer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1 참고
# 문자의 아스키 값을 돌려주는 함수인 ord()함수를 사용
# min(ord(name[idx])-ord('A'),(ord('Z')-ord(name[idx])+1) 수식을 사용
def solution(name):
    idx,cnt = 0,0
    name = [min(ord(i)-ord('A'),(ord('Z')-ord(i)+1)) for i in name]

    while True:
        cnt += name[idx]
        name[idx] = 0

        if sum(name) == 0:
            break

        left, right = 1, 1
        while name[idx - left] == 0:
            left += 1

        while name[idx + right] == 0:
            right += 1

        cnt += left if left < right else right
        idx += -left if left < right else right

    return cnt
