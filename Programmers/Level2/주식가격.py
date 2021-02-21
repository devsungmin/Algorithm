def solution(prices):
    stack = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i]<= prices[j]:
                stack[i] += 1
            else:
                stack[i]+= 1
                break
                
    return stack
