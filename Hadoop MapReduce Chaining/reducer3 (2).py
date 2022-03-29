#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys
import os

# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    total_unigram = 8392040
    total_bigram = 8383096
    total_trigram = 8387568
    data = read_mapper_output(sys.stdin, separator=separator)

    # groupby groups multiple word-count pairs by word
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            if(current_word=='U'):
                for a,current_word,count in group:
                    unigram_prob = int(count)/int(total_unigram)
                    print("%s%s%.15f" % (current_word, separator, unigram_prob))
            
            elif(current_word=='B'):
                for a,current_word,count in group:
                    bigram_prob = int(count)/int(total_bigram)
                    print("%s%s%.15f" % (current_word, separator, bigram_prob))    
            
            else:
                for a,current_word,count in group:
                trigram_count = int(count)/int(total_trigram)
                print("%s%s%.15f" % (current_word, separator, trigram_prob))        
                
        except ValueError:
            # count was not a number, so silently discard this item
            pass

if __name__ == "__main__":
    main()
