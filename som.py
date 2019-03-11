import sys
import soundfile as sf
from scipy import signal
from scipy.signal import butter, lfilter,filtfilt
from scipy.signal import freqs
import matplotlib.pyplot as plt
from scipy.io import wavfile
import wave
import numpy as np

def read_audio_file(file):
    return sf.read(file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        error_message = 'the call is: python %(sys.argv[0]) path_to_audio_file'
        print error_message

    path_audio_file = sys.argv[1]
    datas, sample_time = read_audio_file(path_audio_file) 
    
    print "Array of Datas: ", datas
    print "Sample Time: ", sample_time

    sf.write('NewAudio.flac', datas, sample_time/2)
    
    spf1 = wave.open(path_audio_file,'r')
    signal1 = spf1.readframes(-1)
    signal1= np.fromstring(signal1, 'Int16')
    
    plt.figure(1)
    plt.title('Signal Wave...')
    plt.plot(signal1)
    
    spf = wave.open('NewAudio.wav','r')
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    
    plt.figure(2)
    plt.title('Signal Wave Compress...')
    plt.plot(signal)
    plt.show()
