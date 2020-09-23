'''
 We want to create a simple autocomplete-like feature where we can input one or more words, and be returned a list of all sentences that can start with our input.
'''
from collections import defaultdict
class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = defaultdict()
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
        self.word_list = []

    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')
    def insert(self, key):
        root = self.root
        lenght= len(key)
        for i in range(lenght):
            index =self._charToIndex(key[i])
            if index not in root.children:
                root.children[index] = TrieNode()
            root= root.children[index]
        root.isEndOfWord = True

    def search(self, word):
        root = self.root
        len = len(word)
        for i in range(len):
            index = self._charToIndex(word[i])
            if index not in root.children:
                return False
            root = root.children[index]
        return root
    def preprocess(self,word):
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for p in punc:
            word=word.replace(p, '')
        return word
    def read_novel(self,file):

        file = open(file, 'rt')
        data = file.read()
        return data
    def form_trie(self,file):
        '''
        input: startOfSentence
        returns: list of strings that starts with the inputs
        '''
        data = self.read_novel(file)
        #Build Trie
        trie = Trie()
        for word in data:
            word = self.preprocess(word)
            trie.insert(word)
        #after insertin all words
        #we will search for the key
    def printAutoSuggetsion(self,prefix):
        root =self.root
        not_found = False
        temp_word =''

        for a in list(prefix):
            if a not in root.children:
                return 0
            temp_word += a
            root = root.children[a]
        if not root.children or root.isEndOfWord:
            return -1
        self.suggestionRes(root,temp_word)
        return self.word_list

    def suggestionRes(self,node,word):
        if node.isEndOfWord:
            self.word_list.append(word)
        #n  are childreen and a is the letter
        for a,n in node.childreen.items():
            self.suggestionRes(n,word+a)
