from os import walk, path
# Browse, read, edit, add and delete
# Navegue, leia, edite, adicione e delete
# É o Bread!

def browse():
    for root, dirs, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            yield local

def read():
    pass

def edit():
    pass

def delete():
    pass
