def _4948():
    import sys
    import math
    # Maximum input
    MAX = 123456 * 2

    is_prime = [True] * (MAX + 1)
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX + 1, i):
                is_prime[j] = False

    for line in sys.stdin:
        num = int(line.strip())
        if num == 0:
            break
        count = sum(is_prime[num+1:2*num+1])
        print(count)

if __name__ == '__main__':
    _4948()