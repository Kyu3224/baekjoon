def _4134():
    import math
    num_test = int(input())
    for _ in range(num_test):
        num = int(input())
        prime_cand = max(num, 2)
        is_prime = False
        while not is_prime:
            is_prime = True
            for i in range(2, int(math.sqrt(prime_cand)) + 1):
                if prime_cand % i == 0:
                    is_prime = False
                    prime_cand += 1
                    break
            if is_prime:
                print(prime_cand)
                break

if __name__ == '__main__':
    _4134()