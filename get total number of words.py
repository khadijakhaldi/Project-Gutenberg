from collections import defaultdict
def getTotalNumberOfLines(file):
    lines= []
    with open(file,"r") as f:
        for line in f:
            line = line.strip()
            lines.append(line)
    print(lines)
    return len(lines)

def getTotalNumberOfWords(file):
    file = open(file, 'rt')
    data = file.read()
    words= data.split() #split word by white spaces
    return len(words)
def getTotalUniqueWords(file):
    file = open(file, 'rt')
    data = file.read()
    words= data.split()
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    d = defaultdict(int)
    for w in words:
        for p in punc:
            w = w.replace(p,'')
        d[w.lower()] += 1
    print(d)
    return len(d)
#print(getTotalNumberOfWords('Pride_and_Prejudice.txt'))
print(getTotalUniqueWords('Pride_and_Prejudice.txt'))
