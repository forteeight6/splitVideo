from pytest import mark

@mark.skip(reason="In Production")
def test_simpleGui():
	pass

if __name__ == '__main__':
	test_simpleGui()