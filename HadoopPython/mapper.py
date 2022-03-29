#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re

def read_input(input):
    for line in input:
        # split the line into words; keep returning each word
        line = line.lower()
        line = re.sub(pattern='[^A-Za-z0-9]',repl=' ',string=line)
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    # print(data)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print('%s%s%d' % (word, separator, 1))
        for word in zip(words,words[1:]):
            print('%s %s%s%d' % (word[0],word[1], separator, 1))
        for word in zip(words,words[1:],words[2:]):
            print('%s %s %s%s%d' % (word[0],word[1],word[2], separator, 1))

# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
