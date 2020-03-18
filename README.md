# Personalized_Audio_Stories

## Libraries required

### For GUI

- **pygame**: The GUI is built primarily using pygame. This library provides the ability to create and interact with a window. 
- **winsound**: Is used to play different sounds, for example the sound made when a button is clicked. 
- **speech_recognition**: As the name suggests, this library is used to recognize what a speaker has said. This is used to check if the user has said what we intended for them to say.
- **pyaudio**: This library is used to enable voice recording. 
- **wave**: This library is used to write .wav files that will later be used by the model. 
- **difflib**: From difflib we only need the *SequenceMatcher* function as we need to verify just how similar two strings are and if the similarity is above a certain threshold. 
- **ctypes**: We used ctypes to figure out the resoultion of the screen user is running the application on. This will be used to scale all screen elements such that everything fits neatly on screen. 

### For Model 

- **pytorch**: The Model is built using pytorch. pytorch provides the functionality needed for style transfer. 
- **librosa**: We use librosa for dealing with most audio related tasks, such as making spectrograms, loading audio files and writing audio files.
- **scipy**: This library is also used for its capability to write wav files. 
- **numpy**: As expected, numpy is used for tasks like calculating sums of vectors, absolute values and other numerical tasks. 

### Libraries needed that come with python

- time
- os
- math 
