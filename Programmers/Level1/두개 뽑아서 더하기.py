def solution(numbers):
    result = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            num = numbers[i] + numbers[j]
            result.append(num)
            result_number = set(result)
    
    return sorted(result_number)