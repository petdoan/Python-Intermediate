
def count_words(text, debug=False):
    """Returns a dictionary of the words and how many times the word
    appeard in the string passed in."""
    count = {}
    for word in text.split():
        if debug:
            print("incrementing count for '{}'".format(word))
        try:
            count[word] += 1
        except:
            if debug:
                print("'{}' not in dict, starting count at 1".format(word))
            count[word] = 1
    return count


