import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import time


def sawtooth_wave(fundamental_hz, duration_s=1.0, max_k=2, f_s=44100):
    """
    Calculate a sawtooth wave as a sum of a sine wave and
    all integer harmonics of the fundamental.

    Parameters
    ----------
    fundamental_hz: {float} The frequency of the fundamental in hz
    duration_s: {float} Duration of the waveform

    Returns
    -------
    result: {(waveform, harmonics_hz, components_arr)} A tuple containing
            the summed waveform as the
            first element, the list of harmonics as the second element
            and all the individual components as the third element.
    """
    harmonics_hz = []
    components_list = []
    ks = np.arange(1, max_k)
    t_is = np.arange(duration_s * f_s)

    for k in ks:
        harmonics_hz.append(k * fundamental_hz)
        component = (-1) ** k * np.sin(2 * np.pi * k * fundamental_hz * t_is / f_s) / k
        component = component.reshape(1, -1)
        components_list.append(component)

    components_arr = np.vstack(components_list)
    waveform = 2 / np.pi * components_arr.sum(axis=0)
    return waveform, harmonics_hz, components_arr


def main():
    # f_s: Sample rate
    # A_c: Amplitude of the sawtooth
    f_s = 44100
    A_c = 0.5

    # duration_s: The duration in seconds of the sound.
    # The f_c: Frequency of the sawtooth wave.
    duration_s = 5.0
    f_c = 100.0

    # Add up the sawtooth
    waveform, _, _ = sawtooth_wave(fundamental_hz=f_c, duration_s=duration_s, max_k=11)
    waveform *= A_c

    # In order to play out of the speakers, we need integers
    waveform_ints = np.int16(waveform * 32768)

    # Now write to the file
    write('second_sawtooth.wav', f_s, waveform_ints)

    # And play out of the speakers
    sd.play(waveform_ints, f_s)
    time.sleep(duration_s)
    sd.stop()


if __name__ == '__main__':
    main()
