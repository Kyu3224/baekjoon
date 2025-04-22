def _14681():
    x_coor = int(input())
    y_coor = int(input())
    if x_coor > 0:
        if y_coor > 0:
            print("1")
        else:
            print("4")
    else:
        if y_coor > 0:
            print('2')
        else:
            print('3')

if __name__ == '__main__':
    _14681()