def _11279():
    import heapq
    import sys

    input = sys.stdin.readline

    num_calc = int(input())
    max_heap = []

    for _ in range(num_calc):
        x = int(input())
        if x == 0:
            if max_heap:
                print(-heapq.heappop(max_heap))
            else:
                print(0)
        else:
            heapq.heappush(max_heap, -x)

if __name__ == '__main__':
    _11279()