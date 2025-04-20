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