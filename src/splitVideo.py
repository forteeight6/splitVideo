from moviepy.editor import VideoFileClip
from src.utils import convert_time_to_seconds

def splitVideo(op:str=None, **kwargs) -> None:
    """
    Function for multiple cuts in the video.
    :param - origem: enter the location of the file.
           - destino: enter the outputs you want.
           - slices: defines where you want the cuts to be.
    """
    if op:
        unicSplit(
            origem=kwargs["origem"],
            destino=kwargs["destino"],
            slices=kwargs["slices"])
    else:
        multiSplit(
            origem=kwargs["origem"],
            destino=kwargs["destino"],
            slices=kwargs["slices"])
        
def multiSplit(**kwargs):
    video = VideoFileClip(kwargs["origem"])
    novo_video = iter(kwargs["destino"])
    
    for i, f in kwargs["slices"]:
        fstart_time = convert_time_to_seconds(i)
        fend_time = convert_time_to_seconds(f)
        trimed_video = video.subclip(fstart_time, fend_time)
        trimed_video.write_videofile(next(novo_video))

def unicSplit(**kwargs):
    video = VideoFileClip(kwargs["origem"])
    
    novo_video = kwargs["destino"]

    for i, f in kwargs["slices"]:
        fstart_time = convert_time_to_seconds(i)
        fend_time = convert_time_to_seconds(f)
        trimed_video = video.subclip(fstart_time, fend_time)
        trimed_video.write_videofile(novo_video)