def _5622():
    word = input()
    time_spent = 0
    for i in range(len(word)):
        if ord('A') <= ord(word[i]) <= ord('C'):
            time_spent += 3
        elif ord('D') <= ord(word[i]) <= ord('F'):
            time_spent += 4
        elif ord('G') <= ord(word[i]) <= ord('I'):
            time_spent += 5
        elif ord('J') <= ord(word[i]) <= ord('L'):
            time_spent += 6
        elif ord('M') <= ord(word[i]) <= ord('O'):
            time_spent += 7
        elif ord('P') <= ord(word[i]) <= ord('S'):
            time_spent += 8
        elif ord('T') <= ord(word[i]) <= ord('V'):
            time_spent += 9
        else:
            time_spent += 10
    print(time_spent)

if __name__ == '__main__':
    _5622()