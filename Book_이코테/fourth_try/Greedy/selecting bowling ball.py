'''
볼링공 고르기

두 사람이 서로 다른 무게를 고를 수 있는 볼링 공의 조합 경우의 수 구하기
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
balls = list(map(int, input().rstrip().split()))
ballCounts = [0] * 11

for weight in balls :
	ballCounts[weight] += 1

count = 0;

for weight in range(1, m + 1) :
	ballCount = ballCounts[weight]
	n -= ballCount
	count += ballCount * n

print(count)