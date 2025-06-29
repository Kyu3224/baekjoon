def _12015():
    def put_num(_array, num_to_find):
        start, end = 0, len(_array) - 1
        while start <= end:
            mid = (start + end) // 2
            if _array[mid] >= num_to_find:
                end = mid - 1
            else:
                start = mid + 1
        return start

    n = int(input())
    num_list = list(map(int, input().split()))
    sol_array = []
    for query in num_list:
        if not sol_array or query > sol_array[-1]:
            sol_array.append(query)
        else:
            idx = put_num(sol_array, query)
            sol_array[idx] = query
    print(len(sol_array))

if __name__ == '__main__':
    _12015()