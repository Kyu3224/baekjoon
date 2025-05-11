def _11718():
    while True:
        try:
            word = input()
            if word == '':
                break
            print(word)
        except EOFError:  # EOF 입력 시 안전하게 종료
            break

def _11720():
    num = int(input())
    nums = input()
    sums = 0
    for i in range(num):
        sums += int(nums[i])
    print(sums)

def _11729():
    def hanoi_tower(num_poles, start, goal):
        if num_poles == 1:
            print(f"{start} {goal}")
            return
        left = 6 - start - goal
        hanoi_tower(num_poles - 1, start, left)
        print(f"{start} {goal}")
        hanoi_tower(num_poles - 1, left, goal)

    num_pole = int(input())
    print(2 ** num_pole - 1)
    hanoi_tower(num_pole, 1, 3)

def _11758():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    vec1 = (x2 - x1, y2 - y1)
    vec2 = (x3 - x2, y3 - y2)
    cross = vec1[0] * vec2[1] - vec1[1] * vec2[0]
    if cross == 0:
        print(0)
    elif cross > 0:
        print(1)
    else:
        print(-1)

if __name__ == '__main__':
    _11720()