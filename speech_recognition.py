# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 01:10:41 2018

@author: vento
"""
key_path = "C:/Users/vento/OneDrive/เอกสาร/Project/KEY/recog.json"

import time, io
start_time = time.time()
from google.oauth2 import service_account
from pydub import AudioSegment
credentials = service_account.Credentials.from_service_account_file(key_path)



def set_key_path(path):
    key_path = path

def google_could(path,lang):# wav to file limit 1 min
    sound = AudioSegment.from_file(path).set_channels(1)      # set chanel 1 and wav to flac
    sound.set_frame_rate(44100)
    sound.export(path+".flac",format='flac')

    timeFlac = sound.duration_seconds
    print(timeFlac)

    times = int((timeFlac+59)/60)
    print(times)
    start = 0
    end = 60
    for i in range(times):
        newAudio = sound[start*1000:end*1000]
        newAudio.export(path+str(i)+".flac", format="flac")
        start = end
        end = end + 60
        if end >= timeFlac:
            end = -1
            newAudio = sound[start*1000:-1]
            newAudio.export(path+str(i+1)+".flac", format="flac")
            break

    shift = 0
    file_text_path = path+"Rec.txt"
    file = open(file_text_path,"a")
    for i in range(times):
        from google.cloud import speech
        from google.cloud.speech import enums
        from google.cloud.speech import types
        client = speech.SpeechClient(credentials=credentials)

        with io.open(path+str(i)+".flac", 'rb') as audio_file:
            content = audio_file.read()

        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=44100,
            language_code=lang,
            enable_word_time_offsets=True)

        response = client.recognize(config, audio)

        print("-----------------------------"+str(i)+"-----------------------------------")
        for result in response.results:  
            alternative = result.alternatives[0]
            print("Transcript: "+alternative.transcript) 
            file.write("Transcript: "+alternative.transcript+"\n")
            print(result)
            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                end_time = word_info.end_time
                file.write(word+" "+str(shift + start_time.seconds + start_time.nanos * 1e-9)+" "+str(shift + end_time.seconds + end_time.nanos * 1e-9)+" \n") 
        shift = shift + 60
    return file_text_path

'''
import manager_vdo as mv
path = "C:/Users/vento/OneDrive/เอกสาร/Project/VDO/testOil/"
name = 'st1.mp4'
#mv.split_wav_vdo(path+name,path+"wav.wav")
google_could(path+"wav.wav",'en')
'''