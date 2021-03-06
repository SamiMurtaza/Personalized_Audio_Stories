# -*- coding: utf-8 -*-
"""fuzzy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q9aRwCtPGo2-EcSi2MnxJxfxDefW9XvT
"""

!pip install pyacoustid
!pip install fuzzywuzzy[speedup]

import acoustid
import chromaprint
from fuzzywuzzy import fuzz
import librosa

from google.colab import drive
drive.mount("/content/gdrive", force_remount=True)

basepath = "/content/gdrive/My Drive/PAS"

audio1_source_name = "/LowPassed/Maryam/"
audio_clip_s = "SF-17.wav"
audio_s = basepath + audio1_source_name + audio_clip_s

audio1_source_name = "/LowPassed/results/MS-17_Maryam_10000_0.002/"
audio_clip_m = "(10000).wav"
audio_m = basepath + audio1_source_name + audio_clip_m

duration, fp_encoded = acoustid.fingerprint_file(audio_s)
fingerprint_s, version = chromaprint.decode_fingerprint(fp_encoded)

duration, fp_encoded = acoustid.fingerprint_file(audio_m)
fingerprint_m, version = chromaprint.decode_fingerprint(fp_encoded)

print(audio_s)
print(audio_m)

similarity = fuzz.ratio(fingerprint_s, fingerprint_m)
print(similarity)