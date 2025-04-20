def _9012():
    import sys
    num_ps = int(sys.stdin.readline().strip())
    for _ in range(num_ps):
        ps = sys.stdin.readline().strip()
        ps_list = []
        is_vsp = True
        for i in range(len(ps)):
            if ps[i] == '(':
                ps_list.append(ps[i])
            else:
                if not ps_list:
                    is_vsp = False
                    break
                ps_list.pop(-1)
        print("YES" if is_vsp and not ps_list else "NO")

if __name__ == '__main__':
    _9012()