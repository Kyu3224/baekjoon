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

def _11286():
    import sys

    _input = sys.stdin.readline

    class MinHeapAbs:
        def __init__(self):
            self.heap = []

        def push(self, val):
            self.heap.append(val)
            self._sift_up(len(self.heap) - 1)

        def pop(self):
            if not self.heap:
                return 0
            if len(self.heap) == 1:
                return self.heap.pop()
            min_value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._sift_down(0)
            return min_value

        def _check_cond(self, parent_idx, idx):
            is_satisfied = False
            if abs(self.heap[parent_idx]) > abs(self.heap[idx]):
                is_satisfied = True
            if abs(self.heap[parent_idx]) == abs(self.heap[idx]) and self.heap[parent_idx] > self.heap[idx]:
                is_satisfied = True
            return is_satisfied

        def _sift_up(self, idx):
            parent_node = (idx - 1) // 2
            while parent_node >= 0 and self._check_cond(parent_node, idx):
                self.heap[idx], self.heap[parent_node] = self.heap[parent_node], self.heap[idx]
                idx = parent_node
                parent_node = (idx - 1) // 2

        def _sift_down(self, idx):
            while True:
                smallest = idx
                left, right = 2 * idx + 1, 2 * idx + 2

                if left < len(self.heap) and self._check_cond(smallest, left):
                    smallest = left

                if right < len(self.heap) and self._check_cond(smallest, right):
                    smallest = right

                if smallest == idx:
                    break
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest

    num_action = int(_input())
    test_heap = MinHeapAbs()
    for i in range(num_action):
        action = int(_input())
        if action == 0:
            print(test_heap.pop())
        else:
            test_heap.push(action)

if __name__ == '__main__':
    _11279()