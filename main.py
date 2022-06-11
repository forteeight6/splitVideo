from src.dynamic_splitVideo import cutter
import logging as log

@cutter # cutter(main())
def main() -> str:
    origin = str(input("origin < "))
    dest = str(input("destiny < "))
    
    initial_time = str(input("initial_time < "))
    final_time = str(input("final_time < "))
    
    return [origin, dest, initial_time, final_time]


if __name__ == "__main__":
    try:
        main()
    except TypeError as e:
        log.error(f"{__name__} - {e}")