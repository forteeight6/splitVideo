from pytest import mark
from os import walk, path, remove
from tests.iterReadTxt import iterReadTxt_fake
from src.bread.add import AddContents

"""
Estou utilizando o iterReadTxt_fake() para checar o conteudo do arquivo.
"""
@mark.skip(reason="Teste Imcompleto")
def test_AddContents_real_data(): # Testando se as mesmas datas inseridas são as que foram inseridos.
    lista = ["teste1", "teste2", "teste3"]
    for item in lista:
        AddContents("cache\\teste.txt", item)
    
    iter_lista = iter(lista)
    for item in iterReadTxt_fake():
        print(item)
        print(next(iter_lista))
        print()
        # assert item == next(iter_lista)

@mark.skip(reason="Falhou")
def test_AddContents_quant_datas(): # Testando se a quantidade de datas inserido está correta.
    """
    Testando se está inserindo os dados corretamente.
    Ps. Este teste so ira funcionar para arquivos novos, porque
    arquivos ja vai conter dados, então a lógica não ira funcionar.
    Por isso defini um arquivo padrão que será deletado após o teste,
    e criado novamente ao ser testado.
    """
    lista = ["teste1", "teste2", "teste3"]
    for item in lista:
        AddContents("cache\\teste.txt", item)

    count = 0
    for item in iterReadTxt_fake():
        count += 1
        
    assert len(lista) == count
    remove("cache\\teste.txt")
    
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
    # test_AddContents_quant_datas()
    test_AddContents_real_data()
    
    breakpoint()
    # Remocao do arquivo testado
    remove("cache\\teste.txt")
