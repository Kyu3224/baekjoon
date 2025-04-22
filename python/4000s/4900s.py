def _4948():
    import sys
    import math
    # Maximum input
    MAX = 123456 * 2

    is_prime = [True] * (MAX + 1)
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX + 1, i):
                is_prime[j] = False

    for line in sys.stdin:
        num = int(line.strip())
        if num == 0:
            break
        count = sum(is_prime[num+1:2*num+1])
        print(count)

def _4949():
    import sys
    for line in sys.stdin:
        word = line.strip('\n')
        if word == '.':
            break
        word_stack = []
        is_balanced = True
        for i in range(len(word)):
            if word[i] == '(' or word[i] == '[':
                word_stack.append(word[i])
            elif word[i] == ')' or word[i] == ']':
                if len(word_stack) == 0:
                    is_balanced = False
                    break
                last = word_stack.pop(-1)
                if (word[i] == ')' and last != '(') or (word[i] == ']' and last != '['):
                    is_balanced = False
                    break
        print('yes' if is_balanced and len(word_stack) == 0 else 'no')

if __name__ == '__main__':
    _4948()