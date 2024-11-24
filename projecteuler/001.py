"""
Given the constraints of the problem (numbers just below a thousand), a very
simple brute force solution will suffice.
"""

result = 0

for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        result += num

print(result)
