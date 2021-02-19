def solution(brown, yellow):
    carpet = brown + yellow
    
    # 가로 값
    for width in range(carpet, 2, -1):
        if carpet % width == 0:
            # 세로 값
            length = carpet // width
            if yellow == (width-2)*(length-2):
                return [width, length]
