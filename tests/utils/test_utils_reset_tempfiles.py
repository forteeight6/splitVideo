from os import walk
from src.utils import reset_tempfiles

def test_reset_tempfile():
    reset_tempfiles()
    
    for _, _, files in walk("cache"):
        tm = int(len(files))

    assert tm == 0

if __name__ == "__main__":
    test_reset_tempfile()
