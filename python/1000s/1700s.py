def _1735():
    import math

    nums = [list(map(int, input().split())) for _ in range(2)]
    results = [nums[0][0] * nums[1][1] + nums[0][1] * nums[1][0], nums[0][1] * nums[1][1]]
    gcd = math.gcd(results[0], results[1])
    results = [results[0] // gcd, results[1] // gcd]
    print(*results)

def _1764():
    num_listen, num_see = map(int, input().split())
    listen_list = {}
    for _ in range(num_listen):
        listen_list[input()] = 'y'

    see_list = {}
    for _ in range(num_see):
        name = input()
        if name in listen_list:
            see_list[name] = 'y'
    print(len(see_list), *sorted(list(see_list.keys())), sep='\n')

def _1780():
    def recur_div(size, arr, counter):
        total_value = 0
        real_value = 0
        for row in arr:
            total_value += sum(map(abs, row))
            real_value += sum(row)
        if total_value == 0:
            counter['n_zero'] += 1
        elif real_value == -size ** 2:
            counter['n_neg'] += 1
        elif real_value == size ** 2:
            counter['n_pos'] += 1
        else:
            tri = size // 3
            recur_div(tri, [row[:tri] for row in arr[:tri]], counter)
            recur_div(tri, [row[tri:2 * tri] for row in arr[:tri]], counter)
            recur_div(tri, [row[2 * tri:] for row in arr[:tri]], counter)
            recur_div(tri, [row[:tri] for row in arr[tri:2 * tri]], counter)
            recur_div(tri, [row[tri:2 * tri] for row in arr[tri:2 * tri]], counter)
            recur_div(tri, [row[2 * tri:] for row in arr[tri:2 * tri]], counter)
            recur_div(tri, [row[:tri] for row in arr[2 * tri:]], counter)
            recur_div(tri, [row[tri:2 * tri] for row in arr[2 * tri:]], counter)
            recur_div(tri, [row[2 * tri:] for row in arr[2 * tri:]], counter)

    import sys
    from collections import defaultdict

    _input = lambda: sys.stdin.readline().strip()
    num_input = int(_input())
    board_array = [list(map(int, _input().split())) for i in range(num_input)]
    counter = defaultdict(int)
    recur_div(num_input, board_array, counter)
    print(counter['n_neg'], counter['n_zero'], counter['n_pos'], sep="\n")

if __name__ == '__main__':
    _1735()