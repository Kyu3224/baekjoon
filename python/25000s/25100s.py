def _25192():
    # If people_chatted = [], time out occurs.
    import sys
    num_chat = int(input())
    people_chatted = {}
    num_emoticon = 0
    for i in range(num_chat):
        chat = sys.stdin.readline().strip()
        if chat == 'ENTER':
            people_chatted = {}
            continue

        if chat in people_chatted:
            continue
        else:
            people_chatted[chat] = True
            num_emoticon += 1
    print(num_emoticon)

if __name__ == '__main__':
    _25192()