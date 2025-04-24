def _4779():
    import sys
    def cantor_set(arr, start, end):
        # When we change value with slicing, list values are not modified -> We should modify value with index.
        if end - start + 1 >= 3:
            third = (end - start + 1) // 3
            for i in range(start + third, start + 2 * third):
                arr[i] = False
            cantor_set(arr, start, start + third - 1)
            cantor_set(arr, start + 2 * third, end)

    for line in sys.stdin:
        line = line.strip()
        if not line or line == "":
            break
        n = int(line)
        if not (0 <= n <= 12):
            continue
        length = 3 ** n
        cantor_array = [True] * length
        cantor_set(cantor_array, 0, length - 1)
        print(''.join('-' if x else ' ' for x in cantor_array))

if __name__ == '__main__':
    _4779()