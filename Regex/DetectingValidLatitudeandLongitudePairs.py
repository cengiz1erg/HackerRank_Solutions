import re

n = int(input())

Pattern = r"\(([+-]?[1-9][0-9]*(?:\.[0-9]+)?), ([+-]?[1-9][0-9]*(?:\.[0-9]+)?)\)"

for _ in range (n):
    x = input()
    a = re.search(Pattern, x)
    if a:
        if (-90 <= float(a.group(1)) <= +90) and (-180 <= float(a.group(2)) <= 180):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
