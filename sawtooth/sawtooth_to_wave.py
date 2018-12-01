import numpy as np
from scipy.io.wavfile import write

# f_s: Sample rate
# A_c: Amplitude of the sawtooth
# thirty_two_bits_per_sample: We are doing 32 bits per sample,
#   and this is what you need to multiply each float by.
f_s = 96000
thirty_two_bits_per_sample = 2147483647
A_c = 0.3

# duration_s: The duration in seconds of the sound.
# The f_c: Frequency of the sawtooth wave.
duration_s = 2.0
f_c = 100.0

# Create one period of the sawtooth waveform
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
waveform_ints = np.int32(waveform * 2147483647)
write('first_sawtooth.wav', f_s, waveform_ints)
