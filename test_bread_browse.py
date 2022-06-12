from src.bread import browse

def test_browse_access_filetemps():
    navegador = browse()
    for i in navegador:
        print(i)
    
if __name__ == "__main__":
    test_browse_access_filetemps()