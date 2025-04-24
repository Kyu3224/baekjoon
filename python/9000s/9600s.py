def _9663():
    def n_queen(row, n, cols, diag1, diag2):
        if row == n:
            return 1

        count = 0

        for col in range(n):
            if not cols[col] and not diag1[row - col + n - 1] and not diag2[row + col]:
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = True
                count += n_queen(row + 1, n, cols, diag1, diag2)
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = False
        return count

    num_input = int(input())
    columns = [False] * num_input
    diag1 = [False] * (2 * num_input - 1)  # Num of distinct diagonal from right up -> left bottom
    diag2 = [False] * (2 * num_input - 1)  # Num of distinct diagonal from left bottom -> right up
    print(n_queen(0, num_input, columns, diag1, diag2))

if __name__ == '__main__':
    _9663()