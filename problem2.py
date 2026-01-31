n = int(input())
a = list(map(int, input().split()))
k = int(input())

maxsum = float('-inf')

for i in range(n - k + 1):
    sum_ = 0
    for j in range(i, i + k):
        sum_ += a[j]
    maxsum = max(maxsum, sum_)

print(maxsum)
