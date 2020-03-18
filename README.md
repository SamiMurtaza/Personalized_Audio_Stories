# Personalized_Audio_Stories

* [Libraries required](##Libraries-Required)
    * [For GUI](#For-GUI)
    * [For Model ](#For-Model)
    * [Libraries needed that come with python](###Libraries-needed-that-come-with-python)
* [Running the Prototype](#Running-the-Prototype)
    * [The GUI](#The-GUI)
    * [The Model](#The-Model) 
* [The Dataset](#The-Dataset)

## Libraries Required

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

## Running the Prototype

### The GUI

To run the GUI we just need to execute the file *main.py*. This can be done by executing the script in IDLE or by typing this in the cmd.
  
    python3 main.py

It is to be noted that the GUI used winsound which is a windows library and as such prevents the GUI from running on Linux. 

### The Model

There are multiple configurations of the model. What each of the configuration does is as follows and how to run them is shown in the table below:

| Filename        | Spectrogram Type | Number of Layers | Style Loss Files | To Run                  |
|-----------------|------------------|------------------|------------------|-------------------------|
| mel__cnn.py     | Mel              | 1                | 1                | python3 mel__cnn.py     |
| lin__cnn.py     | Linear           | 1                | 1                | python3 lin__cnn.py     |
| mel__cnn2.py    | Mel              | 2                | 1                | python3 mel__cnn2.py    |
| lin__cnn2.py    | Linear           | 2                | 1                | python3 lin__cnn2.py    |
| mel__cnn2All.py | Mel              | 2                | 24               | python3 mel__cnn2All.py |
| lin__cnn2All.py | Linear           | 2                | 24               | python3 lin__cnn2All.py | 

## The Dataset
The model uses a dataset of sentences spoken in each of the group members voice. These files are all in .wav format. The initials in the filename can be used to identify the speaker based on the following key: 

| Initials | Speaker Name        |
|----------|---------------------|
| MS       | Marina Shahzad      |
| SF       | Syeda Maryam Fatima |
| SM       | Sami Murtaza        |

The number in the filename can be used to identify what is spoken as follows:
| Sentence Code | Sentence Text                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1             | A quick brown fox jumps over the lazy dog                                                                                                                      |
| 2             | Jack and Jill went up the hill to fetch a pail of water. Jack fell down and broke his crown and Jill came tumbling after                                       |
| 3             | Twinkle Twinkle little a star, how I wonder what you are                                                                                                       |
| 4             | I am what I am and Im not ashamed. Never be ashamed. My old dad used to say 'there are some that will hold it against you but theyre not worth bothering with' |
| 5             | Happiness can be found even in the darkest of times                                                                                                            |
| 6             | Happiness can be found even in the darkest of times, if only one remembers to turn on the light                                                                |
| 7             | Once upon a time there was a little girl called red riding hood                                                                                                |
| 8             | Once upon a time there was a girl called red riding hood                                                                                                       |
| 9             | Im headed to my grandmas house cant stop to talk, said red                                                                                                     |
| 10            | Please don’t eat me said red, just eat my bread instead                                                                                                        |
| 11            | Why do you keep a vicious beast as a pet human                                                                                                                 |
| 12            | One hot day an ant was searching for some water                                                                                                                |
| 13            | I ate them all up and now, im hungry again                                                                                                                     |
| 14            | People die when they are killed                                                                                                                                |
| 15            | Once upon a time a cat and a dog and a mouse and a little red hen all lived together in a pretty little house                                                  |
| 16            | Ive got an idea!                                                                                                                                               |
| 17            | Whats in it for me? The boy asked                                                                                                                              |
| 18            | You may find that the drop is not nearly as tall                                                                                                               |
| 19            | Look! Red mouse has crumbs around his mouth                                                                                                                    |
| 20            | Did you eat the cheese red mouse?                                                                                                                              |
| 21            | No it wasn’t me! This is my lunch                                                                                                                              |
| 22            | At night, when the whole world goes off to sleep, owl wakes up                                                                                                 |
| 23            | He waited and waited until he ws sure all the other owls are ready for bed                                                                                     |
| 24            | I found you he shouted and burst through the door                                                                                                              |
| 25            | I climbed up the hill and reached out to the sky                                                                                                               |
| 26            | Hurry hurry, they say to mom and dad, we don’t want to be late                                                                                                 |
| 27            | He dreamt about a place that he had never seen before                                                                                                          |
