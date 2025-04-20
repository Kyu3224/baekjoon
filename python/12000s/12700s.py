def _12789():
    import sys
    n = int(input())
    people = list(map(int, sys.stdin.readline().split()))
    people_pass = [0]
    people_stop = []
    while len(people_pass) + len(people_stop) < n + 1:
        if people[0] == people_pass[-1] + 1:
            people_pass.append(people[0])
            people.pop(0)
        elif len(people_stop) > 0 and people_stop[-1] == people_pass[-1] + 1:
            people_pass.append(people_stop[-1])
            people_stop.pop(-1)
        else:
            people_stop.append(people[0])
            people.pop(0)
    can_have = True
    for idx in range(len(people_stop) - 1):
        if people_stop[idx] != people_stop[idx + 1] + 1:
            can_have = False
            break
    print("Nice" if can_have else "Sad")


if __name__ == '__main__':
    _12789()