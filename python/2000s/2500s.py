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