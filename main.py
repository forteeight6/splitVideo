from src.dynamic_splitVideo import cutter

"""
    Adicionar Arquivo Temporario, utilizando o Bread.
    Criar Interface Gráfica. PS: Faça um rascunho antes.
"""

def main(spy=False) -> str:
    if spy:
    	origin = "teste\\Como usar arquivos temporários - Live de Python201.mp4"
    	# print(f"origin < {origin}")
    	dest = "teste.mp4"
    	# print(f"origin < {dest}")
    
    	initial_time = str("0:5:0")
    	# print(f"initial_time < {initial_time}")
    	final_time = str("0:15:0")
    	# print(f"final_time < {final_time}")
    else:
    	origin = str(input("origin < "))
    	dest = str(input("destiny < "))
    
    	initial_time = str(input("initial_time < "))
    	final_time = str(input("final_time < "))
    
    return [origin, dest, initial_time, final_time]


if __name__ == "__main__":
    cutter(main())
