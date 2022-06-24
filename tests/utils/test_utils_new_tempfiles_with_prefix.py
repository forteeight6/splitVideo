from os import path
from src.utils import new_tempfile_with_prefix

def test_new_tempfile_with_prefix():
    file = new_tempfile_with_prefix(pre="teste_")
    assert path.exists(file) == True

if __name__ == "__main__":
    test_new_tempfile_with_prefix()