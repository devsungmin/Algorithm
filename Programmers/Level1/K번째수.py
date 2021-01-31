def solution(array, commands):
    result = []
    # num = sorted(array[commands[0][0]-1:commands[0][1]])
    # print(num)
    # print(num[commands[0][2]-1])
    
    for i,j,k in commands:
        result.append(sorted(array[i-1:j])[k-1])
        
    return result
