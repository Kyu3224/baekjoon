def _18870():
    num_pts = int(input())
    pts = list(map(int, input().split()))
    pts_sorted = sorted(list(set(pts)))
    value_to_index = {value: index for index, value in enumerate(pts_sorted)}
    print(''.join(str(value_to_index[x]) + ' ' for x in pts).rstrip(' '))

if __name__ == '__main__':
    _18870()