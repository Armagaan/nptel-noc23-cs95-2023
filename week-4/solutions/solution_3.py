vowels = ("a", "e", "i", "o", "u")

# This is how we would implement the function using loops.
# def only_vowels(words):
#     output = []
#     for word in words:
#         mask = []
#         for letter in word.lower():
#             if letter in vowels:
#                 mask.append(True)
#             else:
#                 mask.append(False)
#         if all(mask):
#             output.append(word)
#     return output

def only_vowels(words):
    '''Returns a list of words that only contain vowels.'''
    return list(
        filter(
            lambda word: all((letter in vowels for letter in word.lower())),
            words
        )
    )

def any_vowel(words):
    '''Returns a list of words that contains any vowel.'''
    return list(filter(lambda word: any((letter in vowels for letter in word.lower())), words))

def no_vowels(words):
    '''Returns a list of words that contains no vowel.'''
    return list(filter(lambda word: all((letter not in vowels for letter in word.lower())), words))

if __name__ == "__main__":
    words = ["Hmm", "hello", "wIred", "AI", "uae"]
    print(only_vowels(words))
    print(any_vowel(words))
    print(no_vowels(words))
