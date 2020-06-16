# I imported database as per the instructions.
from database import Simpledb
    
# I assigned filename to the name of the file, so that it is easier to reference to later.
filename = 'phonedirectory.txt'

choice = ''
v = ''
phoenumber = ''


#This function gets the choice of the user on what they want to do in the phone directory.
def getChoice():
    
    choice = ''

# This while loop makes sure that they enter a valid choice. It will keep asking the user until they do so.
    while choice != 'a' and choice != 'f' and choice != 'd' and choice != 'u' and choice != 'q' and choice != 'A' and choice != 'F' and choice != 'D' and choice != 'U' and choice != 'Q':
        print()
        print ("Welcome to the telephone directory!. Please enter the letter for what you want to do now:\nAdd a number-a\nFind a number-f\nDelete a number-d\nUpdate a number-u\nQuit the directory-q")
        choice = input()
        
    return choice

# This function will execute what is needed to be done based on the choice.
def calls(choice):
# If "a" is chosen, it will ask for a name and number to be added.
    if choice == 'a' or choice == 'A':
        name = input("What is the name of the person?")
        phonenumber = input("What is their number?")
        mydirectory = Simpledb(filename,name,phonenumber)
        mydirectory.insert()
        text = mydirectory.__repr__()
        print (text)
        print ("The text above shows the name, phonenumber, and filename that was added.")
        
# If "f" is chosen, it will ask for the name and see whether or not there is a phonenumber available to print.       
    if choice == 'f' or choice == 'F':
         phonenumber = ''
         name = input("What is the name of the person whose number you are trying to find?")
         v = Simpledb (filename,name,phonenumber)
         j = v.select_one()
         
         
         text = v.__repr__()
         if j == 'Not Found':
             print ("Not found. We are sorry.")
         else:
              print (text)
              
              print ("Find Completed! We found the name with the number above in the file listed.")

                  

# If "d" is chosen, it will ask for the name and decide whether or not it can be deleted.
    if choice == 'd' or choice == 'D':
        phonenumber = ''
        name = input("What is the name of the person whose number you are trying to delete?")
        z =Simpledb(filename, name,phonenumber)
        j = z.delete()
        text = z.__repr__()
        if j == "Not Found!":
            print ('Not found')
        else:
            print (text)
            print ('Found and Deleted! We deleted this name and number from the file listed.')

#If "u" is chosen, it will ask for the name and decide whether an updated number is possible or not.
    if choice == 'u' or choice == 'U':
        phonenumber = ''
        name = input ("What is the name of the person whose number you are trying to update?")
        v = Simpledb(filename, name, phonenumber)
        b = v.select_one()
        if b == "Not Found":
            print ("Not found!")             
        else:
            phonenumber = input ("What is the new number of this person?")
            b = Simpledb(filename,name,phonenumber)
            b.update()
            text  = b.__repr__()
            print (text)
            print ("Completed! It has been successfully updated with the new number " +phonenumber )

#This is the loop that keeps going back to the place where they can select what they want to do until "q" is selected.
while True:
    choice = getChoice()
    calls(choice)
    if choice == 'q' or choice == 'Q':
        break




