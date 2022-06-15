import operator
from django.shortcuts import render
import time


def home(request):
    return render(request, 'home.html', {'on': 'active'})


def counterTxt(request):
    text = request.POST['texttocount']
    if text != '':
        i = True
        return render(request, 'counter.html',
                      {'wordlistlen': TakeSolution(text)[0], 'SentenceLen': FindSentence(text), 'ReadingTime': TakeSolution(text)[4], 'CharListLen': TakeSolution(text)[1], 'SortedWordListCountDict': TakeSolution(text)[2], 'text': TakeSolution(text)[3], 'i': i, 'on': 'active'})
    else:
        return render(request, 'home.html', {'on': 'active'})
        
def counterFile(request):
    text = request.FILES['txtFile'].read()
    text = text.decode()
    text = ''.join(map(str, text))
    if text != '':
        i = True
        return render(request, 'counter.html',
                      {'wordlistlen': TakeSolution(text)[0], 'SentenceLen': FindSentence(text), 'CharListLen': TakeSolution(text)[1],
                       'SortedWordListCountDict': TakeSolution(text)[2], 'ReadingTime': TakeSolution(text)[4], 'text': TakeSolution(text)[3], 'i': i, 'on': 'active'})
    else:
        return render(request, 'home.html', {'on': 'active'})


def TextPreProcessing(text):
    punc = '''!()-[];:'"\,<>./?@#$%^&*_~`'''
    text = text.lower()
    for ele in punc:
        if ele in text:
            text = text.replace(ele, "")
    return text


def SplitTextToWord(text):
    return text.split()


def SplitTextToChar(text):
    return len(text)


def FindSentence(text):
    import re
    return len(re.findall(r"[A-Z].*?([.?!])", text))


def TakeSolution(data):
    s = time.time()
    CharListLen = SplitTextToChar(TextPreProcessing(data))
    wordlist = SplitTextToWord(TextPreProcessing(data))
    wordlistlen = len(wordlist)
    wordlistCountDict = {}
    for word in wordlist:
        if word in wordlistCountDict:
            wordlistCountDict[word] += 1
        else:
            wordlistCountDict[word] = 1

    SortedWordListCountDict = sorted(wordlistCountDict.items(), key=operator.itemgetter(1), reverse=True)
    ReadingTime = time.time() - s
    return wordlistlen, CharListLen, SortedWordListCountDict, data, round(ReadingTime, 7)
