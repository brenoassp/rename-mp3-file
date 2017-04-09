import os
from mutagen.mp3 import MP3

files_list = os.listdir(".")
for f in files_list:
    if ".mp3" in f:
        audio = MP3(f)
        new_name = str(audio.info.length // 60)[:-2] + 'minutes-' + f
        print new_name
        #os.rename(f,new_name)
