def convert_time_to_seconds(time):

    splitted_time = time.split(":")

    hora = int(splitted_time[0])
    minutes = int(splitted_time[1])
    seconds = int(splitted_time[2])

    hour_to_sec = hora * 3600
    minut_to_sec= minutes * 60

    fixed_time = hour_to_sec + minut_to_sec + seconds
    
    return fixed_time


