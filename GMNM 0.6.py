#GUESS MY NAME MACHINE 0.6 (SELF MADE IDEA AND NO TUTORIALS but needed some help from Stackoverflow)
import random

names = ["Gabriel", "Aaron", "Kiano", "Liam", "Sebastian", "Felix", "Hector", "Lennart", "Tobias", "Vincent"]

while True:
    get_out = False             # Used to exit this program gracefully
    name_choice = random.choice(names)
    name_letter_find = random.choice(names) # Acquire the name randomly before performing tests
    #print(name_choice)
    guessesList = [] 
    guesses = 0

    for i in range(10):   
        inputoffind = input("Write a Letter to know where it is located in the name you've been given: ")
        print(guessesList)
        
        if inputoffind == '0':          # Done with the program
            get_out = True
            exit()      
            
        #if inputoffind == '1':          # Try another name
            
        inputoffind.isdigit()
#        print(inputoffind.lower())
        name_letter_find = name_choice.lower().find(inputoffind.lower())    # Need to make sure both letters are lower case
        
#        print(name_letter_find)
        if inputoffind.isdigit() == False:
            if inputoffind.isalpha() == True:
                if len(inputoffind) == 1:
                    if name_letter_find == -1:
                        print("The Letter that you have picked does not exist in my Name.")
                        guesses += 1
                        print("You have ",10 - guesses, " tries left!")
                        if inputoffind not in guessesList:
                            guessesList.append(inputoffind)
                    else:
                        print("The Letter you have chosen is in spot " ,name_letter_find + 1)
                        guesses += 1
                        print("You have ",10 - guesses, " tries left!")
                        if inputoffind not in guessesList:
                            guessesList.append(inputoffind)
                else:
                    print("Try Again")
                    break
        else:  
            print("Try Again")
    final_guess = input("What is the name? : ")
    if final_guess.lower() == name_choice.lower():
        print("You Won!")
        break
    else:
        print("You lost! The correct answer was :", name_choice)
        break
        
# I want to inpliment a better names list. And lastly I'd make it have a UI with ktinker where it reveals the letters you write like hangmanchen and impliment tips aswell

#Limited tries CHECK
#Tries left CHECK
#Name and Win CHECK
#List for guesses CHECK
#Only one letter CHECK
#Get out of Programm with 0 CHECK
#Try another name (POSTPONED cause of tk)
