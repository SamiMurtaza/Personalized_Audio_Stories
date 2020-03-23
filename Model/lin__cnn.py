from torch.autograd import Variable
from librosa.feature.inverse import mel_to_audio
from scipy.io.wavfile import write

import torch.nn as nn
import time
import math
import librosa
import numpy as np
import torch
import os
from utils import *

print("*IMPORTED*")

basepath = "data/"
result_path = basepath + "results/"

content_source_name = "Marina"
CName = "/MS-1.WAV"
CONTENT_FILENAME = basepath + content_source_name +CName

SName = "/Maryam/SF-2.WAV"
style_source_name = ""
STYLE_FILENAME = basepath + style_source_name + SName

style_param = 1
content_param = 1e2
learning_rate = 0.23

num_epochs = 10000
print_every = 500

cuda = True if torch.cuda.is_available() else False
print("Cuda = ", cuda)

print("*GLOBALS SET*")

#Directory Name = 'BaseAudio_TargetAudio_epochs_learningrate'
dir_name = result_path + CONTENT_FILENAME.split("/")[-1][:-4] + "_" + STYLE_FILENAME.split("/")[-1][:-4] + "_" + str(num_epochs) + "_" + str(learning_rate)
if os.path.exists(dir_name):
    count = 1
    temp = dir_name + "(" +str(count) + ")"
    while os.path.exists(temp):
        count+=1
        temp = dir_name + "(" +str(count) + ")"
    dir_name = temp
    
os.mkdir(dir_name)

print("*DIR MADE " + dir_name +" *")

a_content, sr = wav2spectrum2(CONTENT_FILENAME)
a_style, sr = wav2spectrum2(STYLE_FILENAME)

a_content_torch = torch.from_numpy(a_content)[None, None, :, :]

if cuda:
    a_content_torch = a_content_torch.cuda()    
print(a_content_torch.shape)

a_style_torch = torch.from_numpy(a_style)[None, None, :, :]

if cuda:
    a_style_torch = a_style_torch.cuda()
print(a_style_torch.shape)

model = RandomCNN()
model.eval()

a_C_var = Variable(a_content_torch, requires_grad=False).float()
a_S_var = Variable(a_style_torch, requires_grad=False).float()

if cuda:
    model = model.cuda()
    a_C_var = a_C_var.cuda()
    a_S_var = a_S_var.cuda()

a_C = model(a_C_var)
a_S = model(a_S_var)

if cuda:
    a_G_var = Variable(torch.randn(a_content_torch.shape).cuda() * 1e-3, requires_grad=True)
else:
    a_G_var = Variable(torch.randn(a_content_torch.shape) * 1e-3, requires_grad=True)
    
optimizer = torch.optim.Adam([a_G_var])

start = time.time()
# Train the Model

print ("*TRAINING STARTED*")
for epoch in range(0, num_epochs + 1):
    optimizer.zero_grad()
    a_G = model(a_G_var)

    content_loss = content_param * compute_content_loss(a_C, a_G, False)
    style_loss = style_param * compute_layer_style_loss(a_S, a_G, False)
    loss = content_loss + style_loss 
    
    loss.backward()
    optimizer.step()

    if epoch % print_every == 0:
        gen_spectrum = a_G_var.cpu().data.numpy().squeeze()
        gen_audio_C = dir_name + "/(" + str(epoch) + ")" + '.wav'
        spectrum2wav(gen_spectrum, sr, gen_audio_C)
        
        print("{} {}% {} content_loss:{:4f} style_loss:{:4f} total_loss:{:4f}".format(epoch,
                                                                                      epoch / num_epochs * 100,
                                                                                      timeSince(start),
                                                                                      content_loss.item(),
                                                                                      style_loss.item(), loss.item()))

gen_spectrum = a_G_var.cpu().data.numpy().squeeze()
gen_audio_C = result_path + '.wav'
spectrum2wav(gen_spectrum, sr, gen_audio_C)

print("_________________________________")
