import sys
from math import gcd


def lcd(a, b):
    return a * b // gcd(a, b)


a, b = map(int, sys.stdin.readline().split())

print(gcd(a, b))
print(lcd(a, b))
