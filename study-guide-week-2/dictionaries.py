"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example:

        >>> no_dupes = without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"])

        >>> isinstance(no_dupes, list)
        True

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]

    The function should return a variable of type list:
        >>> type(without_duplicates([111111, 2, 33333, 2]))
        <class 'list'>
    """
    # Method 1
    # set_words = set(words)
    # new_list = []

    # for word in set_words:
    #     new_list.append(word)

    # return new_list

    # Method 2
    return [word for word in set(words)]



def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a set of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should return a set:

        >>> unique_common_items = find_unique_common_items([1, 2, 3, 4], [2, 1])
        >>> isinstance(unique_common_items, set)
        True

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once:

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types:

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    # Method 1
    # items1 = set(items1)
    # items2 = set(items2)

    # print(set([items1 & items2]))
    # print(set([item for item in set(items1) & set(items2)]))

    # Method 2
    # Sudo- answer needs to be as a set- the first test tested for it.
        # Hance: the first set([]) operation- it MUST have two sets of ()
        # The result will be in regular []
    # Need to switch list to set in order to use set operations: 
            # Union:            items1 | items2
            # Intersection:     items1 & items2
            # Not intersection: items1 ^ items2
            # Diff:             items1 - items2 or items2 - items1
    
    # This will return a list:
    # print(([item for item in set(items1) & set(items2)]))
    # This will return a set:
    # print((set([item for item in set(items1) & set(items2)])))
    
    return (set([item for item in set(items1) & set(items2)]))


# def get_sum_zero_pairs(numbers):
#     """Given list of numbers, return list of pairs summing to 0.

#     Given a list of numbers, add up each individual pair of numbers.
#     Return a list of each pair of numbers that adds up to 0.

#     For example:

#         >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
#         [[-2, 2], [-1, 1]]

#         >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
#         [[-3, 3], [-2, 2], [-1, 1]]

#     This should always be a unique list, even if there are
#     duplicates in the input list:

#         >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
#         [[-2, 2], [-1, 1]]

#     Of course, if there are one or more zeros to pair together,
#     that's fine, too (even a single zero can pair with itself):

#         >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
#         [[-1, 1], [0, 0]]
#     """

#     # Sudo: 
#     # create an empty list 
#     # find unique values only by changing the type to set()
#     # Append the pair to the list as a nested collection
#     # return sorted list within a list for all pairs - abs() related

#     return []


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    # Sudo
    # create a dict w each char and the count- key, value pair!
    # sort the dict by value... use .items/ .values pair
    # return the list of char appears the most by using .keys()

    counts = {}
    # phrase = phrase.split(' ')
    list1 = []
    phrase = list(phrase)
    # print(phrase)
    # print(type(phrase))
    
    for letter in (phrase):
        counts[letter] = counts.get(letter, 0) + 1

    # print(counts)
    del counts[' ']
    del counts['.']
    # print(counts)

    for k, v in counts.items():
        newtup = (v, k)
        list1.append(newtup)
    
    list1 = sorted(list1, reverse = True)
    print(list1)

    # for k in list1:
    print(max(int(list1[k])))

    for v, k in list1[:1]:
        return([k])



    # return []

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()

