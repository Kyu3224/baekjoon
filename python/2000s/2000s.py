def _2075():
    import sys, heapq

    _input = sys.stdin.readline

    array_size = int(_input())
    heap = []
    for i in range(array_size):
        nums = list(map(int, _input().split()))
        for num in nums:
            if len(heap) < array_size:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
    print(heap[0])

if __name__ == '__main__':
    _2075()