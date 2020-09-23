'''
Once each chapter is stored as an element in a String array, we can iterate through the array
to see if our quote is found inside the string that represents the chapter.

For many of the novels there were random line breaks \n throughout the text.
One way to navigate around this was to remove all the line breaks and spaces
so that a chapter is represented as one long string with no breaks.

'''
def getChapterQuoteAppears(file,quote):
    file = open(file, 'rt')
    data = file.read()
    chapters = data.split('Chapter')

    for i in range(len(chapters)):
        chapters[i]=chapters[i].replace("\n","").replace(' ','')
        if quote.replace('\n','').replace(' ','') in chapters[i]:
            return i
    return -1
print(getChapterQuoteAppears('Pride_and_Prejudice.txt','people themselves alter so much, that there is something new to be observed in them for ever.'))