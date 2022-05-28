# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    f = open(filename, "r")
    content = f.read()
    
    return content

def count_words():
    text = read_file_content("./story.txt")

    # [assignment] Add your code here
    # initialize an empty dictionary 
    dictionary = dict()

    punc = ".?,!:{}[]"
    # remove punctuation

    for p in punc:
        if p in text:
            text = text.replace(p, "")
    
    text = text.lower()

    lines = text.split()

    for w in lines:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return dictionary

print(count_words())