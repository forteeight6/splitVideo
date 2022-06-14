from os import walk, path
from src.bread.browse import Browse

def Edit(choice, new_dados):
    with open(choice, "wb") as file:
        file.write(new_dados.encode('utf-8'))
        
def EditTxt(new_dados):
    for i in Browse():
        print(i)
    print()
    choice = str(input("Edit < "))
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)

            if local == choice:
                Edit(choice, new_dados)