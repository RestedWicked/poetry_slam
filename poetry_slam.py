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
    return (poem.join(poem_list_reversed))

print(lines_printed_backwards(get_file_lines("poem.txt")))

