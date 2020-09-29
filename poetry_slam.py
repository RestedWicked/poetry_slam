import random

def get_file_lines(filename):
    infile = open(filename ,"r")

    poem_list = []
    for line in infile:
        poem_list.append(line)
    infile.close()
    return(poem_list)

def lines_printed_backwards(lines_list):
    poem_list_reversed = []
    index = 0
    for line in lines_list:
        index += 1
        indexed_line = str(index)+" "+line
        poem_list_reversed.append(indexed_line)
    poem_list_reversed.reverse()
    poem = " "
    print(poem.join(poem_list_reversed))

def lines_printed_random(lines_list):
    poem_list_randomized = []
    for line in (lines_list):
        poem_list_randomized.append(line)
    random.shuffle(poem_list_randomized)
    poem = " "
    print(poem.join(poem_list_randomized))

def lines_printed_custom(lines_list):
    lines_list.sort(key=len, reverse=True)
    for line in (lines_list):
        print(line.strip("\n"))
