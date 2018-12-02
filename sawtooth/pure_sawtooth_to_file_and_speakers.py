import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import time

# f_s: Sample rate
# A_c: Amplitude of the sawtooth.
f_s = 44100
A_c = 0.3

# duration_s: The duration in seconds of the sound.
# The f_c: Frequency of the sawtooth wave.
duration_s = 5.0
f_c = 100.0

# Create the sawtooth wave for the entire duration of the
# waveform. The duration won't come to the exact number
# of periods, so the excess will be trimmed.
#
# period_c: The PERIOD of the sawtooth waveform
#
# periods_in_duration: The number of periods in the whole duration
#
# samples_per_period: Given f_s, the number of samples that are
#   present in the waveform
#
# tiled_sawtooth: The total sawtooth periods in the waveform.
#
# trimmed_sawtooth: The sawtooth trimmed down to the number of
#   samples.
period_c = 1.0 / f_c
periods_in_duration = int(np.ceil(duration_s / period_c))
samples_per_period = int(np.ceil(period_c * f_s))
sawtooth_period = np.linspace(1.0, -1.0, samples_per_period)
tiled_sawtooth = np.tile(sawtooth_period, periods_in_duration)
samples_in_duration = int(np.ceil(duration_s * f_s))
waveform = tiled_sawtooth[:samples_in_duration]
waveform *= A_c

# In order to play out of the speakers, we need integers
waveform_ints = np.int16(waveform * 32768)

# Now write to the file
write('first_sawtooth.wav', f_s, waveform_ints)

# And play out of the speakers
sd.play(waveform_ints, f_s)
time.sleep(duration_s)
sd.stop()
