'''
PE2 Module 4.4: The OS Module
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''

import os

def main():

    # making main directory 
    os.mkdir("MyFiles")

    # making subdirectories inside main directory
    os.mkdir("MyFiles/Docs")
    os.mkdir("MyFiles/Images")
    os.mkdir("MyFiles/Videos")

main()