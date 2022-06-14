import src.utils as utils


def Add(contents):
    """
    Adiciona um novo arquivo temporario e seu conteudo.
    """
    AddContents(utils.new_tempfile(), contents)


def Add_with_prefix_and_sufix(prefix, suffix, contents):
    """
    Adiciona um novo arquivo temporario e seu conteudo.
    """
    AddContents(utils.new_tempfile_with_prefix_and_suffix(prefix, suffix), contents)
    
def Add_with_prefix(prefix, contents):
    """
    Adiciona um novo arquivo temporario e seu conteudo.
    """
    AddContents(utils.new_tempfile_with_prefix(prefix), contents)
    
def Add_with_suffix(suffix, contents):
    """
    Adiciona um novo arquivo temporario e seu conteudo.
    """
    AddContents(utils.new_tempfile_with_suffix(suffix), contents)

def AddContents(local, contents):
    """Adiciona conteudo no documento"""
    with open(local, "ab") as file:
        file.write(contents.encode('utf-8'))
        file.write('\n'.encode('utf-8'))
