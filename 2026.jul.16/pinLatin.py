''' Challenge of July 16th, 2026
Given a string, convert it to Pig Latin using the following rules:

- If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to "universeway".
- If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to "ellohay".
- Preserve the case of the first letter. For example, "Hello" converts to "Ellohay".
'''
s = input('Write a word: ')
def pig_latin(s):
    # list = s.split()
    ns = ''
    # Considering that s is a single word
    if s[0] in 'aeiou':
        ns = f"{s}way"
    else:
        ns = "Error. The word doesn't beggins with an vowel."

    # result = " ".join(ns)
    return ns

a = pig_latin(s)
print(a)



# s = input(str('Write a word: '))
# # ns = f"{s}way"
# result = ''
# if s in 'aeiou':
#     result = f"{s}way"

# print(result)
