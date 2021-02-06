def solution(board):
    # 가로 세로 길이 부터 구함
    hight = len(board)
    width = len(board[0])
    
    for i in range(1, hight):
        for j in range(1, width):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) +1

    return max([num for row in board for num in row])**2 # 최대 값 반환















