t = int(input())

# A, B, C에 지정된 시간은 각각 300초, 60초, 10초
a_time = 300
b_time = 60
c_time = 10

if t % 10 != 0:
    print(-1)
else:
    a = t // a_time
    b = (t % a_time) // b_time
    c = (t % a_time) % b_time // c_time
    print(a, b, c)
