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

def _1629():
    def recur_remainder(base, exponent, modulus):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base % modulus

        half = recur_remainder(base, exponent // 2, modulus)

        if exponent % 2 == 0:
            return (half * half) % modulus
        else:
            return (half * half * base) % modulus

    base_num, exp_num, mod_num = map(int, input().split())
    print(recur_remainder(base_num, exp_num, mod_num))

if __name__ == '__main__':
    _1620()