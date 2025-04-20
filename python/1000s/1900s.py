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

def _1934():
    import math

    nums = int(input())
    for _ in range(nums):
        a, b = map(int, input().split())
        print(a * b // math.gcd(a, b))

def _1978():
    num = int(input())
    num_list = list(map(int, input().split()))
    num_prime = 0
    for i in range(num):
        is_prime = True
        if num_list[i] == 1:
            is_prime = False
        for j in range(2, num_list[i]):
            if num_list[i] % j == 0:
                is_prime = False
        if is_prime:
            num_prime += 1
    print(num_prime)

if __name__ == "__main__":
    _1929()