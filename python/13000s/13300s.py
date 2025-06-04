def _13305():
    import sys
    _input = lambda: sys.stdin.readline().strip()
    num_input = int(_input())
    road_data = list(map(int, _input().split()))
    oil_data = list(map(lambda x: [int(x[1]), x[0]], enumerate(_input().split())))
    oil_data_sorted = sorted(oil_data, key=lambda x: (x[0], x[1]))
    price = 0
    end_idx = num_input - 1
    for data in oil_data_sorted:
        if data[1] == num_input - 1 or data[1] > end_idx:
            continue
        price += sum(road_data[data[1]:end_idx]) * data[0]
        end_idx = data[1]
        if end_idx == 0:
            break
    print(price)

if __name__ == '__main__':
    _13305()