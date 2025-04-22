def _13241():
    def get_gcd(start, fin):
        if fin == 0:
            return start
        return get_gcd(fin, start % fin)

    a, b = map(int, input().split())
    print(a * b // get_gcd(a, b))

if __name__ == '__main__':
    _13241()