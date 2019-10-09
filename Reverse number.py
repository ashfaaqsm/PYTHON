while True: #loop to try again

    value = int(input("Enter number: ")) #user input

    numstring=str(value) #Converting integer to string

    rev=numstring[: : -1] #starting from the last value

    print("YOUR INPUT WAS:",value)

    print("IT'S REVERSE IS: ",rev)

    if numstring==rev: #output
        print("TRUE")

    else:
     print("FALSE") #output

    new=int(input("Do you want to continue(press 1 for yes , 2 for no): "))#user choice
    if new == 2:
        print("Program ended")
        break #end  the program
    else:
        print("Again") # restart the program

