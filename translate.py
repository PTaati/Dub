# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 01:12:21 2018

@author: vento
"""
from google.cloud import translate
from google.oauth2 import service_account

key_path = "C:/Users/vento/OneDrive/เอกสาร/Project/KEY/tran.json"

def set_key(path_k):
        key_path = path_k

def google_cloud_tran(path,name): # file to file
   
    credentials = service_account.Credentials.from_service_account_file(key_path)
    # Instantiates a client
    translate_client = translate.Client(credentials=credentials)

    # The target language
    target = 'th'

    # Translates some text into Russian
    file = open(path+name,"r")
    file_Tran = open(path+"text_Tran.txt","w")
    
    texts = file.readlines()
    for i in texts:
        line = i.split(" ")
        word = line[0]
        l = len(word)
        left = i[l:]
        if(word=='Transcript:'):
                translation = translate_client.translate(left,target_language=target)
                tran_text = translation['translatedText']
                new_tran = 'Transcript: '+str(tran_text)+'\n'
        else:
                translation = translate_client.translate(word,target_language=target)
                tran_text = translation['translatedText']
                new_tran = str(tran_text)+str(left)

        file_Tran.write(new_tran)

    file.close()
    file_Tran.close()


