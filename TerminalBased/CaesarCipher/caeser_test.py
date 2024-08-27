import CaesarCipherTestable as CCTest


def test_get_mode():
    assert CCTest.get_mode("e") == "invalid"
    assert CCTest.get_mode("encrypt") == "invalid"
    assert CCTest.get_mode("d") == "invalid"
    assert CCTest.get_mode("decrypt") == "invalid"
    assert CCTest.get_mode("b") == "invalid"
    assert CCTest.get_mode("brute") == "invalid"
    assert CCTest.get_mode("u") == "invalid"


def test_get_key():
    assert CCTest.get_key(92) == 92
    assert CCTest.get_key(1) == 1
    assert CCTest.get_key(45) == 45
    assert CCTest.get_key(0) == 0
    assert CCTest.get_key(93) == 0
    assert CCTest.get_key(-100) == 0
    assert CCTest.get_key(111) == 0



def test_get_translated_message():
    assert CCTest.get_translated_message("e", "Hello World", 1) == "Ifmmp Xpsme"
    assert CCTest.get_translated_message("e", "Hello World", 21) == "cz770 r0#7y"
    assert CCTest.get_translated_message("d", "cz770 r0#7y", 21) == "Hello World"
    assert CCTest.get_translated_message("e", "I Like Linux", 92) == "I Like Linux"
