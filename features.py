# -*- coding: utf-8 -*-
# encoding=utf8

import pandas as pd
import numpy as np
import re
import difflib

def countVowels(string):
    vowel = ("aıioöuüAEIİOÖUÜ")
    count = 0
    for i in string:
        if i in vowel:
            count += 1
    return count


def countCons(string):
    cons = ("bcçdfgğhjklmnprsştyzBCÇDFGĞHJKLMNPRSŞTVYZ")
    count = 0
    for i in string:
        if i in cons:
            count += 1
    return count

def hasPunctuation(word):
    words = []
    checker = 0
    for x in word.split(" "):
        words.append(x)

    # çoklu kelimeler icin kelimeleri ayirdik
    for y in range(0, len(words)):
        # sadece alfabetik karakter icerirse checker 1
        if (words[y].isalpha() == False):
            checker = 1
            break

    #print("hasPunc:", checker)
    return checker

def hasEmoticon(word):
    emoticons = [':)', ':(', ';)', ':O', ':D', ':P', ':@', ':S', ':$', 'B)', ':\'(', ':*', '>:)', 'O:)', ':/', ':|',
                 ':B', ':SS', ':))', '8)', ':&', ':?', '<3', '(u)']
    checker = 0

    for i in range(0, len(emoticons)):
        if emoticons[i] in word:
            checker = 1
            break

    #print("hasEmoticon:", checker)
    return checker

def hasVowel(word):
    vowel = ("aıioöuüAEIİOÖUÜ")
    hasVowel = 0
    for i in range(0, len(word) - 1):
        if (word[i] == word[i + 1]):
            if word[i] in vowel:
                hasVowel = 1

    return hasVowel

def hasConsonant(word):
    cons = ("bcçdfgğhjklmnprsştyzBCÇDFGĞHJKLMNPRSŞTVYZ")
    hasCons=0

    for i in range(0, len(word) - 1):
        if (word[i] == word[i + 1]):
            if word[i] in cons:
                hasCons = 1
    return hasCons

def containNumber(tweet):
    cnt = 0
    digitLst = []
    wordLst = tweet.split(" ")
    for word in wordLst:
        if (word.isdigit()):
            digitLst.append(word)
        else:
            for i in range(len(word)):
                if(word[i].isdigit()):
                    digitLst.append(word[i])

    #print("Bu tweet %d tane rakam iceriyor" %len(digitLst))
    #for digit in digitLst:
        #print(digit)
    return len(digitLst)

def hasHashtag(tweet):
    if(tweet.find('#')>=0):
        hashtagLst =1
    else:
        hashtagLst=0

    return hashtagLst

def hasMention(tweet):

    if(tweet.find('@')>=0):
        mentionLst =1
    else:
        mentionLst=0
    return mentionLst

def hasRT(tweet):

    if(tweet.find('RT')>=0):
        RTLst =1
    else:
        RTLst=0
    return RTLst


def hasUrl(tweet) :
    urlLst = re.findall(r'(https?://[^\s]+)', tweet)
    #print("Bu tweette %d adet url var" % len(urlLst))

    return urlLst;

def mostUsedWord(tweet):
    wordLst = tweet.split(" ")

    for i in range(len(wordLst)):
        if wordLst[i] in tweet:
            return wordLst[i]
        else:
            return ''


def FindNumberOfWord(tweet):
    words_tweet = tweet.split(" ")
    return len(words_tweet)

def main():
    data = {
        'Word Before': [''],
        'WB Stem': [''],
        'WB POS Tag': [''],
        'WB Letter': [''],
        'WB Letter Diff Stem': [''],
        'WB Is Capital': [''],
        'WB Is All Capital': [''],
        'WB Has Punct BA': [''],
        'WB Has Emot BA': [''],
        'WB Has Double Consonant': [''],
        'WB Has Double Vowel': [''],
        'WB Has Harmony': [''],
        'WB Cons Vow Ratio': [''],
        'WB Contain Number': [''],
        'WB Has Hashtag': [''],
        'WB Has Url': [''],

        'Word': [''],
        'W Stem': [''],
        'W POS Tag': [''],
        'W Letter': [''],
        'W Letter Diff Stem': [''],
        'W Is Capital': [''],
        'W Is All Capital': [''],
        'W Has Punct BA': [''],
        'W Has Emot BA': [''],
        'W Has Double Consonant': [''],
        'W Has Double Vowel': [''],
        'W Has Harmony': [''],
        'W Cons Vow Ratio': [''],
        'W Contain Number': [''],
        'W Has Hashtag': [''],
        'W Has Url': [''],

        'Word After': [''],
        'WA Stem': [''],
        'WA POS Tag': [''],
        'WA Letter': [''],
        'WA Letter Diff Stem': [''],
        'WA Is Capital': [''],
        'WA Is All Capital': [''],
        'WA Has Punct BA': [''],
        'WA Has Emot BA': [''],
        'WA Has Double Consonant': [''],
        'WA Has Double Vowel': [''],
        'WA Has Harmony': [''],
        'WA Cons Vow Ratio': [''],
        'WA Contain Number': [''],
        'WA Has Hashtag': [''],
        'WA Has Url': ['']
    }

    data2 ={
        'Tweet': [''],
        'Tweet has Punct BA': [''],
        'Tweet has Emot BA': [''],
        'Tweet has Hashtag': [''],
        'Tweet has Mention': [''],
        'Tweet has Url': [''],
        'Frequently used word': [''],
        'Tweet FAV Ratio': [''],
        'Tweet RT Ratio': [''],
        'Tweet Has Location': [''],
        'Tweet Has Checkin': [''],
        'Tweet From Mobile Device': [''],
        'Length of tweet as # of words': [''],
        'Length of tweet as # of characters': [''],
    }

    words = []
    tweet=[]
    with open('tweet1.txt', 'r') as f:
        for line in f:
            tweet.append(line)
            for word in line.split():
                words.append(word)

    df = pd.DataFrame(data, index=words)
    df2=pd.DataFrame(data2, index=tweet)

    print('.....')
    """for i, row in df.iterrows():
        row['Word'] = i
        row['W Stem'] = i
        row['W POS Tag'] = 'X'
        row['W Letter'] = len(i)
        row['W Letter Diff Stem'] = len(i) - len(i)
        row['W Is Capital'] = i.istitle()
        row['W Is All Capital'] = i.isupper()
    print (df)
    """

    print('XXXX XXXX')

    for j in range(df.size):

        """ Word Before """
        df.iloc[j]['Word Before'] = df.index[j - 1]
        df.iloc[j]['WB Stem'] = df.index[j - 1]
        df.iloc[j]['WB POS Tag'] = 'X'
        df.iloc[j]['WB Letter'] = len(df.index[j - 1])
        df.iloc[j]['WB Letter Diff Stem'] = len(df.index[j - 1]) - len(df.index[j - 1])
        df.iloc[j]['WB Is Capital'] = df.index[j - 1].istitle()
        df.iloc[j]['WB Is All Capital'] = df.index[j - 1].isupper()
        df.iloc[j]['WB Has Punct BA'] = hasPunctuation(df.index[j - 1])
        df.iloc[j]['WB Has Emot BA'] = hasEmoticon(df.index[j - 1])
        df.iloc[j]['WB Has Double Consonant'] = hasConsonant(df.index[j - 1])
        df.iloc[j]['WB Has Double Vowel'] = hasVowel(df.index[j - 1])
        df.iloc[j]['WB Has Harmony'] = ''
        df.iloc[j]['WB Contains Number'] = containNumber(df.index[j - 1])
        df.iloc[j]['WB Has Hashtag'] = hasHashtag(df.index[j - 1])
        df.iloc[j]['WB Has Url'] = hasUrl(df.index[j - 1])
        if (countVowels(df.index[j - 1]) > 0):
            df.iloc[j]['WB Cons Vow Ratio'] = countCons(df.index[j - 1]) / countVowels(df.index[j - 1])
        else:
            df.iloc[j]['WB Cons Vow Ratio'] = 0


        """ Word """
        df.iloc[j]['Word'] = df.index[j]
        df.iloc[j]['W Stem'] = df.index[j]
        df.iloc[j]['W POS Tag'] = 'X'
        df.iloc[j]['W Letter'] = len(df.index[j])
        df.iloc[j]['W Letter Diff Stem'] = len(df.index[j]) - len(df.index[j])
        df.iloc[j]['W Is Capital'] = df.index[j].istitle()
        df.iloc[j]['W Is All Capital'] = df.index[j].isupper()
        df.iloc[j]['W Has Punct BA'] = hasPunctuation(df.index[j])
        df.iloc[j]['W Has Emot BA'] = hasEmoticon(df.index[j])
        df.iloc[j]['W Has Double Consonant'] = hasConsonant(df.index[j])
        df.iloc[j]['W Has Double Vowel'] = hasVowel(df.index[j])
        df.iloc[j]['W Has Harmony'] = ''
        df.iloc[j]['W Contains Number'] = containNumber(df.index[j])
        df.iloc[j]['W Has Hashtag'] = hasHashtag(df.index[j])
        df.iloc[j]['W Has Url'] = hasUrl( df.index[j])
        if (countVowels(df.index[j]) > 0):
            df.iloc[j]['W Cons Vow Ratio'] = countCons(df.index[j]) / countVowels(df.index[j])
        else:
            df.iloc[j]['W Cons Vow Ratio'] = 0

        """ Word After """
        df.iloc[j]['Word After'] = df.index[j + 1]
        df.iloc[j]['WA Stem'] = df.index[j + 1]
        df.iloc[j]['WA POS Tag'] = 'X'
        df.iloc[j]['WA Letter'] = len(df.index[j + 1])
        df.iloc[j]['WA Letter Diff Stem'] = len(df.index[j + 1]) - len(df.index[j + 1])
        df.iloc[j]['WA Is Capital'] = df.index[j + 1].istitle()
        df.iloc[j]['WA Is All Capital'] = df.index[j + 1].isupper()
        df.iloc[j]['WA Has Punct BA'] = hasPunctuation(df.index[j + 1])
        df.iloc[j]['WA Has Emot BA'] = hasEmoticon(df.index[j + 1])
        df.iloc[j]['WA Has Double Consonant'] = hasConsonant(df.index[j + 1])
        df.iloc[j]['WA Has Double Vowel'] = hasVowel(df.index[j + 1])
        df.iloc[j]['WA Has Harmony'] = ''
        df.iloc[j]['WA Contains Number'] = containNumber(df.index[j + 1])
        df.iloc[j]['WA Has Hashtag'] = hasHashtag(df.index[j + 1])
        df.iloc[j]['WA Has Url'] = hasUrl(df.index[j + 1])
        if (countVowels(df.index[j + 1]) > 0):
            df.iloc[j]['WA Cons Vow Ratio'] = countCons(df.index[j + 1]) / countVowels(df.index[j + 1])
        else:
            df.iloc[j]['WA Cons Vow Ratio'] = 0

        if (j == 370):
            break

    for i in range(len(df2)):
        df2.iloc[i]['Tweet'] = df2.index[i]
        df2.iloc[i]['Tweet has Punct BA'] =hasPunctuation(df2.index[i])
        df2.iloc[i]['Tweet has Emot BA'] = hasEmoticon(df2.index[i])
        df2.iloc[i]['Tweet has Hashtag'] = hasHashtag(df2.index[i])
        df2.iloc[i]['Tweet has Mention'] = hasMention(df2.index[i])
        df2.iloc[i]['Tweet has Url']=hasUrl(df2.index[i])
        df2.iloc[i]['Frequently used word'] ='X'
        df2.iloc[i]['Tweet FAV Ratio'] = 'X'
        df2.iloc[i]['Tweet RT Ratio'] = hasRT(df2.index[i])
        df2.iloc[i]['Tweet Has Location'] = 'X'
        df2.iloc[i]['Tweet Has Checkin'] = 'X'
        df2.iloc[i]['Tweet From Mobile Device'] = 'X'
        df2.iloc[i]['Length of tweet as # of words'] = len(df2.index[i].split())
        df2.iloc[i]['Length of tweet as # of characters'] = len(df2.iloc[i]['Tweet'])

    print(df2.iloc[0])

    print('.....')


main()