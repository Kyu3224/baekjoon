def _7785():
    num_log = int(input())
    people_status = {}
    for _ in range(num_log):
        people, action = input().split()
        people_status[people] = action
    result = sorted([name for name, act in people_status.items() if act == 'enter'], reverse=True)
    print('\n'.join(result))

if __name__ == '__main__':
    _7785()