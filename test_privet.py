from privet import privet, multiply, divide

def setup_function(function):
	print(f"Running Teardown: {function.__name__}")
	function.x = 5


def test_multiply(x,y):
	assert multiply(3,4) == 12

def test_privet_dividex(x,y):
	assert divide(4,2) == 2

