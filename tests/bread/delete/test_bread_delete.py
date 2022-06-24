from os import walk, path, remove
from pytest import mark
from src.bread.browse import Browse
from test_bread_add_addcontents import test_AddContents

def Delete_fake(): # Clone da função Delete com input definido.
    """
        Clone referente a função Delete do modulo delete.
        Path: src.bread.delete
    """
    for i in Browse():
        print(i)
    print()
    
    choice = "cache\\teste.txt"
    print(f"remove < {choice}")
    
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            if local == choice:      
                remove(choice)


def test_Delete():
    """
    Testar se realmente esta deletando:
    Verifique se o arquivo ainda existe apos o uso da função.
    """
    test_AddContents() # Ira criar o arquivo para ser deletado
    # breakpoint() # Caso queira ver o processo
    
    Delete_fake()
    
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            assert local != "cache\\teste.txt"
    
if __name__ == "__main__":
    test_Delete()