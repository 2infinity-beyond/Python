'''
PE2 Module 4.1: Generators, iterators, and closures
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''



def two_letter_combinations(characters):

    # a nested loop: for each character in the range of the parameter, for each character
    for char in range(len(characters)): 
        for sub_char in range(len(characters)):

            # combine the two characters and yield all results
            yield characters[char] + characters[sub_char]


# main function provides the list to be used as the parameter
def main():
 
    characters = ['x', 'y', 'z', 'w', 'v']

    # creating an empty list to output the results into
    all_combos = []
    
    # loop to append the yielded results to the empty list
    for two_letter_combo in two_letter_combinations(characters):
        all_combos.append(two_letter_combo)
    
    print(all_combos)


main()