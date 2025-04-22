def _3003():
    nums = list(map(int, input().split()))
    for i, nums_parts in enumerate(nums):
        if i < 2:
            ref = 1
        elif i < 5:
            ref = 2
        else:
            ref = 8
        nums[i] = ref - nums_parts
    print(*nums)

def _3009():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 == x2:
        x = x3
    elif x1 == x3:
        x = x2
    else:
        x = x1
    if y1 == y2:
        y = y3
    elif y1 == y3:
        y = y2
    else:
        y = y1
    print(x, y)

def _3052():
    list = []
    for num in range(10):
        list.append(int(input()) % 42)
    print(len(set(list)))

if __name__ == '__main__':
    _3003()