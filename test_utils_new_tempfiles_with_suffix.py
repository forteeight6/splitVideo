from os import path
from src.utils import new_tempfile_with_suffix

def test_new_tempfile_with_suffix():
    file = new_tempfile_with_suffix(suf=".mp3")
    assert path.exists(file) == True

if __name__ == "__main__":
    test_new_tempfile_with_suffix()