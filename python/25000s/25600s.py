def _25682():
    # Submitted with pypy3
    import sys
    _input = sys.stdin.readline
    n, m, k = map(int, _input().strip().split())
    table_white_start = [[0] * (m + 1) for _ in range(n + 1)]
    table_black_start = [[0] * (m + 1) for _ in range(n + 1)]
    sum_white_table = [[0] * (m + 1) for _ in range(n + 1)]
    sum_black_table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        input_name = _input().strip()
        for j in range(1, m + 1):
            current_color = input_name[j - 1]
            if (i + j) % 2 == 0:
                if current_color != 'W':
                    table_white_start[i][j] = 1
                if current_color != 'B':
                    table_black_start[i][j] = 1
            else:
                if current_color != 'B':
                    table_white_start[i][j] = 1
                if current_color != 'W':
                    table_black_start[i][j] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum_white_table[i][j] = (table_white_start[i][j] + sum_white_table[i][j - 1] +
                                     sum_white_table[i - 1][j] - sum_white_table[i - 1][j - 1])
            sum_black_table[i][j] = (table_black_start[i][j] + sum_black_table[i][j - 1] +
                                     sum_black_table[i - 1][j] - sum_black_table[i - 1][j - 1])
    min_value = float('inf')
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            value_from_white = (
                    sum_white_table[i + k - 1][j + k - 1]
                    - sum_white_table[i + k - 1][j - 1]
                    - sum_white_table[i - 1][j + k - 1]
                    + sum_white_table[i - 1][j - 1]
            )
            value_from_black = (
                    sum_black_table[i + k - 1][j + k - 1]
                    - sum_black_table[i + k - 1][j - 1]
                    - sum_black_table[i - 1][j + k - 1]
                    + sum_black_table[i - 1][j - 1]
            )
            min_value = min(min_value, value_from_white, value_from_black)

    print(min_value)

if __name__ == '__main__':
    _25682()