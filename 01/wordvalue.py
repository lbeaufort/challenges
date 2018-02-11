from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    #save the dictionary in a large string `file`
    file = open(DICTIONARY, 'r')

    #split the `file` into a list of words
    dictionary = file.read().split()

    return dictionary
    pass

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        # print('letter {0} score is {1}'.format(letter, LETTER_SCORES[letter.upper()]))
        #.get(key, default)
        score = score + LETTER_SCORES.get(letter.upper(), 0)

    return score
    pass

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if not word_list:
        word_list = load_words()

    scores = []

    for word in word_list:
        score = calc_word_value(word)
        scores.append((word, score))
        #print('word: {0} score is: {1}'.format(word, score))
        #print('word is {0}'.format(scores[-1][0]))

    scores.sort(key = lambda x : x[1], reverse = True)
    return scores[0][0]

    pass

if __name__ == "__main__":
    pass # run unittests to validate

# print(max_word_value())
# print(max_word_value(['Laura', 'Steve', 'Stephanie']))
