'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    # TBC
    if len(word) <= 1:
        return 0

    split_word = word[1:]
    #print(word, split_word)
    count += count_th(split_word)

    if word[0] == 't' and word[1] == 'h':
        count += 1

    return count
    
