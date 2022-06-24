from os import path
from src.utils import new_tempfile

def test_new_tempfile():
    file = new_tempfile()
    assert path.exists(file) == True

if __name__ == "__main__":
    test_new_tempfile()
