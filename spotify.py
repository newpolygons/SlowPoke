from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
import os, helper

def getSpotify(url):
    os.chdir(os.getcwd() + "/files/temp")
    #Ensure  No Other Songs
    for file in os.listdir(os.getcwd()):
        if file.endswith(".wav"):
            os.remove(file)

    os.system("spotdl " + url + " --output-format wav")

    currentDirectory = os.getcwd()
    for file in os.listdir(os.getcwd()):
        if file.endswith(".wav"):
            song = file

    
    
    factor = float(input("Input a number from 1.1 - 1.9 the higher the slower: "))
    while (type(factor) != float):
        factor = float(input("Input a number from 1.1 - 1.9 the higher the slower: "))


    print("Converting Song, Output file will be in files folder.")
    helper.stretch(song , factor)

    #Add Reverb To Slowed Track

    with AudioFile(currentDirectory + '/stretched.wav', 'r') as f:
        audio = f.read(f.frames)
        samplerate = f.samplerate

    
    board = Pedalboard([Reverb(room_size=0.25)])
    
    effected = board(audio, samplerate)
    
    with AudioFile('../' + song + "_slowed.wav", 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)

    #Ensure  No Other Songs
    for file in os.listdir(os.getcwd()):
        if file.endswith(".wav"):
            os.remove(file)



