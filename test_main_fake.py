from main import main
from tests.main import main_fake
"""
Testar se o main_fake está se comportando igual
ao original main
"""
def test_main_fake_is_equal_to_main_in_quant():
	entry_main = main(spy=True)
	entry_main_fake = main_fake()

	# print("entry_main", entry_main)
	# print()
	# print("entry_main_fake", entry_main_fake)

	assert len(entry_main) == len(entry_main_fake)
	return True

def test_main_fake_is_equal_to_main_in_item():
	entry_main = iter(main(spy=True))
	entry_main_fake = iter(main_fake())

	while True:
		try:
			assert next(entry_main) == next(entry_main_fake)
		finally:
			break	
	return True

if __name__ == "__main__":
	# test_main_fake_is_equal_to_main_in_quant()
	test_main_fake_is_equal_to_main_in_item()