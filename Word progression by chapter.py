
def getFrequencyOfWord(file,word):
    file = open(file, 'rt')
    data = file.read()
    chapters = data.split('Chapter')
    print(len(chapters))
    frequencyByChapter = [0] * len(chapters)
    for i in range(len(chapters)):
      frequencyByChapter[i] = getFrequencyOfWordInChapter(chapters[i], word)
    return frequencyByChapter

def getFrequencyOfWordInChapter(chapter, word):
    count = 0
    chapterSplitByWord = chapter.split()
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for w in chapterSplitByWord:
        for p in punc:
            w=w.replace(p,'')
        if word==w:
            count += 1
    return count


print(getFrequencyOfWord('Pride_and_Prejudice.txt','love'))