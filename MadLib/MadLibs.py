class MadLibs:

    # Normal MadLibs
    def simple_mad_lib_mode_func(self):
        import random
        print("Welcome To MadLib. I will give you a prompt and then ask for three inputs(they will be inserted at the capitalized words in parentheses).\n")
        s1 = "___"
        s2 = "___"
        s3 = "___"
        sentence = random.randrange(1, 10)
        if sentence == 1:
            print("\"NAME\" went to the \"NOUN\" with their \"NOUN\".\n")
        if sentence == 2:
            print("\"NAME\" is captain of the \"NOUN\" in \"ADJECTIVE\"city.\n")
        if sentence == 3:
            print("The \"ADJECTIVE\" \"COLOR\" fox jumped over the \"ADJECTIVE\" dog.\n")
        if sentence == 4:
            print("If you only knew the \"NOUN\" of the dark side. \"NAME\" never told you what happened to your \"NOUN\".\n")
        if sentence == 5:
            print("\"NAME\" is a famous japanese character whos power is \"ACTION\"ing enemies with his \"NOUN\".\n")
        if sentence == 6:
            print("\"NOUN\" scientists study \"NOUN\"\'s effect on \"NOUN\".\n")
        if sentence == 7:
            print("It\'s \"NOUN\" O'clock and im feeling like \"ADJECTIVE\" \"NOUN\"\'s.\n")
        if sentence == 8:
            print("The best way to stay \"ADJECTIVE\" is to \"ACTION\" \"NOUN\" everyday.\n")
        if sentence == 9:
            print("I \"ACTION\" my \"NOUN\" everyday like a \"ADJECTIVE\".\n")
        # Prints a random format

        s1 = input("Blank 1:")
        s2 = input("Blank 2:")
        s3 = input("Blank 3:")
        if sentence == 1:
            print(s1 + " went to the " + s2 + " with their " + s3)
        if sentence == 2:
            print("The " + s1 + " is captain of the " + s2 + " in " + s3 + " city")
        if sentence == 3:
            print("The " + s1 + " " + s2 + " fox jumped over the " + s3 + " dog.")
        if sentence == 4:
            print("If you only knew the " + s1 + " of the dark side. " + s2 + " never told you what happened to your " + s3 + ".")
        if sentence == 5:
            print(s1 + " is a famous japanese character who's power is " + s2 + "ing enemies with his " + s3 + ".")
        if sentence == 6:
            print(s1 + " scientists study " + s2 + "\'s effect on " + s3 + ".")
        if sentence == 7:
            print("It\'s " + s1 + " O'clock and im feeling like " + s2 + " " + s3 + "\'s.")
        if sentence == 8:
            print("The best way to stay " + s1 + " is to " + s2 + " " + s3 + " everyday.")
        if sentence == 9:
            print("I " + s1 + " my " + s2 + " everyday like a " + s3 + ".")
        # Puts your answers in that format

        print("I hope that was what you wanted")

    # Prints the CrazyMadLib
    def crazy_mad_lib_mode_func(self):
        print("Welcome to Crazy MadLib. I will ask you for three words and then put them in every prompt in the program.")
        s1 = input("Word 1:")
        s2 = input("Word 2:")
        s3 = input("Word 3:")
        # Just gets three words and puts them in everything
        print(s1 + " went to the " + s2 + " with their " + s3)
        print("The " + s1 + " is captain of the " + s2 + " in " + s3 + " city")
        print("The " + s1 + " " + s2 + " fox jumped over the " + s3 + " dog.")
        print("If you only knew the " + s1 + " of the dark side. " + s2 + " never told you what happened to your " + s3 + ".")
        print(s1 + " is a famous japanese character who's power is " + s2 + "ing enemies with his " + s3 + ".")
        print(s1 + " scientists study " + s2 + "\'s effect on " + s3 + ".")
        print("It\'s " + s1 + " O'clock and im feeling like " + s2 + " " + s3 + "\'s.")
        print("The best way to stay " + s1 + " is to " + s2 + " " + s3 + " everyday.")
        print("I " + s1 + " my " + s2 + " everyday like a " + s3 + ".")
