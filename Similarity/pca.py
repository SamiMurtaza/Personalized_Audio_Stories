# -*- coding: utf-8 -*-
"""pca.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G6Bf93FXwkjS5CyP8slgFTZ2ls-Ls7Wl
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy, scipy, matplotlib.pyplot as plt, sklearn, urllib, IPython.display
# %matplotlib inline
plt.rcParams['figure.figsize'] = (14, 5)

!pip install essentia

import numpy, scipy, matplotlib.pyplot as plt, sklearn, librosa, urllib, IPython.display
import essentia, essentia.standard as ess
plt.rcParams['figure.figsize'] = (14,4)

from google.colab import drive
drive.mount('/content/drive')

ls

import os

for i in range(1,27):
  if os.path.exists('/content/drive/My Drive/PAS/Maryam/SF-'+ str(i) +'.WAV'):
    x, fs = librosa.load('/content/drive/My Drive/PAS/Maryam/SF-'+ str(i) +'.WAV')
    IPython.display.Audio(x, rate=fs)

    X = librosa.feature.mfcc(x, sr=fs)
    #print(X.shape)
    X = sklearn.preprocessing.scale(X)
    X.mean()
    model = sklearn.decomposition.PCA(n_components=2, whiten=True)
    model.fit(X.T)
    Y1 = model.transform(X.T)
    #print(Y1.shape)

    a=model.components_
    #print(a)
    #print(a.shape)

    plt.scatter(Y1[:,0], Y1[:,1])
print(model.explained_variance_ratio_)

for i in range(1,27):
  if os.path.exists('/content/drive/My Drive/PAS/Marina/MS-'+ str(i) +'.WAV'):
    x, fs = librosa.load('/content/drive/My Drive/PAS/Marina/MS-'+ str(i) +'.WAV')
    IPython.display.Audio(x, rate=fs)

    X = librosa.feature.mfcc(x, sr=fs)
    #print(X.shape)
    X = sklearn.preprocessing.scale(X)
    X.mean()
    model = sklearn.decomposition.PCA(n_components=2, whiten=True)
    model.fit(X.T)
    Y1 = model.transform(X.T)
    #print(Y1.shape)

    a=model.components_
    #print(a)
    #print(a.shape)

    plt.scatter(Y1[:,0], Y1[:,1])
print(model.explained_variance_ratio_)

for i in range(1,27):
  if os.path.exists('/content/drive/My Drive/PAS/Sami/SM-'+ str(i) +'.WAV'):
    x, fs = librosa.load('/content/drive/My Drive/PAS/Sami/SM-'+ str(i) +'.WAV')
    IPython.display.Audio(x, rate=fs)

    X = librosa.feature.mfcc(x, sr=fs)
    #print(X.shape)
    X = sklearn.preprocessing.scale(X)
    X.mean()
    model = sklearn.decomposition.PCA(n_components=2, whiten=True)
    model.fit(X.T)
    Y1 = model.transform(X.T)
    #print(Y1.shape)

    a=model.components_
    #print(a)
    #print(a.shape)

    plt.scatter(Y1[:,0], Y1[:,1])
print(model.explained_variance_ratio_)

x, fs = librosa.load('/content/drive/My Drive/PAS/Marina/MS-27.WAV')
IPython.display.Audio(x, rate=fs)

X = librosa.feature.mfcc(x, sr=fs)
print(X.shape)
X = sklearn.preprocessing.scale(X)
X.mean()
model = sklearn.decomposition.PCA(n_components=2, whiten=True)
model.fit(X.T)
Y1 = model.transform(X.T)
print(Y1.shape)

b=model.components_
model.components_.shape
print(model.components_.shape)

plt.scatter(Y1[:,0], Y1[:,1])



import pandas as pd

x, fs = librosa.load('/content/drive/My Drive/PAS/Marina/MS-27.WAV')
IPython.display.Audio(x, rate=fs)

X = librosa.feature.mfcc(x, sr=fs)
X = sklearn.preprocessing.scale(X)

model = sklearn.decomposition.PCA(n_components=4, whiten=True)
pc = model.fit_transform(X)

model.explained_variance_ratio_

x, fs = librosa.load('/content/drive/My Drive/PAS/Maryam/SF-15.WAV')
IPython.display.Audio(x, rate=fs)

X = librosa.feature.mfcc(x, sr=fs)
print(X.shape)
X = sklearn.preprocessing.scale(X)
X.mean()
model = sklearn.decomposition.PCA(n_components=2, whiten=True)
model.fit(X.T)
Y2 = model.transform(X.T)
print(Y2.shape)

b=model.components_
model.components_.shape
print(model.components_.shape)

plt.scatter(Y2[:,0], Y2[:,1])

x, fs = librosa.load('/content/drive/My Drive/PAS/results/MS-27_SF-15_10000_0.02/(10000).wav')
IPython.display.Audio(x, rate=fs)

X = librosa.feature.mfcc(x, sr=fs)
print(X.shape)
X = sklearn.preprocessing.scale(X)
X.mean()
model = sklearn.decomposition.PCA(n_components=2, whiten=True)
model.fit(X.T)
Y = model.transform(X.T)
print(Y.shape)

b=model.components_
model.components_.shape
print(model.components_.shape)

plt.scatter(Y[:,0], Y[:,1])

plt.scatter(Y1[:,0],Y1[:,1])
plt.scatter(Y2[:,0],Y2[:,1])
plt.scatter(Y[:,0],Y[:,1])

plt.scatter(Y1[:,0],Y1[:,1])
plt.scatter(Y[:,0],Y[:,1])
plt.title('Marina MS-27 and Mimicked Maryam (MS-27_SF-15)')

plt.scatter(Y2[:,0],Y2[:,1])
plt.scatter(Y[:,0],Y[:,1])
plt.title('Maryam SF-15 and Mimicked Maryam (MS-27_SF-15)')

x, fs = librosa.load('/content/drive/My Drive/PAS/Maryam/SF-27.WAV')
IPython.display.Audio(x, rate=fs)

X = librosa.feature.mfcc(x, sr=fs)
print(X.shape)
X = sklearn.preprocessing.scale(X)
X.mean()
model = sklearn.decomposition.PCA(n_components=2, whiten=True)
model.fit(X.T)
Y3 = model.transform(X.T)
print(Y3.shape)

b=model.components_
model.components_.shape
print(model.components_.shape)

plt.scatter(Y3[:,0], Y3[:,1])

plt.scatter(Y3[:,0], Y3[:,1])
plt.scatter(Y[:,0],Y[:,1])

plt.title('Maryam SF-27 and Mimicked Maryam (MS-27_SF-15)')

#print(a)
#print(b)

c=a-b
print(c)
print(c.shape)

plt.plot(a, c='b')
plt.plot(b, c='r')
plt.legend(('x', 'y'))

from matplotlib import pyplot as plt
import numpy as np
import math
from sklearn.preprocessing import StandardScaler
import numpy as np



import pandas as pd

df = pd.read_csv('/content/drive/My Drive/PAS/audio2.csv')

df.columns=['number','label','audio']

df.tail()

X = df.iloc[:,2]
print( type(eval(X[0])))
#for i in X[0]:
#  if type(i) != float: print(i)
Y = df.iloc[:,1]
#print(Y)

X = df.iloc[:,1]
print(X)
print(X.dtype)

intery = df.iloc[:,0]
print(intery)

y=intery.str.slice(0,2,1)
print(y)

Y.values

X

eval(X[1])

from sklearn.preprocessing import StandardScaler

X = np.array([np.array(i) for i in X])
print(type(X), len(X))
for i in X:
  print(len(i))
#print(len(X), len(X[0]), len(X[1]))
#X_std = StandardScaler().fit_transform(X)

from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn = sklearn_pca.fit_transform(X)

with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(6, 4))
    for lab, col in zip(('SM','SF','MS'),
                        ('blue', 'red', 'green')):
        plt.scatter(Y_sklearn[y==lab, 0],
                    Y_sklearn[y==lab, 1],
                    label=lab,
                    c=col)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(loc='lower center')
    plt.tight_layout()
    plt.show()

import os
import librosa
import csv

f = open('/content/drive/My Drive/audio3.csv', 'w')
writer = csv.writer(f)
print('Hi')
for i in os.listdir():
  print('Hi3')
  if i in ["Marina","Sami","Maryam"]:
    for j in os.listdir(i):
      x, sr = librosa.load(i+"/"+j)
      row = [j, list(x), i]
      writer.writerow(row)
      print('Hi2')



import os
import librosa

directory = '/content/drive/My Drive/PAS/Marina'

for file in os.listdir(directory):
    if file.endswith('.WAV'):
        file_path = os.path.join(directory, file)
        audio_data, _ = librosa.load(file_path)

from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler


def get_pca(features):
    pca = PCA(n_components=2)
    transformed = pca.fit(features).transform(features)
    scaler = MinMaxScaler()
    scaler.fit(transformed)
    return scaler.transform(transformed)
  

my_array_of_feature_vectors = ...
scaled_pca = get_pca(my_array_of_feature_vectors)