
from pydub import AudioSegment as am

from scipy.io import wavfile
import scipy.signal as sps
import soundfile

filename= "data/1.wav"

def check(filename):
    ob = soundfile.SoundFile(filename)
    print('Sample rate: {}'.format(ob.samplerate))
    print('Channels: {}'.format(ob.channels))
    print('Subtype: {}'.format(ob.subtype))

def convert_soundfile(filename):
    data, samplerate = soundfile.read('data/0.wav')
    soundfile.write('00.wav', data, samplerate, subtype='PCM_16')

# https://github.com/jiaaro/pydub/blob/master/API.markdown
def convert_pydub(filename):
    sound = am.from_file("data/1.wav", format="wav", sample_width=1)
    sound= sound.set_sample_width(2) # 2 bytes= 16 bits
    sound= sound.set_frame_rate(16000) 
    sound= sound.set_channels(1) 

    sound.export("data/test.wav", format="wav")

convert_pydub(filename)
check("data/test.wav")

