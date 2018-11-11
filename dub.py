# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:18:49 2018

@author: vento
"""

import manager_vdo as mgv
import speech_recognition as sr
import translate as ts
import text_to_speech as tts



path = "C:/Users/vento/OneDrive/เอกสาร/Project/VDO/testOil/"
name = 'st1.mp4'

mgv.split_wav_vdo(path+name,path+"wav.wav") 

sr.google_could(path+"wav.wav",'en')  #แปลเสียงเป็นข้อความเก็บในไฟล์ wav.wavReg.txt 

file_name = "wav.wavRec.txt"

ts.google_cloud_tran(path,file_name) #แปลภาษา ในไฟล์ wav.wavReg.txt ไปเป็น text_Tran.txt