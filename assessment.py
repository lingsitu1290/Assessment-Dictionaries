"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_dict = {}

    for word in phrase.split(): 
        word_dict[word] = word_dict.get(word, 0) + 1
        
    return word_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """
    melon = {
    'Watermelon': 2.95,
    'Cantaloupe': 2.50, 
    'Musk': 3.25, 
    'Christmas':14.25,
    }

    return melon.get(melon_name, 'No price found')


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # Able to return but didn't sort ['an','ok'] alphabetically

    word_len_dict = {}

    for word in words: 
        word_len_dict.setdefault(len(word),[]).append(word)
        # word_len_dict[len(word)] = word_len_dict.get(len(word), [word]) 

        # if len(word) in word_len_dict.keys():
        #     [word].append(word)

        # return (len(word), [word])

    #sort the values of the dictionary

    for length, word_list in word_len_dict.iteritems():
        word_list.sort()

    return [(key, value) for key, value in word_len_dict.iteritems()]


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    pirate_dict = {
    'sir':'matey',
    'hotel':'fleabag inn',
    'student':'swabbie',
    'man':'matey',
    'professor':'foul blaggart',
    'restaurant':'galley',
    'your':'yer',
    'excuse':'arr',
    'students':'swabbies',
    'are':'be',
    'restroom':'head',
    'my':'me',
    'is':'be',
    'man!':'man!',
    }

    # pirate_phrase = []

    # for word in phrase.split():
    #     if word in pirate_dict:
    #         pirate_phrase.append(pirate_dict[word])
    #     else: 
    #         pirate_phrase.append(word)
    
    # return ' '.join(pirate_phrase)
    

    # Using list comprehension
    return ' '.join([pirate_dict.get(word, word) for word in phrase.split()])

def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Possibly start with dictionary of all words with values set as list of words?
    # As each word is used, pop it out from the list of words?

    # List will start with first name
    output = [names.pop(0)]

    # Create dict with first letter and name
    first_letter_dict = {}

    # Create dict of first letter and list of names
    for name in names:
        if name[0] not in first_letter_dict:
            first_letter_dict[name[0]] = [name]

        else:
            first_letter_dict[name[0]].append(name)

    # Do looping to look for the first word with the start letter of last letter of the last word in the output list
    while True:

        start_letter = output[-1][-1]

        #If there is no words with that start letter, break out of loop
        if not first_letter_dict.get(start_letter):
            break

        # Get the first word with that start letter and remove
        word = first_letter_dict[start_letter].pop(0)
        output.append(word)

    return output

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
