num1 = int(input())
num2 = int(input())

print("%d\n%d\n%d\n%d"%((num1 * (num2 % 10)), (num1 * ((num2 % 100)//10)), (num1 * (num2//100)), (num1 * num2)))