''' Challenge of July 16th, 2026
Given a string, convert it to Pig Latin using the following rules:

- If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to "universeway".
- If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to "ellohay".
- Preserve the case of the first letter. For example, "Hello" converts to "Ellohay".
'''

def pig_latin(s):
    list = s.split()


    if 'aeiou' in s[0]:
        list = f'{s + 'way'}'

    result = " ".join(list)
    return result

print(pig_latin('universe'))
