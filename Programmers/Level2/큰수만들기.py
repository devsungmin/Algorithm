def solution(number, k):
    stack = []
    
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue
            
        check = False
        
        while stack and int(stack[-1]) < int(number[i]):
            stack.pop()
            k -= 1
            if not k:
                check = True
                stack += number[i:]
                break
                
        if check:
            break
        stack.append(number[i])
        
    return "".join(stack[:len(number)- k]) if k else "".join(stack)
