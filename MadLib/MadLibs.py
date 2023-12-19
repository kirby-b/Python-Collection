class MadLibs:
    
    #Normal MadLibs
    def SimpleMadLibModeFunc():
        import random
        print("Welcome To MadLib. I will give you a prompt and then ask for three inputs(they will be inserted at the capitalized words in parentheses).\n")
        s1 = "___"
        s2 = "___"
        s3 = "___"
        format = random.randrange(1,10)
        if format == 1:
            print("\"NAME\" went to the \"NOUN\" with their \"NOUN\".\n")
        if format == 2:
            print("\"NAME\" is captain of the \"NOUN\" in \"ADJECTIVE\"city.\n")
        if format == 3:
            print("The \"ADJECTIVE\" \"COLOR\" fox jumped over the \"ADJECTIVE\" dog.\n")
        if format == 4:
            print("If you only knew the \"NOUN\" of the dark side. \"NAME\" never told you what happened to your \"NOUN\".\n")
        if format == 5:
            print("\"NAME\" is a famous japanese character whos power is \"ACTION\"ing enemies with his \"NOUN\".\n")
        if format == 6:
            print("\"NOUN\" scientists study \"NOUN\"\'s effect on \"NOUN\".\n")
        if format == 7:
            print("It\'s \"NOUN\" O'clock and im feeling like \"ADJECTIVE\" \"NOUN\"\'s.\n")
        if format == 8:
            print("The best way to stay \"ADJECTIVE\" is to \"ACTION\" \"NOUN\" everyday.\n")
        if format == 9:
            print("I \"ACTION\" my \"NOUN\" everyday like a \"ADJECTIVE\".\n")
        #Prints a random format

        s1 = input("Blank 1:")
        s2 = input("Blank 2:")
        s3 = input("Blank 3:")
        if format == 1:
            print(s1 + " went to the " + s2 + " with their " + s3)
        if format == 2:
            print("The "+ s1 + " is captain of the "+ s2 + " in " + s3 + " city")
        if format == 3:
            print("The "+ s1 + " " + s2 + " fox jumped over the " + s3 + " dog.")
        if format == 4:
            print("If you only knew the "+ s1 + " of the dark side. " + s2 + " never told you what happened to your " + s3 + ".")
        if format == 5:
            print(s1 + " is a famous japanese character whos power is " + s2 + "ing enemies with his " + s3 + ".")
        if format == 6:
            print(s1 + " scientists study " + s2 + "\'s effect on " + s3 + ".")
        if format == 7:
            print("It\'s "+ s1 + " O'clock and im feeling like " + s2 + " " + s3 + "\'s.")
        if format == 8:
            print("The best way to stay "+ s1 + " is to " + s2 + " " + s3 + " everyday.")
        if format == 9:
            print("I "+ s1 + " my " + s2 + " everyday like a " + s3 + ".")
        #Puts your answers in that format

        print("I hope that was what you wanted")
        print ("Would you like to do another")
        YesNo = str.lower(str.strip(input()))
            #Figures out if you want to paly again
        while YesNo != "yes" and YesNo != "no" and YesNo != "n" and YesNo != "y":
            print("Error, try again")
            YesNo = str.lower(str.strip(input()))

        if YesNo == "no" or YesNo == "n":
            print("Goodbye!")

        if YesNo == "yes" or YesNo == "y":
            print("Alright!")
            MadLibs.SimpleMadLibModeFunc()

    #Prints the CrazyMadLib
    def CrazyMadLibModeFunc():
        print("Welcome to Crazy MadLib. I will ask you for three words and then put them in every prompt in the program.")
        s1 = input("Word 1:")
        s2 = input("Word 2:")
        s3 = input("Word 3:")
        #Just gets three words and puts them in everything
        print(s1 + " went to the " + s2 + " with their " + s3)
        print("The "+ s1 + " is captain of the "+ s2 + " in " + s3 + " city")
        print("The "+ s1 + " " + s2 + " fox jumped over the " + s3 + " dog.")
        print("If you only knew the "+ s1 + " of the dark side. " + s2 + " never told you what happened to your " + s3 + ".")
        print(s1 + " is a famous japanese character whos power is " + s2 + "ing enemies with his " + s3 + ".")
        print(s1 + " scientists study " + s2 + "\'s effect on " + s3 + ".")
        print("It\'s "+ s1 + " O'clock and im feeling like " + s2 + " " + s3 + "\'s.")
        print("The best way to stay "+ s1 + " is to " + s2 + " " + s3 + " everyday.")
        print("I "+ s1 + " my " + s2 + " everyday like a " + s3 + ".")  
        print ("Would you like to do another")
        YesNo = str.lower(str.strip(input()))
        while YesNo != "yes" and YesNo != "no" and YesNo != "n" and YesNo != "y":
            print("Error, try again")
            YesNo = str.lower(str.strip(input()))

        if YesNo == "no" or YesNo == "n":
            print("Goodbye!")

        if YesNo == "yes" or YesNo == "y":
            print("Alright!")
            MadLibs.CrazyMadLibModeFunc()