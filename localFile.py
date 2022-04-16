from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
from pydub import AudioSegment
import tkinter, os, shutil, helper
from tkinter import filedialog

''' This fle handles the slowing of local files :)'''


def localFileConvert():
    os.environ['TK_SILENCE_DEPRECATION'] = "1"
   
    filetypes = (
        ('mp3', '*.mp3'),
        ('wav', '*.wav')

    )
    currentDirectory = os.getcwd()
    temperaryFile =  filedialog.askopenfilename(initialdir = currentDirectory, title='Select Audio', filetypes=filetypes)
    
    if temperaryFile.lower().endswith('.mp3'):
        #MP3 Implementation
        sound = AudioSegment.from_mp3(temperaryFile)
        sound.export(currentDirectory + "/files/temperaryFile.wav", format='wav')
    
    elif temperaryFile.lower().endswith('.wav'):
        shutil.copyfile(temperaryFile, currentDirectory + "/files/temperaryFile.wav")

    factor = float(input("Input a number from 1.1 - 1.9 the higher the slower: "))
    while (type(factor) != float):
        factor = float(input("Input a number from 1.1 - 1.9 the higher the slower: "))
    
    os.chdir('files')
    helper.stretch('temperaryFile.wav', factor)
    
    #Add Reverb to Slowed Track

    with AudioFile(currentDirectory + '/files/stretched.wav', 'r') as f:
        audio = f.read(f.frames)
        samplerate = f.samplerate

    board = Pedalboard([Reverb(room_size=0.25)])
    
    effected = board(audio, samplerate)
    
    with AudioFile(currentDirectory + '/files/slowpokedSound.wav', 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)

    #Clean UP

    if os.path.exists(currentDirectory + '/files/temperaryFile.wav'):
        os.remove(currentDirectory + '/files/temperaryFile.wav')
    if os.path.exists(currentDirectory + '/files/stretched.wav'):
        os.remove(currentDirectory + '/files/stretched.wav')


    



