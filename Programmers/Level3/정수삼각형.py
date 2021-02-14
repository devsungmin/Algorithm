# dp을 사용하여 문제 풀이
# 대각선 방향으로만 이동이 가능 => v[row][col] += max(v[row-1][col-1], v[row-1][col])을 사용
def solution(triangle):
    for row in range(1, len(triangle)):
        for col in range(row + 1):
            if col == 0:
                triangle[row][col] += triangle[row-1][col]
            elif col == row:
                triangle[row][col] += triangle[row-1][-1]
            else:
                triangle[row][col] += max(triangle[row-1][col-1], triangle[row-1][col])
                
    return max(triangle[-1])
