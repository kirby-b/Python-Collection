from pig_latin import pigify

def test_pigify():
    assert pigify("Hello World") == "ello hey orld way"
    assert pigify("I like Metallica") == "i yay ike lay etallica may"
    assert pigify("I dont know why Im testing this") == "i yay ont day now kay hy way im yay esting tay his tay"