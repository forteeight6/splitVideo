from os import walk, path, remove
from src.bread.browse import Browse

def Delete():
    for i in Browse():
        print(i)
    print()
    choice = str(input("remove < "))
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            if local == choice:
                remove(choice)    