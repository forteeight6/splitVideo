from os import walk, path

def iterReadTxt_fake():
    """
    O test_iterReadTxt_return_line está utilizando essa função,
    derivado da função iterReadTxt porém com o input pre definido.
    Ps: A dependência Browse() foi removido pois não ah necessidade
    de listar os possiveis inputs, pois como ja foi dito ele ja esta
    pre-definido nessa função de teste.
    """
    
    choice = "cache\\teste.txt"

    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)

            if local == choice:
                with open(choice) as file:
                    for linha in file:
                        # Por padrão o strip revome todos os espaços
                        yield linha.strip()
