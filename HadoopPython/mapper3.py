#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re

def read_input(input):
    for line in input:
        # split the line into words; keep returning each word
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for current_word, count in data:
        try:
            if(len(current_word.split())==1):
                for current_word, count in group:
                    print("%s%s%d" % (unigram, separator, count))
            elif(len(current_word.split())==2):
                for current_word, count in group:

                    print("%s%s%d" % (biigram, separator, count))
            else:
                print("%s%s%d" % (trigram, separator, count))                
        except ValueError:
            # count was not a number, so silently discard this item
            pass
# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
