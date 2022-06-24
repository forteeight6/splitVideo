from pytest import mark
from os import walk, path
from src.bread.browse import BrowseSuffix
from test_bread_add_suffix import test_add_with_suffix_return_none as create_file

# mark.skip(reason="necessary definy a suffix in function.")
def test_BrowseSuffix():
    """
    Testar se esta retornando o local corretamente.
    """
    create_file()
    l_1 = BrowseSuffix("_teste")
    
    for root, _, files in walk("cache"):
        for file in files:
            l_2 = path.join(root, file)
            if l_1 == l_2:
                result = True
                break
                
    assert result == True
    

if __name__ == "__main__":
    test_BrowseSuffix()