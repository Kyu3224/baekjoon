def _10101():
    angles = [int(input()) for _ in range(3)]
    if len(set(angles)) == 1 and angles[0] == 60:
        print("Equilateral")
    elif sum(angles) != 180:
        print("Error")
    elif len(set(angles)) == 3:
        print("Scalene")
    else:
        print("Isosceles")

def _10171():
    print("\    /\ \n )  ( ')\n(  /  )\n \(__)|")

def _10172():
    print('|\_/|\n|q p|   /}\n( 0 )"""\\\n' + '|"^"`    | \n||_/=\\\__|')
