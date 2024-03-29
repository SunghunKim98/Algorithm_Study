def solution(N, number):
    dp = [set() for i in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N)*i))

        for j in range(i//2 + 1):
            for n1 in dp[j]:
                for n2 in dp[i-j]:
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0:
                        dp[i].add(n1 // n2)
                    if n1 != 0:
                        dp[i].add(n2 // n1)

        if number in dp[i]:
            return i
    return -1
