'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, index=0, count=0):
    nextIndex = index + 1
    if len(word) < 2:
        return 0
    elif nextIndex > len(word) -1:
        return count
    else:
        if word[index] + word[index+1] == 'th':
            count += 1
        return count_th(word, nextIndex, count)
    


print(count_th('abcthefthghith'))
