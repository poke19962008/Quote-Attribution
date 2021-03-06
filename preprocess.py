'''
 Preprocessing Class
 Clean and process the raw files into <sess>.cleaned.bin

 Methods:
    cleanFile(): for a given file name it cleans and process data
    cleanName(): process speaker names
    cleanDial(): clean and process the dialogue
    tokenizeQuote(): tokenize the quote by words
'''

import pickle, os, re
import nltk
from config import Config

class Preprocess:

    def cleanFile(self, fname):
        script = open(fname, 'r').read().split('\n')
        cleaned = []
        for i in xrange(len(script)):
            row = script[i].split("\t")
            row[1] = self.cleanName(row[1])
            row[2] = self.cleanDial(row[2])
            cleaned.append([row[1], self.tokenizeQuote(row[2])])

        pickle.dump(cleaned, open("./data/cleaned.bin", 'wb'))
        del cleaned, script
        print "[SUCCESS] Cleaned at ./data/cleaned.bin"

    def cleanName(self, name):
        return name.strip().lower()

    def cleanDial(self, d):
        if not isinstance(d, list):
            d = d.strip().lower()
            d = re.sub(r'(\.\.+)|"|:|;', ' ', d) # Remove Multiple Spaces & Special ch.
            d = re.sub(r'\s*\([^)]*\)', '', d) # Remove bracket and it's content
            d = re.sub(r'\s+', ' ', d) # Remove Multiple Spaces
            return d.strip()
        else:
            return d

    def tokenizeQuote(self, quote):
        if not isinstance(quote, list):
            return nltk.word_tokenize(quote)
        else:
            return quote

if __name__ == '__main__':
    Preprocess().cleanFile(Config().rawData)
