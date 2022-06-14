from os import walk, path, remove
from pytest import mark
from typing import Iterable
from src.bread.read import iterReadTxt
from tests.iterReadTxt import iterReadTxt_fake
from test_bread_add_addcontents import test_AddContents

"""
    Este teste esta relacionado com o test_AddContents,
    o test_AddContents cria um file com o nome teste.txt,
    no diretorio cache, contendo uma frase.
"""
def test_iterReadTxt_return_iterable():
    test_AddContents()
    obj = iterReadTxt()
    # print(isinstance(lido, Iterable))
    assert isinstance(obj, Iterable) == True

def test_iterReadTxt_return_line():
    """
    Objetivo do teste, retornar o conteudo do arquivo.
    Logica, se retornar nenhuma linha falhou.
    """
    test_AddContents()
    count = 0
    for linha in iterReadTxt_fake():
        print(linha)
        count += 1
    assert count > 0

if __name__ == "__main__":
    test_iterReadTxt_return_iterable()
    test_iterReadTxt_return_line()
    remove("cache\\teste.txt")