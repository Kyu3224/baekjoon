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

def _9063():
    num_input = int(input())
    x_min = x_max = y_min = y_max = None
    for i in range(num_input):
        x, y = map(int, input().split())
        if i == 0:
            x_min = x_max = x
            y_min = y_max = y
        x_max = max(x_max, x)
        y_max = max(y_max, y)
        x_min = min(x_min, x)
        y_min = min(y_min, y)
    print((y_max - y_min) * (x_max - x_min))

def _9086():
    num = int(input())
    for i in range(num):
        word = input()
        print(f"{word[0]}{word[-1]}")

if __name__ == '__main__':
    _9012()