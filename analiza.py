from numpy import sin, linspace, pi, fromstring
import pylab
from scipy import fft, arange
import wave

#czestotliwosc = 82.0
#czas = 5.0
#amplituda = 1.0
czest_probkowania = 44100.0

def sound_data(frequency, time, amplitude, sample_rate): #creating data points for a specific parameters to Sine
    time_points = linspace(0, time, time*sample_rate)
    data = sin(2*pi*frequency*time_points)
    data = amplitude*data
    
    return data

def plotSpectrum(y,Fs): #
    n = len(y)
    k = arange(n)
    T = n/Fs
    frq = k/T
    frq = frq[range(n/2)]
    
    Y = fft(y)/n
    Y = Y[range(n/2)]
    
    pylab.plot(frq, abs(Y), 'r')
    pylab.xlabel('Freq (Hz)')
    pylab.ylabel('|Y(freq)|')

waveFile = wave.open('rec_1','r')
print waveFile.getparams()

signal = waveFile.readframes(-1)
signal = fromstring(signal, 'Int16')
print signal

for i in signal:
    print i

#plotSpectrum(signal, czest_probkowania)
#pylab.xlim(16,22000)
#pylab.show(plotSpectrum)