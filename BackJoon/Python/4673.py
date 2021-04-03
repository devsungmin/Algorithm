number = set(range(1, 100001))
remove = set()

for i in range(1, 10001):
    for j in str(i):
        i  += int(j)
    remove.add(i)

self_number = number - remove

for i in sorted(self_number):
    print(i)