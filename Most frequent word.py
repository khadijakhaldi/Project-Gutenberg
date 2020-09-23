from collections import defaultdict
def get20MostFrequentWords(file):
    file = open(file, 'rt')
    data = file.read()
    words= data.split()
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    d = defaultdict(int)
    for w in words:
        for p in punc:
            w = w.replace(p,'')
        d[w.lower()] += 1
    words = []
    for key, value in d.items():
        words.append([key,value])
    words.sort(key= lambda x: x[1], reverse = True)
    return words[:20]

def get20LeastFrequentWords(file):
    file = open(file, 'rt')
    data = file.read()
    words= data.split()
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    d = defaultdict(int)
    for w in words:
        for p in punc:
            w = w.replace(p,'')
        d[w.lower()] += 1
    words = []
    for key, value in d.items():
        words.append([key,value])
    words.sort(key= lambda x: x[1])
    return words[:20]
print(get20MostFrequentWords('Pride_and_Prejudice.txt'))
print(get20LeastFrequentWords('Pride_and_Prejudice.txt'))