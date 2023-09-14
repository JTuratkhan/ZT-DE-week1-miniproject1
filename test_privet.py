from privet import privet, multiply, divide

def test_privet():
    assert privet("Elsa") == "Elsa"

def test_multiply(x,y):
	assert multiply(3,4) == 12

def test_privet_dividex(x,y):
	assert divide(4,2) == 2

