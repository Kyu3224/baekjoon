def _1620():
    num_mon, num_question = map(int, input().split())
    mon_dict = {}
    mon_dict_reverse = {}
    for i in range(1, num_mon + 1):
        name = input()
        mon_dict[name] = i
        mon_dict_reverse[i] = name
    for j in range(num_question):
        mon_q = input()
        if mon_q in mon_dict:
            print(mon_dict[mon_q])
        else:
            print(mon_dict_reverse[int(mon_q)])

if __name__ == '__main__':
    _1620()