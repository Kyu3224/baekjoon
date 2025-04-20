def _24511():
    import sys
    from collections import deque
    input = sys.stdin.readline
    num_queuestack = int(input())
    queuestack = deque(map(int, input().split()))
    queuestack_var = deque(map(int, input().split()))
    permutation_length = int(input())
    permutation_var = deque(map(int, input().split()))
    queue_list = deque()

    for i in range(num_queuestack):
        if queuestack[i] == 0:
            queue_list.append(queuestack_var[i])

    sol = []
    for i in range(permutation_length):
        queue_list.appendleft(permutation_var[i])
        sol.append(queue_list.pop())
    print(*sol)

if __name__ == '__main__':
    _24511()