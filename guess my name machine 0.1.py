#GUESS MY NAME MACHINE (SELF MADE IDEA AND NO TUTORIALS)
name = "gabriel"
input
inputoffind = input("Write a Letter to know where it is located in my name: ")
#checking if the input is a digit or not
inputoffind.isdigit()
#if it's not a digit run the programm
if inputoffind.isdigit() == False: 
    name_letter_find = name.find(inputoffind.lower())
    if name_letter_find == -1:
        print("The Letter that you have picked does not exist in my Name.")
    else:
        print("The Letter you have chosen is in spot " ,name_letter_find + 1)
#if input is a digit then don't proceed
else:
    print("Try Again")