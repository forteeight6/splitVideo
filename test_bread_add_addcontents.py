from os import walk, path, remove
from pytest import mark
import logging as log
from tests.iterReadTxt import iterReadTxt_fake
from src.bread.add import AddContents

log.basicConfig(level=log.DEBUG, filename="log.log")
"""
Estou utilizando o iterReadTxt_fake() para checar o conteudo do arquivo.
"""
def __reset():
    """ Removendo caso diretorio ja exista. """
    try:
        remove("cache\\teste.txt")
    except FileNotFoundError as e:
        print('Repita o Teste, pois o arquivo deve ja ter sido criado.')
        log.error(e)

def test_AddContents_real_data(): 
    """Testando se as mesmas datas inseridas são as que foram inseridos."""

    # Resetando para fazer o teste
    __reset()
    
    entries = ["teste1", "teste2", "teste3"]
    for entry in entries:
        AddContents("cache\\teste.txt", entry)
    
    iter_entries = iter(entries)
    for result in iterReadTxt_fake():
        expect = next(iter_entries)
        assert result == expect
    

# @mark.skip(reason="Falhou")
def test_AddContents_quant_datas(): 
    """
    Testando se a quantidade de datas inserido está correta.

    Testando se está inserindo os dados corretamente.
    Ps. Este teste so ira funcionar para arquivos novos, porque
    arquivos ja vai conter outros dados, então a lógica não ira funcionar.
    Por isso defini um arquivo padrão que será deletado após o teste,
    e criado novamente ao ser testado.
    """
    
    # Resetando para fazer o teste
    __reset()

    entries = ["teste1", "teste2", "teste3"]
    for entry in entries:
        AddContents("cache\\teste.txt", entry)

    count = 0
    for _ in iterReadTxt_fake():
        count += 1
    
    # print(len(entries))
    # print(count)
    assert len(entries) == count
    
def test_AddContents():
    """
    Testando se esta inserido o arquivo.
    Mantenha como padrão os values do 
    AddContents como: "cache\\teste.txt", "teste"
    """
    
    AddContents("cache\\teste.txt", "teste")
    
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            if local == "cache\\teste.txt":
                break
        
        assert local == "cache\\teste.txt"
        break

if __name__ == "__main__":
    # test_AddContents()
    test_AddContents_quant_datas()
    # test_AddContents_real_data()
    
    # breakpoint()
    # Remocao do arquivo testado
    # remove("cache\\teste.txt")
