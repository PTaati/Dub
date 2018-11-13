# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 00:43:29 2018

@author: vento
"""

import moviepy.editor as mp
from pydub import AudioSegment

def split_wav_vdo(path_vdo,path_wav): #avi to wav
    clip = mp.VideoFileClip(path_vdo).subclip(0,-1)
    clip.audio.write_audiofile(path_wav)
    

def Slice(inputAudio,output,start,end): 
    start = int(start * 1000) #Works in milliseconds
    end = int(end * 1000)
    newAudio = inputAudio[start:end]
    newAudio.export(output, format="flac")

def mp3_to_wav(path_mp3,path_wav): # mp3 to wav
    sound = AudioSegment.from_mp3(path_mp3) 
    sound.export(path_wav, format="wav")
    
def change_speed_wav(path_in,path_out,speed): #speed same original
    sound = AudioSegment.from_file(path_in)
    newSound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    newSound.export(path_out,format="wav")
    
def concat_wav(path_in1,path_in2,path_out): #wav + wav to wav
    sound1 = AudioSegment.from_wav(path_in1)
    sound2 = AudioSegment.from_wav(path_in2)
    combined_sounds = sound1 + sound2
    combined_sounds.export(path_out, format="wav")
    
def VdoMergeAudio(path_vdo,path_wav,path_out): #avi + wav to mp4
    audio = mp.AudioFileClip(path_wav)
    video1 = mp.VideoFileClip(path_vdo)
    final = mp.concatenate_videoclips([video1]).set_audio(audio)
    final.write_videofile(path_out)
