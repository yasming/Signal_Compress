# Project Title

In this project is possible process an audio signal. This code, compress the audio signal in .wav format, reducing your sample time, then give you back a new audio in format .flac . 

## Prerequisites

This are the libs you need to install to the 

```
sys
```
```
soundfile
```
```
scipy
```
```
scipy.signal 
```
```
matplotlib.pyplot
```
```
scipy.io
```
```
wave
```
```
numpy
```

### Getting Started

First you can exec the project doing

```
python som.py AudioPDS.wav
```

When you do this, you will can see in the terminal, the array of datas coming from the AudioPDS.wav and the sample_time too.

After this you will get a archive called "NewAudio.flac", this new audio is already compressed, you can play this and watch the result.

Then, convert this to  "NewAudio.wav" using some audio convert like this https://online-audio-converter.com/pt/ . So, rename the archive to "NewAudio.wav" .

Then, exec the project again .

```
python som.py AudioPDS.wav
```

So, you will obtain graphics to the normal audio and to the compressed audio being displayed. 





