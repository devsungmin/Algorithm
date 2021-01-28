a = int(input())
b = int(input())
c = int(input())

mul = list(str(a * b * c))

for i in range(10) :
    cnt = mul.count(str(i))
    print(cnt)