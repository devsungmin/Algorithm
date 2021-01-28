a,b,c = map(int, input().split()) #a = 고정 비용, b =  가변 비용
break_even_point = 0 # 순익 분익점

if(c <= b) :
    break_even_point = -1
else :
    break_even_point = a//(c-b)+1
print(break_even_point)