import os
from mutagen.mp3 import MP3
from Tkinter import Tk
from tkFileDialog import askopenfilenames

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
files_list = askopenfilenames() # show an "Open" dialog box and return the path to the selected file

for f in files_list:
	if ".mp3" in f:
		path = f[0:f.rfind('/')+1]
		file_name = f[f.rfind('/')+1:]
		audio = MP3(f)
		new_name = path + str(audio.info.length // 60)[:-2] + 'minutes-' + file_name
		os.rename(f,new_name)