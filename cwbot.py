# -*- coding: utf-8 -*-
import jieba
import re
import nltk

inputtext = open("onecorpus.txt", "r")


def processText(rawtext, sentCor):
    rawtext = unicode(rawtext, 'utf-8')
    rawtext = re.sub(ur"^陳雲：", '', rawtext.rstrip("\n"))
    seg_list = jieba.cut(rawtext)
    sentCor.append(" ".join(seg_list))

sentCor = []
for i in inputtext:
    if i != "\n":
        processText(i, sentCor)

content_text =  ' '.join(sentCor)
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')

tokenized_content = tokenizer.tokenize(content_text)
content_model = nltk.NgramModel(4, tokenized_content)


def chinwanBot(content_model):
    starting_words = content_model.generate(100)[-2:]
    randomsentence = content_model.generate(70, starting_words)
    for i in range(0, len(randomsentence)):
        if re.match(ur'[A-Za-z]+$', randomsentence[i]):
            randomsentence[i] = randomsentence[i] + " "
    puncIndex = [i for i, x in enumerate(randomsentence) if any(thing in x for thing in [u'。', u'！', u'？'])]
    startingIndex = min(puncIndex) + 1
    endingIndex = max(puncIndex) + 1
    return "".join(randomsentence[startingIndex:endingIndex])


#import pickle
#pickle.dump(chinwanBot(content_model), open("example.p", "wb"))

randomText = open('randomText.txt', 'w')
for i in range(0, 1000):
    try:
        ranText = chinwanBot(content_model)
        if ranText != "\n":
            randomText.write(chinwanBot(content_model).encode('utf-8') + "\n")
    except:
        pass
randomText.close()


inputtext.close()

