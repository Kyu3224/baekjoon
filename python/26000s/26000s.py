def _26069():
    import sys
    dance_people = {'ChongChong': True}
    for i in range(int(input())):
        names = list(sys.stdin.readline().split())
        if names[0] not in dance_people and names[1] in dance_people:
            dance_people[names[0]] = True
        elif names[0] in dance_people and names[1] not in dance_people:
            dance_people[names[1]] = True
    print(len(dance_people.keys()))

if __name__ == '__main__':
    _26069()