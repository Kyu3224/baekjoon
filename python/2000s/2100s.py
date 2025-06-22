def _2108():
    import sys
    from collections import defaultdict
    num_dict = defaultdict(int)
    nums = int(input())
    numbers = []
    for _ in range(nums):
        num = int(sys.stdin.readline())
        num_dict[num] += 1
        numbers.append(num)

    # Average
    print(int(round(sum(numbers) / nums, 0)))

    # Mid value
    key_list = sorted(numbers)
    print(key_list[nums // 2])

    # frequency
    max_val = max(num_dict.values())
    max_vals = []
    for key, value in num_dict.items():
        if value == max_val:
            max_vals.append(key)
    print(sorted(max_vals)[1] if len(max_vals) > 1 else max_vals[0])

    # range
    print(key_list[-1] - key_list[0])

def _2110():
    def is_feasible(house_arr, house_dist, num_net):
        count = 1
        last_pos = house_arr[0]
        for i in range(1, len(house_arr)):
            if house_arr[i] - last_pos >= house_dist:
                count += 1
                last_pos = house_arr[i]
                if count >= num_net:
                    return True
        return False

    def param_search(l, h, house_arr, num_net):
        if l == h:
            return l
        m = (l + h + 1) // 2
        if is_feasible(house_arr, m, num_net):
            return param_search(m, h, house_arr, num_net)
        else:
            return param_search(l, m - 1, house_arr, num_net)

    num_house, num_net = map(int, input().split())
    houses = [int(input()) for _ in range(num_house)]
    houses = sorted(houses)
    min_pos = min(houses)
    max_pos = max(houses)
    low = 1
    high = houses[-1] - houses[0]
    print(param_search(low, high, houses, num_net))

def _2156():
    import sys
    input = sys.stdin.readline

    num_wine = int(input())
    wines = [int(input()) for _ in range(num_wine)]

    dp = [0] * num_wine
    if num_wine == 1:
        print(wines[0])
    elif num_wine == 2:
        print(wines[0] + wines[1])
    elif num_wine == 3:
        print(max(wines[0] + wines[2], wines[1] + wines[2], wines[0] + wines[1]))
    else:
        dp[0] = wines[0]
        dp[1] = wines[0] + wines[1]
        dp[2] = max(wines[0] + wines[2], wines[1] + wines[2], dp[1])

        for i in range(3, num_wine):
            dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])
        print(dp[num_wine - 1])


def _2164():
    from collections import deque
    _queue = deque([i+1 for i in range(int(input()))])
    while len(_queue) != 1:
        _queue.popleft()
        _queue.append(_queue.popleft())
    print(_queue.popleft())

if __name__ == '__main__':
    _2108()
    # _2164()