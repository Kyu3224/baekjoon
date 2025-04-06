def _17103():
    import math
    num_input = int(input())
    MAX = 1000000

    is_prime = [True] * (MAX + 1)
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX + 1, i):
                is_prime[j] = False

    for _ in range(num_input):
        num = int(input())
        cnt = 0
        for i in range(2, num // 2 + 1):
            if is_prime[i] and is_prime[num - i]:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    _17103()