from pytest import mark
from src.dynamic_splitVideo import cutter
import logging as log
log.basicConfig(level=log.DEBUG, filename="log.log")

@mark.skip(reason="teste manual")
# @cutter # cutter(test_input()) # tive que comentar para skipar
def test_main() -> list:
    """
        Substituindo entradas dinamica por entradas estaticas.
    """

    origin = "teste\Como usar arquivos temporários - Live de Python201.mp4"
    print(f"origin < {origin}")
    dest = "teste.mp4"
    print(f"origin < {dest}")
    
    initial_time = str("0:5:0")
    print(f"initial_time < {initial_time}")
    final_time = str("0:15:0")
    print(f"final_time < {final_time}")
    
    return [origin, dest, initial_time, final_time]

if __name__ == "__main__":
    try:
        test_main()
    except TypeError as e:
        log.error(f"{__name__} - {e}")