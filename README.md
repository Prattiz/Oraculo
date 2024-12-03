# Oraculo

Oraculo is an intelligent voice assistant designed to understand and execute voice commands, respond in natural language, and learn from user interactions. The project leverages various speech and machine learning libraries to enhance its capabilities.

##

## Installation and Setup

### Create a virtual environment:
`python -m venv venv`

### Activate the virtual environment:

- On Windows:

`.\venv\Scripts\activate`

- On Linux/macOS:

`source venv/bin/activate`

### Install dependencies:

`pip install -r requirements.txt`


# How to use -->

1) run main.py with:
`python main.py`

2) you can train the assistent with more functions by:
- going to `nlu/train.yml` and add more functions to respond
- add more bot functions in `core`

## functional requirements --✅-- 

- [X] it must hear your voice
- [X] it must understand your voice
- [X] it must speak your language 
- [X] it must speak to you
- [X] it must learn
- [X] it must do what you command

## domain requirements --✅--

- [X] must use Python
- [X] the libraries: speech recognition, PyAudio, pyttsx3, Vosk, Numpy, scikit-learn and PyYAML must be installed
- [X] when running model.py or classifier.py you must create or update the assistant training files
- [X] should open the notepad
- [X] must pass every test