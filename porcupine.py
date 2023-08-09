#! /usr/bin/env python3

# import
import os
import pvporcupine
import playsound as ps
from pvrecorder import PvRecorder

# Access key 1
key = "8BY7hb24nfW4y/M6h7tECqWMZ+vwu4BY/F8OyzENOQ9GnvKbALz5DA=="

# path to keyword
keyword_p = os.path.abspath("Hey-Theta_en_linux_v2_2_0.ppn")

# detected sound
din = os.path.abspath("din-ding.mp3")

pp = pvporcupine.create(access_key=key,
                        keyword_paths=[keyword_p],
                        sensitivities=[0.9])


## record device
recorder = PvRecorder(device_index=-1,
                      frame_length=pp.frame_length)
                      
print("Say hotword:")

while True:
    recorder.start()
    pcm = recorder.read()
    audio_frame = pcm
    keyword_index = pp.process(audio_frame)
    if keyword_index >=0:
       print("Detected.")
       ps.playsound(din)
       # do something
       recorder.stop()
