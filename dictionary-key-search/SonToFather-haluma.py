#This program allows you to search for a person's father

#programed by Hethur Aluma | 2/13/20

fathers = {"son1": "dad1",
          "dad1": "grandpa1",
          "son2": "dad2",
          "dad2": "grandpa2",
          "John Quincy Adams": "John Adams",
          "John Adams": "John Adams Sr.",
          "Bart Simpson": "Homer Simpson",
           "Homer Simpson": "Grandpa Simpson"}

choice = None

while choice != "0":
    print (
    """
    Father Finder

    0 - Quit
    1 - Find a Father
    2 - Find a Grandfather
    3 - List all of the sons/keys
    """
    )
    
    choice = input("Choice:")
    print()

    #exit
    if choice == "0":
        print("Good-bye")

    #find the name of the key's father
    elif choice == "1":
        son = input("What is the name of the son?")
        son = son.title()

        if son in fathers:
            print("The name of the father is:", fathers[son])
        else:
            print("I don't know who their father is.", son, " is not in the dictionary.")


    #find the name of the key's grandfather
    elif choice == "2":
        grandson = input("What is the name of the grandson?")
        grandson = grandson.title()


        if grandson in fathers:
            son = fathers[grandson]
            print("The name of the father is:", fathers[son])
        else:
            print("I don't know who their grandfather is.")

    #provide names of all sons/keys
    elif choice == "3":
        for i in fathers:
            print ("The father of:", i, "is", fathers[i])

    #some unknown choice
    else:
        print("Sorry, but ", choice, "isn't a valid choice.")

input("Hit enter to exit.")
