def main_fake() -> list:
    """
        Substituindo entradas dinamica por entradas estaticas.
    """

    origin = "teste\\Como usar arquivos temporários - Live de Python201.mp4"
    # print(f"origin < {origin}")
    dest = "teste.mp4"
    # print(f"origin < {dest}")
    
    initial_time = str("0:5:0")
    # print(f"initial_time < {initial_time}")
    final_time = str("0:15:0")
    # print(f"final_time < {final_time}")
    
    return [origin, dest, initial_time, final_time]
