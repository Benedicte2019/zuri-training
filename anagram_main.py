# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    # converting letters to lowercase
    word = word.lower()
    anagram = anagram.lower()

    # converting the given words to a list of characters
    list_w = list(word)
    list_anagr = list(anagram)

    # sorting list
    list_w = set(list_w)
    list_anagr = set(list_anagr)

    if(list_w != list_anagr):
        return False
    elif(list_w == list_anagr):
        return True

print(find_anagram("listen", "silant"))