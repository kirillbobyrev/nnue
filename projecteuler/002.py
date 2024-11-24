"""
Given the constraints, a very simple brute force solution will suffice.
"""

current, previous = 0, 1
result = 0

while current <= 4_000_000:
    current, previous = previous + current, current
    if current % 2 == 0:
        result += current

print(result)
