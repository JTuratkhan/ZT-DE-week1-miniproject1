from privet import privet, multiply, divide

def setup_function(function):
	print(f"Running Teardown: {function.__name__}")
	function.x = 5


def teardown_function(function):
	print(f"Running Teardown: {function.__name__}")
	del function.x

def test_privet_divide():
	assert divide(test_privet_divide.x == 4)

