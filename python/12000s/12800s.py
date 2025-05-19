def _12865():
    num_items, max_weight = map(int, input().split())
    bags = [[0, 0] for i in range(num_items)]
    dp = [[0] * (max_weight + 1) for idx in range(num_items)]
    for i in range(num_items):
        bags[i] = list(map(int, input().split()))

    for i in range(bags[0][0], max_weight + 1):
        dp[0][i] = bags[0][1]

    for i in range(1, num_items):
        dp[i] = dp[i - 1].copy()
        for j in range(bags[i][0], max_weight + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - bags[i][0]] + bags[i][1])
    print(dp[-1][-1])

if __name__ == '__main__':
    _12865()