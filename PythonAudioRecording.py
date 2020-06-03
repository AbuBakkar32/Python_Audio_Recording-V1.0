import sounddevice as sound_device
from scipy.io.wavfile import write as audio_write

fs=44100
seconds=15

recording=sound_device.rec(int(seconds*fs),samplerate=fs,channels=2)
sound_device.wait()
audio_write("recording.wav",fs,recording)
