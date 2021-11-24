n = int(input())
line = list(map(int, input().rstrip().split()))

line.sort()
print(line[(n - 1)//2])