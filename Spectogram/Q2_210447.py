import cv2
import numpy as np
import librosa

def solution(audio_path):
    ############################
    ############################
    # Load an audio file (replace 'your_audio_file.wav' with the actual file path)
    #audio_file = 'metal_banging11.mp3'
    y, sr = librosa.load(audio_path)

    # Compute the magnitude spectrum using FFT
    D = librosa.stft(y)
    magnitude = np.abs(D)

    # Compute the average magnitude at each frequency
    average_magnitude = np.mean(magnitude, axis=1)

    # Frquency corresponding to maximum magnitude
    max_index = np.argmax(average_magnitude)

    # Check whether cardboard or metal using a threshold
    if max_index > 50:
        obj = 'metal'

    else:
        obj = 'cardboard'
    ############################
    ############################
    ## comment the line below before submitting else your code wont be executed##
    # pass
    # class_name = 'cardboard'
    # return class_name
    return obj
