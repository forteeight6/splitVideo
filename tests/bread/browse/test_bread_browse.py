from os import walk
from typing import Iterable
from src.bread.browse import Browse


def test_browse_access_filetemps_is_iterable():
    navegador = Browse()
    # print(isinstance(navegador, Iterable))
    # print(type(navegador), navegador)
    assert isinstance(navegador, Iterable) == True
    
def test_browse_access_filetemps_return_all_files():
    count = 0
    for _, _, files in walk("cache"):
        for file in files:
            count += 1
    total_of_file_in_directory = count
    # print(f"total_of_file_in_directory: {total_of_file_in_directory}")
    
    count = 0
    for _ in Browse():
        count += 1
    total_of_file_return_for_browse = count
    # print(f"total_of_file_return_for_browse: {total_of_file_return_for_browse}")
    
    assert total_of_file_in_directory == total_of_file_return_for_browse
        
    
if __name__ == "__main__":
    test_browse_access_filetemps_is_iterable()
    test_browse_access_filetemps_return_all_files()