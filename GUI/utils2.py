# adds a second layer

from torch.autograd import Variable
from librosa.feature.inverse import mel_to_audio
from scipy.io.wavfile import write
from librosa.util import normalize

import torch.nn as nn
import time
import math
import librosa
import numpy as np
import torch
import os

N_FFT = 256
N_MELS = 512
N_CHANNELS = round(1 + N_FFT/2)
OUT_CHANNELS = 32

class RandomCNN(nn.Module):

    def __init__(self):
        super(RandomCNN, self).__init__()

        # 2-D CNN
        self.conv1 = nn.Conv2d(1, OUT_CHANNELS, kernel_size=(3, 3), stride=1, padding=0)
        self.LeakyReLU = nn.LeakyReLU(0.2)

        # Set the random parameters to be constant.
        weight = torch.randn(self.conv1.weight.data.shape)
        self.conv1.weight = torch.nn.Parameter(weight, requires_grad=False)
        bias = torch.zeros(self.conv1.bias.data.shape)
        self.conv1.bias = torch.nn.Parameter(bias, requires_grad=False)

        self.conv2 = nn.Conv2d(OUT_CHANNELS, OUT_CHANNELS, kernel_size=(3, 3), stride=1, padding=0)
        self.LeakyReLU = nn.LeakyReLU(0.2)
        # Set the random parameters to be constant.
        weight = torch.randn(self.conv2.weight.data.shape)
        self.conv2.weight = torch.nn.Parameter(weight, requires_grad=False)
        bias = torch.zeros(self.conv2.bias.data.shape)
        self.conv2.bias = torch.nn.Parameter(bias, requires_grad=False)

##

    def forward(self, x_delta):
        #out = self.LeakyReLU(self.conv1(x_delta))
        x_delta = x_delta
        x_delta = self.conv1(x_delta)
        x_delta = self.LeakyReLU(x_delta)
        #x_delta = self.max_pool2d(x_delta, kernel_size=2, stride=2)

        x_delta = self.conv2(x_delta)
        x_delta = self.LeakyReLU(x_delta)
        return x_delta

def wav2spectrum(filename):
    #x, sr = librosa.load(filename)
    #S = librosa.stft(x, N_FFT)
    #p = np.angle(S)
    #S = np.log1p(np.abs(S))
    #S = librosa.filters.mel(sr=sr, n_fft=2048, n_mels=512)
    x, sr = librosa.load(filename)
    S = librosa.feature.melspectrogram(x, n_fft= N_FFT, n_mels = N_MELS, sr=41000)
    return S, sr

def wav2spectrum2(filename):
    x, sr = librosa.load(filename)
    S = librosa.stft(x, N_FFT)
    p = np.angle(S)
    S = np.log1p(np.abs(S))
    return S, sr


def spectrum2wav(spectrum, sr, outfile):
    # Return the all-zero vector with the same shape of `a_content`
   a = np.exp(spectrum) - 1
   p = 2 * np.pi * np.random.random_sample(spectrum.shape) - np.pi
   for i in range(50):
       S = a * np.exp(1j * p)
       x = librosa.istft(S)
       p = np.angle(librosa.stft(x, N_FFT))
   librosa.output.write_wav(outfile, x, sr)

   # inv = librosa.feature.inverse.mel_to_audio(spectrum)
   # write(outfile, sr, inv)

def spectrum2wav2(spectrum, sr, outfile):
    inv = librosa.feature.inverse.mel_to_audio(spectrum)
    write(outfile, sr, inv)

def wav2spectrum_keep_phase(filename):
    x, sr = librosa.load(filename)
    S = librosa.stft(x, N_FFT)
    p = np.angle(S)

    S = np.log1p(np.abs(S))
    return S, p, sr


def spectrum2wav_keep_phase(spectrum, p, sr, outfile):
    # Return the all-zero vector with the same shape of `a_content`
    a = np.exp(spectrum) - 1
    for i in range(50):
        S = a * np.exp(1j * p)
        x = librosa.istft(S)
        p = np.angle(librosa.stft(x, N_FFT))
    librosa.output.write_wav(outfile, x, sr, norm=True)


def compute_content_loss(a_C, a_G, isMel):
    """
    Compute the content cost

    Arguments:
    a_C -- tensor of dimension (1, n_C, n_H, n_W)
    a_G -- tensor of dimension (1, n_C, n_H, n_W)

    Returns:
    J_content -- scalar that you compute using equation 1 above
    """
    m, n_C, n_H, n_W = a_G.shape

    # Reshape a_C and a_G to the (m * n_C, n_H * n_W)
    a_C_unrolled = a_C.view(m * n_C, n_H * n_W)
    a_G_unrolled = a_G.view(m * n_C, n_H * n_W)

    # Compute the cost
    #J_content = 1.0 / (4 * m * n_C * n_H * n_W) * torch.sum((a_C_unrolled - a_G_unrolled) ** 2)
    if isMel:
      J_content = torch.sum((a_C_unrolled - a_G_unrolled) ** 2)
    else:
      J_content = 1.0 / (4 * m * n_C * n_H * n_W) * torch.sum((a_C_unrolled - a_G_unrolled) ** 2)

    return J_content


def gram(A):
    """
    Argument:
    A -- matrix of shape (n_C, n_L)

    Returns:
    GA -- Gram matrix of shape (n_C, n_C)
    """
    GA = torch.matmul(A, A.t())

    return GA


def gram_over_time_axis(A):
    """
    Argument:
    A -- matrix of shape (1, n_C, n_H, n_W)

    Returns:
    GA -- Gram matrix of A along time axis, of shape (n_C, n_C)
    """
    m, n_C, n_H, n_W = A.shape

    # Reshape the matrix to the shape of (n_C, n_L)
    # Reshape a_C and a_G to the (m * n_C, n_H * n_W)
    A_unrolled = A.view(m * n_C * n_H, n_W)
    GA = torch.matmul(A_unrolled, A_unrolled.t())

    return GA


def compute_layer_style_loss(a_S, a_G, isMel):
    """
    Arguments:
    a_S -- tensor of dimension (1, n_C, n_H, n_W)
    a_G -- tensor of dimension (1, n_C, n_H, n_W)

    Returns:
    J_style_layer -- tensor representing a scalar style cost.
    """
    
    m, n_C, n_H, n_W = a_G.shape

    # Reshape the matrix to the shape of (n_C, n_L)
    # Reshape a_C and a_G to the (m * n_C, n_H * n_W)

    # Calculate the gram
    # !!!!!! IMPORTANT !!!!! Here we compute the Gram along n_C,
    # not along n_H * n_W. But is the result the same? No.
    GS = gram_over_time_axis(a_S)
    GG = gram_over_time_axis(a_G)
     
    # Computing the loss
    #J_style_layer = 1.0 / (4 * (n_C ** 2) * (n_H * n_W)) * torch.sum((GS - GG) ** 2)
    if isMel:
      J_style_layer = torch.sum((GS - GG) ** 2)
    else:
      J_style_layer = 1.0 / (4 * (n_C ** 2) * (n_H * n_W)) * torch.sum((GS - GG) ** 2)

    return J_style_layer

def timeSince(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

