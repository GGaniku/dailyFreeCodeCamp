''' Challenge of July 16th, 2026
Given a string, convert it to Pig Latin using the following rules:

1) If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to "universeway".
2) If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to "ellohay".
3) Preserve the case of the first letter. For example, "Hello" converts to "Ellohay".
'''
s = input('Write a word: ')
def pig_latin(s):
    res = ''
    cons = 0

    # Considering that s is a single word

    # Rule 1
    if s[0] in 'aeiou':
        res = f"{s}way"

    # Rule 2
    else:
        for letter in s:
            if letter not in 'aeiou':
                cons += 1
            else:
                break
        res = f"{s[cons:]}{s[:cons]}"

    return res

a = pig_latin(s)
print(a)
