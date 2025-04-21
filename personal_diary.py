'''
PE2 Module 4.2 Processing Files 
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''


# defining a function to check the diary (extra)
def read_diary():

    # open file in read mode, then print it out
    try:
        read_it = open("diary.txt", "r")    

        entries = read_it.read()
        print(entries)
    
    # handling any exceptions 
    except FileNotFoundError:
        print ("File Not Found")
    except Exception as e:
        print ("An error occured", e)

# defining a main function to append new entries to the diary       
def main():

    # prompt user for time and date first, then their entry
    timestamp = input("\nEnter the current date and time:\n\n")
    diary_entry = input("\nWrite a note in your diary:\n\n")
    
    # open and append the user-provided information to the diary
    with open("diary.txt", "a") as file:
        file.write(f"\n\n{timestamp} \n\n {diary_entry}")
    
    # appending complete, closing file
    file.close()


main()

#read_diary()

'''
*** HASH THE "main()" FUNCTION AND
UNHASH THE "read_diary()" FUNCTION 
TO READ THE DIARY!!!
'''