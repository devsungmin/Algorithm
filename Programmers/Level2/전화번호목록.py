def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 같은 값이 들어 있는 경우 False값을 return
        if phone_book[i] in phone_book[i+1]:
            return False
    return True
