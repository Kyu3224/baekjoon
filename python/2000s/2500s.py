def _2501():
    num, idx = map(int, input().split())
    num_list = []
    for i in range(num):
        if num % (i + 1) == 0:
            num_list.append(i + 1)
    num_list.sort()
    print(0 if idx > len(num_list) else num_list[idx - 1])

def _2525():
    hour, minute = map(int, input().split())
    time_need = int(input())
    if minute + time_need >= 60:
        extra_hour = (minute + time_need) // 60
        hour += extra_hour
        minute = minute + time_need - 60 * extra_hour
    else:
        minute += time_need
    hour %= 24
    print(hour, minute)

def _2557():
    print('Hello World!')

def _2558():
    nums = [int(input()) for _ in range(2)]
    print(sum(nums))

def _2559():
    import sys
    _input = sys.stdin.readline

    num_list, days = map(int, _input().split())
    items = list(map(int, _input().split()))
    max_val = 0
    for i in range(days):
        max_val += items[i]
    prev = max_val

    for i in range(num_list - days):
        new = items[i + days] - items[i]
        prev += new
        max_val = max(max_val, prev)
    print(max_val)

def _2562():
    max_idx = 1
    max_value = int(input())
    for i in range(8):
        new_value = int(input())
        if max_value < new_value:
            max_value = new_value
            max_idx = i + 2
    print(max_value)
    print(max_idx)

def _2563():
    num_paper = int(input())
    paper_size = 100
    paper_loc = []
    for i in range(num_paper):
        paper_loc.append(list(map(int, input().split())))

    area = 0
    for row in range(paper_size):
        for col in range(paper_size):
            for num in range(num_paper):
                if (paper_loc[num][0] <= row <= paper_loc[num][0] + 9) \
                        and (paper_loc[num][1] <= col <= paper_loc[num][1] + 9):
                    area += 1
                    break
    print(area)

def _2565():
    import sys
    from collections import deque
    _input = sys.stdin.readline
    num_seq = int(_input())

    num_list = deque([])

    for i in range(num_seq):
        a, b = map(int, _input().split())
        num_list.append([a, b])
    list_sorted = [sorted(num_list, key=lambda x: x[0])[i][1] for i in range(num_seq)]

    dp = [1] * num_seq

    for i in range(1, num_seq):
        for j in range(i):
            if list_sorted[j] < list_sorted[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(num_seq - max(dp))

def _2566():
    num_row = num_col = 9
    table = []
    for i in range(num_row):
        table.append(list(map(int, input().split())))

    max_val = -1
    max_col, max_row = 0, 0
    for i in range(num_row):
        for j in range(num_col):
            if table[i][j] > max_val:
                max_val = table[i][j]
                max_col = j
                max_row = i
    print(max_val)
    print(max_row + 1, max_col + 1)

def _2577():
    nums = [int(input()) for i in range(3)]
    num_counter = 10 * [0]
    mul = 1
    for num in nums:
        mul *= num
    mul = str(mul)
    for char in mul:
        num_counter[int(char)] += 1
    for cnt in num_counter:
        print(cnt)

def _2579():
    import sys
    input = sys.stdin.readline

    num_input = int(input())
    score = [int(input()) for _ in range(num_input)]

    if num_input == 1:
        print(score[0])
    elif num_input == 2:
        print(score[0] + score[1])
    elif num_input == 3:
        print(max(score[0] + score[2], score[1] + score[2]))
    else:
        dp = [0] * num_input
        dp[0] = score[0]
        dp[1] = score[0] + score[1]
        dp[2] = max(score[0] + score[2], score[1] + score[2])
        for i in range(3, num_input):
            dp[i] = max(dp[i - 2] + score[i], dp[i - 3] + score[i - 1] + score[i])
        print(dp[-1])

def _2580():
    import sys

    def solve_studocu(plate, zero_idx, idx, row_set, col_set, block_set):
        if idx == len(zero_idx):
            for row in plate:
                print(*row)
            sys.exit(0)

        row, col = zero_idx[idx]
        for i in range(1, 10):
            if i not in row_set[row] and i not in col_set[col] and i not in block_set[row // 3][col // 3]:
                plate[row][col] = i
                row_set[row].add(i)
                col_set[col].add(i)
                block_set[row // 3][col // 3].add(i)

                solve_studocu(plate, zero_idx, idx + 1, row_set, col_set, block_set)

                plate[row][col] = 0
                row_set[row].remove(i)
                col_set[col].remove(i)
                block_set[row // 3][col // 3].remove(i)

    def get_zero_idx(plate):
        idx = []
        for i in range(9):
            for j in range(9):
                if plate[i][j] == 0:
                    idx.append((i, j))
        return idx

    def initialize_sets(plate):
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        block_set = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = plate[i][j]
                if num != 0:
                    row_set[i].add(num)
                    col_set[j].add(num)
                    block_set[i // 3][j // 3].add(num)
        return row_set, col_set, block_set

    studocu_start = [list(map(int, input().split())) for i in range(9)]
    nums = get_zero_idx(studocu_start)
    row_set, col_set, block_set = initialize_sets(studocu_start)
    solve_studocu(studocu_start, nums, 0, row_set, col_set, block_set)

def _2581():
    start = int(input())
    end = int(input())
    sum_prime = min_prime = 0
    for i in range(start, end + 1):
        is_prime = True
        if i == 1:
            is_prime = False
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            sum_prime += i
            if not min_prime:
                min_prime = i
    if min_prime:
        print(sum_prime, min_prime, sep="\n")
    else:
        print(-1)

def _2587():
    num_list = [int(input()) for _ in range(5)]
    for i in range(4):
        for j in range(4 - i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    print(int(sum(num_list) / len(num_list)), num_list[2], sep="\n")

def _2588():
    a = int(input())
    b = int(input())
    first = b % 10
    second = (b // 10) % 10
    third = b // 100
    print(a * first)
    print(a * second)
    print(a * third)
    print(a * b)

if __name__ == '__main__':
    _2588()