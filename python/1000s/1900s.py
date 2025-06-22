def _1904():
    def dp(n):
        if n == 1 or n == 2:
            return n
        else:
            prev = 1
            cur = 2
            for i in range(2, n):
                num = (prev + cur) % 15746
                prev = cur
                cur = num
            return cur

    print(dp(int(input())))

def _1912():
    import sys
    input = sys.stdin.readline

    num_input = int(input())
    nums = list(map(int, input().split()))
    prev = nums[0]
    max_val = prev
    for i in range(1, num_input):
        prev = max(prev + nums[i], nums[i])
        max_val = max(max_val, prev)
    print(max_val)

def _1920():
    def check(num, numbers, high, low):
        # Avoid Slicing such as numbers[mid:]!
        if low > high:
            return 0
        mid = (low + high) // 2
        if numbers[mid] == num:
            return 1
        elif numbers[mid] < num:
            return check(num, numbers, high, mid + 1)
        else:
            return check(num, numbers, mid - 1, low)

    num_input = int(input())
    nums = list(map(int, input().split()))
    nums = sorted(nums)
    num_query = int(input())
    queries = list(map(int, input().split()))
    for i in range(num_query):
        print(check(queries[i], nums, high=num_input - 1, low=0))

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

def _1931():
    import sys
    _input = lambda: sys.stdin.readline().strip()
    num_input = int(_input())
    input_list = []
    for _ in range(num_input):
        start, end = map(int, _input().split())
        input_list.append([start, end])

    input_list = sorted(input_list, key=lambda x: (x[1], x[0]))
    num_schedule = 0
    end_time = 0
    for start, end in input_list:
        if start >= end_time:
            num_schedule += 1
            end_time = end
    print(num_schedule)

def _1932():
    import sys
    input = sys.stdin.readline

    n = int(input())
    prev = list(map(int, input().split()))
    new = prev
    for i in range(n - 1):
        new = list(map(int, input().split()))
        nums_to_select = len(new) - 2
        new[0] += prev[0]
        new[-1] += prev[-1]
        for j in range(nums_to_select):
            new[j + 1] += max(prev[j], prev[j + 1])
        prev = new
    print(max(new))

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

def _1992():
    def quad(size, arr):
        total_value = 0
        for row in arr:
            total_value += sum(row)
        if total_value == 0:
            return '0'
        elif total_value == size ** 2:
            return '1'
        else:
            half = size // 2
            upper_left = quad(half, [row[:half] for row in arr[:half]])
            upper_right = quad(half, [row[half:] for row in arr[:half]])
            lower_left = quad(half, [row[:half] for row in arr[half:]])
            lower_right = quad(half, [row[half:] for row in arr[half:]])
            return '(' + upper_left + upper_right + lower_left + lower_right + ')'

    import sys
    _input = lambda: sys.stdin.readline().strip()
    num_input = int(_input())
    board_array = [list(map(int, _input())) for i in range(num_input)]
    print(quad(num_input, board_array))

if __name__ == "__main__":
    _1929()