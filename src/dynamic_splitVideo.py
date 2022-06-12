import src.splitVideo as sv
import logging as log

log.basicConfig(level=log.DEBUG, filename="log.log")

def cutter(function) -> None:
    
    origin, dest, initial_time, final_time = function()
    
    slic = [[initial_time, final_time]]
    
    try:
        sv.splitVideo(
            op=True,
            origem=origin,
            destino=dest,
            slices=slic
        )
    finally:
        log.info("Cortado com sucesso!")
        