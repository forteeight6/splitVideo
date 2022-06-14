from os import walk
from src.bread.add import Add_with_prefix

def test_add_with_prefix_return_none():
    """
    Verifica se a função Add return None.
    """
    contents = "OK"
    ver = Add_with_prefix("teste_", contents)

    assert ver == None
    
def test_add_with_prefix_is_right():
    """
    Verifica se a função Add criou apenas um novo arquivo no diretorio.
    Lógica, contar quantos arquivos tem no diretorio antes e depois da execução.
    Objetivo Esperado: ter um arquivo a mais após a execução.
    """
    count = 0
    for _, _, files in walk("cache"):
        for _ in files:
            count += 1
    before_number_of_files_in_directory_cache = count
    # print("before_number_of_files_in_directory_cache:", before_number_of_files_in_directory_cache)
    
    contents = "OK"
    Add_with_prefix("teste_", contents)

    count = 0
    for _, _, files in walk("cache"):
        for _ in files:
            count += 1
    after_number_of_files_in_directory_cache = count
    # print("after_number_of_files_in_directory_cache:", after_number_of_files_in_directory_cache)
    
    assert after_number_of_files_in_directory_cache == (before_number_of_files_in_directory_cache + 1)
    
if __name__ == "__main__":
    test_add_with_prefix_return_none()
    test_add_with_prefix_is_right()