def _18258():
    from collections import deque
    import sys

    num_command = int(sys.stdin.readline())
    _queue = deque()
    for _ in range(num_command):
        command = sys.stdin.readline().strip()
        if command.startswith('push'):
            input_num = int(command.split()[-1])
            _queue.append(input_num)
        elif command == 'pop':
            print(_queue.popleft() if _queue else -1)
        elif command == 'size':
            print(len(_queue))
        elif command == 'empty':
            print(1 if len(_queue) == 0 else 0)
        elif command == 'front':
            print(_queue[0] if _queue else -1)
        elif command == 'back':
            print(_queue[-1] if _queue else -1)

if __name__ == '__main__':
    _18258()