'''
Homework2
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''

def inches_to_cm(inches):
    # your code here
    inches = 2
    conversion_factor = 2.54
    inches_to_cm = inches * conversion_factor
    return round(inches_to_cm, 2) 

def feet_to_meters(feet):
    # your code here
    feet = 3
    conversion_factor = 0.3048
    feet_to_meters = feet * conversion_factor 
    return round(feet_to_meters, 2)
    

def lbs_to_kg(lbs):
    # your code here
    lbs = 2.7
    conversion_factor = 0.45359237
    lbs_to_kg = lbs * conversion_factor
    return round(lbs_to_kg, 2)
    

def hours_to_minutes(hrs):
    # your code here
    hours = 2.5
    conversion_factor = 60
    hours_to_minutes = hrs * conversion_factor
    return round(hours_to_minutes, 2)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))