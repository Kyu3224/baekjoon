def _2805():
    def check_tree(trees, length, length_require):
        tree_length = 0
        for tree in trees:
            if tree > length:
                tree_length += tree - length
            if tree_length >= length_require:
                return True
        else:
            return False

    def param_search(l, h, length_require, tree_arr):
        if l == h:
            return l
        m = (l + h + 1) // 2
        if check_tree(tree_arr, m, length_require):
            return param_search(m, h, length_require, tree_arr)
        else:
            return param_search(l, m - 1, length_require, tree_arr)

    num_tree, tree_height = map(int, input().split())
    trees = list(map(int, input().split()))
    low = 0
    high = max(trees)
    print(param_search(low, high, tree_height, trees))

def _2839():
    total_mass = int(input())
    max_iter = total_mass // 3
    bag_require = max_iter
    dividable = False
    for i in range(0, max_iter + 1):
        mass_left = total_mass - 3 * i
        if mass_left % 5 != 0:
            continue
        else:
            if bag_require >= i + mass_left // 5:
                bag_require = i + mass_left // 5
                dividable = True
    if bag_require == max_iter and not dividable:
        print(-1)
    else:
        print(bag_require)

def _2869():
    climb, fall, length = map(int, input().split())

    if climb >= length:
        print(1)
    else:
        remaining = length - climb
        daily_gain = climb - fall
        days = (remaining + daily_gain - 1) // daily_gain
        print(days + 1)

def _2884():
    hour, minute = map(int, input().split())
    if minute >= 45:
        minute -= 45
    else:
        minute = 60 + (minute - 45)
        if hour > 0:
            hour -= 1
        else:
            hour = 23
    print(hour, minute)

if __name__ == '__main__':
    _2884()