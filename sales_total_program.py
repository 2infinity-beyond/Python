'''
PE2 Module 4.3 Working with Real Files 
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''
#importing OS module
import os

# main function with starting total and count
def main():
    total = 0
    count = 0

    # opening the file in read mode and converting each line to a float to print, using a for loop
    try:
        with open("sales_totals.txt", "r") as file:
            for line in file:
                line_amount = float(line.strip())
                total += line_amount
                count += 1
                print(f"{line_amount:,.2f}")

    except IOError:
        print("An IOError has occured.")

    # printing a summary of the file, including final total, count and average
    print(f"\nTotal: {total:,.2f}")
    print(f"Number of entries: {count}")
    print(f"Average: {total / count:,.2f}")

main()
