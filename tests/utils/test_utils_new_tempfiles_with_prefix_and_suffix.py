from os import path
from src.utils import new_tempfile_with_prefix_and_suffix

def test_new_tempfile_with_prefix_and_suffix():
    file = new_tempfile_with_prefix_and_suffix(pre="teste_", suf=".mp3")
    assert path.exists(file) == True

if __name__ == "__main__":
    test_new_tempfile_with_prefix_and_suffix()