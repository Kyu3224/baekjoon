def _24060():
    import math

    def merge_sort(A, p, r, buffer):
        if p < r:
            q = math.floor((p + r) / 2)
            merge_sort(A, p, q, buffer)
            merge_sort(A, q + 1, r, buffer)
            merge(A, p, q, r, buffer)

    def merge(A, p, q, r, buffer):
        tmp = [0] * (r - p + 1)
        i, j = p, q + 1
        t = 0

        while i <= q and j <= r:
            if A[i] <= A[j]:
                tmp[t] = A[i]
                buffer.append(A[i])
                i += 1
            else:
                tmp[t] = A[j]
                buffer.append(A[j])
                j += 1
            t += 1

        while i <= q:
            tmp[t] = A[i]
            buffer.append(A[i])
            i += 1
            t += 1

        while j <= r:
            tmp[t] = A[j]
            buffer.append(A[j])
            j += 1
            t += 1

        for i in range(len(tmp)):
            A[p + i] = tmp[i]

    array_size, tar_cnt = map(int, input().split())
    array_input = list(map(int, input().split()))
    saved_buffer = []
    merge_sort(array_input, 0, array_size - 1, saved_buffer)
    print(saved_buffer[tar_cnt - 1] if tar_cnt <= len(saved_buffer) else -1)

if __name__ == '__main__':
    _24060()