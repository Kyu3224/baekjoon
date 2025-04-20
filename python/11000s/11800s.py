def _11866():
    from collections import deque

    num_people, del_num = map(int, input().split())
    peoples = deque(range(1, num_people + 1))
    result = []

    while peoples:
        peoples.rotate(-del_num + 1)
        result.append(peoples.popleft())

    print("<" + ", ".join(map(str, result)) + ">")


if __name__ == '__main__':
    _11866()