import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][1] = 1
for i in range(1, K+1):
    dp[1][i] = i
    
for i in range(2, N+1):
    for j in range(2, K+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000
        
print(dp[N][K] % 1000000000)