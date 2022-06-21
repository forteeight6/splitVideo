# from pytest import mark
from src.bread.edit import Edit, EditTxt
from test_bread_add_addcontents import test_AddContents
from test_bread_read import iterReadTxt_fake

"""
    O test_AddContents() esta sendo usado para o dever
    de gerar um arquivo nomeado como teste.txt
    no diretorio \\cache.
    
    O iterReadTxt_fake é um clone da função iterReadTxt porem
    definido como input estático com o valor de cache\\teste.txt,
    e var ser usado para ler o diretorio antecipadamente e 
    posteriormente e por fim fazer a comparação se houve modificação.
"""

# @mark.skip(reason="Teste Incompleto")
def test_Edit():
    """
        Este teste vai verificar se houve a edicao do arquivo teste.txt
    """
    test_AddContents()
    
    Edit("cache\\teste.txt", "teste2")
    before = next(iterReadTxt_fake())
    # retornando ao resultado anterior.
    Edit("cache\\teste.txt", "teste1") 
    after = next(iterReadTxt_fake())

    # print(before)
    # print(after)
    assert before != after


if __name__ == "__main__":
    test_Edit()