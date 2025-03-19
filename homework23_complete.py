'''
Homework23
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''
# function to group words by first letter
def group_by_first_letter(words):
    
    # creating empty dictionary to hold future keys and values
    dictionary = {}

    # list for first letters of words
    first_letters = []

    # for every word in the words provided 
    for word in words:
        first_letters.append(word[0]) # add the first letter of the word to the list 
        first_letters.sort() # sort the list of first letters
    
        # for each letter in the list of first letters
        for letter in first_letters:
             # if the letter is not already added to the dictionry
            if letter not in dictionary:
                dictionary[letter]= []  # add the first letter to the dictionary keys list
            
        # for each letter in the dictionary key, add related word
        dictionary[letter].append(word)  

    return dictionary
    pass

# function to converty list of words into a sentence
def convert_to_sentence(words):
    
    # Join the words with spaces in between
    sentence = " ".join(words)
    
    return sentence + "."
    pass

def main():
    group_by_first_letter()
    convert_to_sentence()

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest23.py'))