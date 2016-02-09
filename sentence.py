class Sentence():
    def __init__(self, text):
        self.text = text
        self.words = text.split()

    def __repr__(self):
        return repr(self.text)

    def __getitem__(self, index):
        return self.words[index] 

    def __len__(self): 
        return len(self.words)

    def __add__(self, other):
        '''Allow one Sentence to be added to another.'''
        return Sentence(self.text + ' ' + other.text)

