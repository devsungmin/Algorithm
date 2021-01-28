#모든 최대 가격 2000
b = 2000
d = 2000

# 버거 가격
for i in range(3) :
    a = int(input())
    b = min(b,a)

# 음료 가격
for i in range(2) :
    c = int(input())
    d = min(d,c)

print(b+d-50)