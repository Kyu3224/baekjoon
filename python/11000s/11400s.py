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

def _11478():
    words = list(input())
    word_made = []
    for i in range(1, len(words) + 1):
        for j in range(0, len(words) - i + 1):
            word_made.append(''.join(words[j:j + i]))
    print(len(set(word_made)))

if __name__ == '__main__':
    _11478()