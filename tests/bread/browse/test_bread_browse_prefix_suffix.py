# from pytest import mark
from os import walk, path
from src.bread.browse import BrowsePrefixSuffix
from test_bread_add_prefix_suffix import test_add_with_prefix_and_sufix_return_none as create_file

# mark.skip(reason="necessary definy a prefix and suffix in function.")
def test_BrowsePrefixSuffix():
    """
    Testar se esta retornando o local corretamente.
    Create_file é derivado de outro teste, que testa a criação de arquivos,
    através da função Add(), ps ela requisita a adição de um prefixo e sufixo.
    O objetivo do teste é saber se esta encontrando o arquivo que foi criado.
    """
    create_file()
    l_1 = BrowsePrefixSuffix("teste_", "_teste")
    
    for root, _, files in walk("cache"):
        for file in files:
            l_2 = path.join(root, file)
            if l_1 == l_2:
                result = True
                break
    
    # print(l_1)
    # print(l_2)
    assert result == True
    

if __name__ == "__main__":
    test_BrowsePrefixSuffix()