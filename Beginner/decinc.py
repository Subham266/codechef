# cook your dish here
from sys import stdin
n = int(stdin.readline())
if n % 4 == 0:
    print(n+1)
else:
    print(n-1)