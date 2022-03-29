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
    total_prob_us= os.environ.get('united states')
    data = read_mapper_output(sys.stdin, separator=separator)
    highest_prob = 0
    # groupby groups multiple word-count pairs by word
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, itemgetter(0)):
         
        filtered_list = list(filter(currentword, "united states"))                    
        for current_word,count in group:
            highest_prob1 = max(int(count)/int(total_prob_us)
            if highest_prob1 > highest_prob:
                highest_prob= highest_prob1
        print(current_word, separator, highest_prob)
        

if __name__ == "__main__":
    main()
