from collections import defaultdict
import random

def preprocess(word):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for p in punc:
        word=word.replace(p, '')
    return word
def generateSentence(word, file):
    output_sentence =[word]
    file = open(file, 'rt')
    data = file.read()

    def generateSentence_helper(word):
        d = getCommonWords(word, data)
        #mostCommonWord = max(d, key = d.get)
        return random.choice(list(d.keys()))

    for _ in range(20):
        common_word =generateSentence_helper(word)
        output_sentence.append(common_word)
        word = common_word
    return ' '.join(output_sentence)


def getCommonWords(word,data):
    data =data.split()
    common_words = defaultdict(int)
    for i,w in enumerate(data):
        if word==preprocess(w) and i+1<len(data):
            common_words[preprocess(data[i+1])] += 1
    return common_words

print(generateSentence('Elizabeth', 'Pride_and_Prejudice.txt'))