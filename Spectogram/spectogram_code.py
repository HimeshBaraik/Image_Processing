import cv2
import numpy as np
import librosa

def solution(audio_path):
    ############################
    ############################
    # Load an audio file (replace 'your_audio_file.wav' with the actual file path)
    
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
        
    return obj
