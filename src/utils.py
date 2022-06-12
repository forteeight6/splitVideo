from os import walk, path, remove
import tempfile

def new_tempfile():
    tempfile.tempdir = "cache"
    try:
        file = tempfile.NamedTemporaryFile(delete=False)
    finally:
        file.close()
        
    return file.name
        
def reset_tempfiles():
    for root, files, docs in walk("cache"):
        for doc in docs:
            rmv = path.join(root, doc)
            remove(rmv)
        
def convert_time_to_seconds(time):

    splitted_time = time.split(":")

    hora = int(splitted_time[0])
    minutes = int(splitted_time[1])
    seconds = int(splitted_time[2])

    hour_to_sec = hora * 3600
    minut_to_sec= minutes * 60

    fixed_time = hour_to_sec + minut_to_sec + seconds
    
    return fixed_time


