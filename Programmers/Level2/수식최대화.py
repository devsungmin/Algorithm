"""
참고 자료
https://velog.io/@tjdud0123/%EC%88%98%EC%8B%9D-%EC%B5%9C%EB%8C%80%ED%99%94-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%AC%B8%EC%A0%9C
"""

from itertools import permutations
import re

def solution(expression):
    # 정규식을 이용하여 비숫자 문자를 찾음
    operation = set(re.findall("\D", expression))
    prior = permutations(operation)
    cand = []

    for op_cand in prior:
        tmp = re.compile("(\D)").split('' + expression)
        for exp in op_cand:
            while exp in tmp:
                idx = tmp.index(exp)
                tmp = tmp[:idx-1] + [str(eval(''.join(tmp[idx-1:idx+2])))] + tmp[idx+2:]
        cand.append(abs(int(tmp[0])))
    return max(cand)