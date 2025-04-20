def _28278():
    import sys
    num_commands = int(input())
    list_stack = []
    for _ in range(num_commands):
        command = list(map(int, sys.stdin.readline().split()))
        if command[0] == 1:
            list_stack.append(command[1])
        elif command[0] == 2:
            print(list_stack.pop() if len(list_stack) != 0 else -1)
        elif command[0] == 3:
            print(len(list_stack))
        elif command[0] == 4:
            print(0 if list_stack else 1)
        elif command[0] == 5:
            print(list_stack[-1] if list_stack else -1)

def _28279():
    import sys
    from collections import deque
    num_commands = int(input())
    _queue = deque()
    for i in range(num_commands):
        command = sys.stdin.readline().split()
        if command[0] == '1':
            _queue.appendleft(int(command[1]))
        elif command[0] == '2':
            _queue.append(int(command[1]))
        elif command[0] == '3':
            print(_queue.popleft() if len(_queue) > 0 else -1)
        elif command[0] == '4':
            print(_queue.pop() if len(_queue) > 0 else -1)
        elif command[0] == '5':
            print(len(_queue))
        elif command[0] == '6':
            print(0 if len(_queue) > 0 else 1)
        elif command[0] == '7':
            print(_queue[0] if len(_queue) > 0 else -1)
        elif command[0] == '8':
            print(_queue[-1] if len(_queue) > 0 else -1)


if __name__ == '__main__':
    _28279()