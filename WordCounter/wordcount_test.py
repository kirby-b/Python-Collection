from word_count import word_count


def test_word_count():
    #Checks to see if the spaces are counted correctly
    assert word_count("Hello World") == 2
    assert word_count("Hello") == 1
    assert word_count("Lorem Ipsum Dolor Set Amet") == 5
    assert word_count("Hello    World") == 2
    assert word_count("By all know laws of aviation bees shouldnt be able to get their fat little bodies of the ground.") == 19
    assert word_count("Wow    Did  I break it   ") == 5
    assert word_count("HTML may or may not be a programming language") == 9
    assert word_count("The quick brown fox jumped over the lazy dog") == 9
    assert word_count("Never gonna give you up, Never gonna let you down, Never gonna run around and desert you, Never gonna make you cry, Never gonna say goodbye, Never gonna tell a lie and hurt you.") == 34
    assert word_count("I like cats") == 3