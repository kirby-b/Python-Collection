import random

jokes = ["If I got 50 cents for every failed math exam, I\'d have $6.30 now.","250 lbs here on Earth is 94.5 lbs on Mercury. No, I'm not fat. I\'m just not on the right planet",
"When life gives you melons, you might be dyslexic","I was wondering why the frisbee kept getting bigger and bigger, but then it hit me",
"A horse walks into a bar.\nSeveral people get up and leave as they spot the potential danger of the situation.","What do you call a fly with no wings?\nA fly. The irony is unfortunate, but the name doesn\'t change.",
"Why was six afraid of seven?\nIt wasn\'t because numbers aren\'t sentient, which means they aren\'t capable of feeling fear.","What do you call a cheese that isn\'t yours?\nStolen! Make sure you return it before the rightful owners prosecute you.",
"Laughter is the best medicine …\nNot for me, I\'ve got cancer.","What is red and extremely bad for your teeth?\nA flying brick.","What do you call 100 lawyers at the bottom of the ocean?\nA horrible boating accident.","I invented a new word\nPlagiarism",
"What do you get if you eat too much ice cream?\nA stomach ache and possibly diabetes.","I just got my doctor's test results and I'm really upset.\nTurns out, I'm not gonna be a doctor.","I just read that someone in London gets stabbed every 52 seconds. Poor guy.",
"My wife told me she'll slam my head on the keyboard if I don't get off the computer. I'm not too worried, I think she's jokinlkjhfakljn m,.nbziyoao78yv87dfaoyuofaytdf","How many emo kids does it take to screw in a lightbulb?\nNone, they all sit in the dark and cry.",
"They say that breakfast is the most important meal of the day. Well, not if it's poisoned. Then the antidote becomes the most important.","The doctor gave me one year to live, so I shot him. The judge gave me 15 years. Problem solved.",
"I hate double standards. Burn a body at a crematorium, you're \"being a respectful friend.\" Do it at home and you're \"destroying evidence.\"","You don\'t need a parachute to go skydiving. You need a parachute to go skydiving twice.", 
"When I die, I want to die like my grandfather who died peacefully in his sleep. Not screaming like all the passengers in his car.","The other day, my wife asked me to pass her lipstick but I accidentally passed her a glue stick. She still isn't talking to me.",
"Never break someone's heart, they only have one. Break their bones instead, they have 206 of them.","One man\'s trash is another man\'s treasure. Wonderful saying, horrible way to find out you were adopted.","My boss told me to have a good day. So I went home.",
"Today was a terrible day. My ex got hit by a bus. And I lost my job as a bus driver!","I took my mother-in-law out yesterday morning. Being a sniper is awesome.","I was in Russia listening to a stand-up comedian making fun of Putin. The jokes weren't that good, but I liked the execution.",
"Remember, being healthy is basically dying as slowly as possible.","Siri, why am I still single?! *Siri activates front camera*","Dark humour is like food, not everyone gets it.","I wasn't close to my father when he died. Which is lucky because he stepped on a landmine.",
"What do you call an orphan taking a selfie? A family photo.","An apple a day keeps the doctor away. Or at least it does if you throw it hard enough.","I was playing chess with my friend and he said, “Let\'s make this interesting.” So we stopped playing chess.",
"I was shocked when I found out my toaster was not waterproof.","I have a fish that can breakdance! Only for 20 seconds though, and only once.","Once, my father came home and found me in front of a roaring fire. That made my father very mad, as we didn\'t have a fireplace.",
"\"I\'m sorry\" and \"I apologize\" mean the same thing. Except at a funeral.", "I made a website for orphans. It doesnt have a home page.", "I threw a boomerang a few years ago. Now I live in constant fear.", "They laughed at my crayon drawing. I laughed at their chalk outline.",
"To teach kids about democracy, I let them vote on dinner. They picked tacos. Then I made pizza because they dont live in a swing state."]
#List of jokes. They are not for everybody and some are kinda offensive
def Jokefunc():
    print("\n"+ jokes[random.randrange(0,45)] + "\n")
    #Prints a random joke from the list using a random number
    print ("Would you like another joke")
    YesNo = str.lower(str.strip(input()))
    #Asks if you want to hear another joke
    while YesNo != "yes" and YesNo != "no" and YesNo != "n" and YesNo != "y":
        print("Error, try again")
        YesNo = str.lower(str.strip(input()))

    if YesNo == "no" or YesNo == "n":
        print("Goodbye!")

    if YesNo == "yes" or YesNo == "y":
        print("Alright!")
        Jokefunc()

Jokefunc()