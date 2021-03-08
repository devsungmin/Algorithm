# set()을 사용하면 중복된 글자는 제거 되기 때문에 사용 하면 안됨
def solution(str1, str2):
    # 대소문자 구분 없이 다 대문자로 변환 후 list로 저장
    # 두글자씩 끊어서 읽는다
    str1 = [str1[i:i+2].upper() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].upper() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
    if len(str1) == 0 and len(str2) == 0: return 1 * 65536
    
    # 교집합
    inter = sum([min(str1.count(i), str2.count(i)) for i in set(str1) & set(str2)])
    # 합집합
    union = sum([max(str1.count(i), str2.count(i)) for i in set(str1) | set(str2)])
    
    result = inter / union
    
    return  int(result * 65536)
