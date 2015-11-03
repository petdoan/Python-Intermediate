
def count_words(text):
    """Returns a dictionary of the words and how many times the word
    appeard in the string passed in."""
    count = {}
    for word in text.split():
        '''ensure we always have a number by calling get with a second
        argument of 0, which causes the return value to be 0 if key is
        not already in the dict'''
        current = count.get(word, 0)
        count[word] = current + 1
    return count
 

