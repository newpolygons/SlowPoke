#File aggregates functions used by each method.
import wave, os



def stretch( fname,  factor ):
    ''' Shoutout  Manarabdelaty for stretch imp 
        https://github.com/Manarabdelaty/Audio-Stretching'''
    infile=wave.open( fname, 'rb')
    rate= infile.getframerate()
    channels=infile.getnchannels()
    swidth=infile.getsampwidth()
    nframes= infile.getnframes()
    audio_signal= infile.readframes(nframes)
    outfile = wave.open('stretched.wav', 'wb')
    outfile.setnchannels(channels)
    outfile.setsampwidth(swidth)
    outfile.setframerate(rate/factor)
    outfile.writeframes(audio_signal)
    outfile.close()
    return;