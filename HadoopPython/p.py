def read_input(input, separator='\t'):
    with open('abc.txt') as f:
        lines = f.readlines()
    for line in lines:
        # print(line.rstrip().split(separator, 1))
        yield line.rstrip().split("       ", 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input("abc.txt")
    try:
        for words in data:
            current_word = words[0]
            count = words[1]
            if(len(current_word.split())==1):
                print("%s%s%d" % (current_word,separator,int(count)))
            elif(len(current_word.split())==2):
                print("%s%s%d" % (current_word,separator,int(count)))
            else:
                print("%s%s%d" % (current_word,separator,int(count)))                
    except ValueError:
            # count was not a number, so silently discard this item
        pass
# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()

