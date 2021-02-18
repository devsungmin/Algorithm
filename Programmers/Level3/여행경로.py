# dictionary을 사용
def solution(tickets):
    dic = {}
    
    # dic = {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    for t in tickets:
        dic[t[0]] = dic.get(t[0], [])+[t[1]]
    for key in dic.keys():
        dic[key].sort(reverse = True)
        
    stack = ['ICN']
    result = []
    while stack:
        top = stack[-1]
        if top not in dic or len(dic[top]) == 0:
            result.append(stack.pop())
        else:
            stack.append(dic[top][-1])
            dic[top].pop()
            
    return result[::-1]
