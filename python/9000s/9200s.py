def _9251():
    import sys
    _input = sys.stdin.readline

    first_word = _input().strip()
    second_word = _input().strip()
    dp = [[0] * (len(second_word) + 1) for _ in range(len(first_word) + 1)]
    for i in range(1, len(first_word) + 1):
        for j in range(1, len(second_word) + 1):
            if first_word[i - 1] == second_word[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[-1][-1])

if __name__ == '__main__':
    _9251()