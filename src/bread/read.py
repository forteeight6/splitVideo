from os import walk, path
from src.bread.browse import Browse

def iterReadTxt():
    for i in Browse():
        print(i)
    print()
    
    choice = str(input("read < "))
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)

            if local == choice:
                with open(choice) as file:
                    for linha in file:
                        # Por padrao strip remove os espaços.
                        yield linha.strip()
