def _1929():
    import math
    start, end = map(int,input().split())
    num_prime = []
    for num in range(max(start,2), end+1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            num_prime.append(num)
    print(*num_prime,sep='\n')

if __name__ == "__main__":
    _1929()