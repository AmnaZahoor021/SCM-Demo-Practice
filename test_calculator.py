from calculator import calculate_discount
def test_discount():
	assert calculate_discount(100,False) == 15
def test_member_discount():
	assert calculate_discount(100,True) == 20
