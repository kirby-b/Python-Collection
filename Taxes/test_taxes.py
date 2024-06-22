import tax_testable as tax

def test_state_tax():
    assert tax.state_tax(100, 4.2) == 4.2
    assert tax.state_tax(1000, 4.2) == 42
    assert tax.state_tax(100000, 6.2) == 6200
    assert tax.state_tax(10000000, 3.2) == 320000
    assert tax.state_tax(82000, 4.2) == 3444

def test_medicare():
    assert tax.medicare(100) == 1.45
    assert tax.medicare(1000) == 14.5
    assert tax.medicare(100000) == 1450
    assert tax.medicare(10000000) == 145000
    assert tax.medicare(82000) == 1189

def test_social_security():
    assert tax.social_security(100) == 6.2
    assert tax.social_security(1000) == 62
    assert tax.social_security(100000) == 6200
    assert tax.social_security(10000000) == 620000
    assert tax.social_security(82000) == 5084

def test_income_tax():
    assert tax.income_tax(100) == 10
    assert tax.income_tax(1000) == 100
    assert tax.income_tax(100000) == 16207
    assert tax.income_tax(10000000) == 3624744

def test_main():
    assert tax.main(100,100,100,100) == "400.00"
    assert tax.main(100, 3.3333, 62.2, 77.1) == "242.63"
    assert tax.main(350, 9.5, 10.5, 50) == "420.00"
    assert tax.main(55, 6.2222, 7.3333, 10.4444) == "78.99"
    assert tax.main(10000, 444.5556, 332.456, 1000.553) == "11777.56"
