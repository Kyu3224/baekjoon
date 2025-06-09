def _11401():
    def factorial(n, mod):
        num_dict = {}
        num_dict[0] = 1
        for i in range(1, n + 1):
            num_dict[i] = (num_dict[i - 1] * i) % mod
        return num_dict

    def mod_inv(a, p):
        return pow(a, p - 2, p)

    n, k = map(int, input().split())
    mod = 1_000_000_007

    factorial_dict = factorial(n, mod)

    print(factorial_dict[n] * mod_inv(factorial_dict[k], mod) * mod_inv(factorial_dict[n - k], mod) % mod)

def _11444():
    def mat_mul(mat_a, mat_b):
        mat_size = len(mat_a)
        result_mat = [[0] * mat_size for _ in range(mat_size)]
        for p in range(mat_size):
            row = mat_a[p]
            for q in range(mat_size):
                for r in range(mat_size):
                    result_mat[p][r] += row[q] * mat_b[q][r]
                    result_mat[p][r] %= 1_000_000_007
        return result_mat

    def mat_exp(mat, pow):
        if pow == 1:
            return [[x % 1_000_000_007 for x in row] for row in mat]
        elif pow == 2:
            return mat_mul(mat, mat)
        elif pow % 2 == 0:
            mat_half = mat_exp(mat, pow=pow // 2)
            return mat_mul(mat_half, mat_half)
        else:
            mat_half = mat_exp(mat, pow=pow // 2)
            return mat_mul(mat_mul(mat_half, mat_half), mat)

    n_fib = int(input())
    mat = [[1, 1], [1, 0]]
    if n_fib <= 1:
        print(n_fib)
    else:
        print(mat_exp(mat, n_fib)[0][1])

def _11478():
    words = list(input())
    word_made = []
    for i in range(1, len(words) + 1):
        for j in range(0, len(words) - i + 1):
            word_made.append(''.join(words[j:j + i]))
    print(len(set(word_made)))

if __name__ == '__main__':
    _11478()