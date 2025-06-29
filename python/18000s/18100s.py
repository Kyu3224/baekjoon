def _18108():
    year = int(input())
    year -= 543
    print(year)

def _18111():
    import sys
    _input = sys.stdin.readline

    N, M, B = map(int, _input().split())
    max_height = 256
    height_counts = [0] * (max_height + 1)

    for _ in range(N):
        for h in map(int, _input().split()):
            height_counts[h] += 1

    best_time, best_height = float('inf'), 0

    for ref_height in range(max_height + 1):
        remove, add = 0, 0

        for h in range(max_height + 1):
            if h < ref_height:
                add += (ref_height - h) * height_counts[h]
            elif h > ref_height:
                remove += (h - ref_height) * height_counts[h]

        if remove + B < add:
            continue

        time = remove * 2 + add
        if time < best_time or (time == best_time and ref_height > best_height):
            best_time = time
            best_height = ref_height

    print(best_time, best_height)

if __name__ == '__main__':
    _18108()