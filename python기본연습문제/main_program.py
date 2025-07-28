# main_program.py
#import math_operations   #1
from math_operations import circle_area
from math_operations import rectangle_area   #2

# 모듈 사용
radius = 5
#1
#print(f"원의 넓이: {math_operations.circle_area(radius)}")

#2 
print(f"원의 넓이: {circle_area(radius)}")

width, height = 10, 5
#1
#print(f"직사각형 넓이: {math_operations.rectangle_area(width, height)}")

#2
print(f"직사각형 넓이: {rectangle_area(width, height)}")

n = 5
#1
#print(f"팩토리얼 {n}! = {math_operations.factorial(n)}")

a, b = 48, 18
#1
#print(f"최대공약수({a}, {b}) = {math_operations.gcd(a, b)}")