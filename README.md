# Hotword
Hotword detection for the PinguimBots robot Theta. Hotword can also be called wakeword.

## Why Porcupine
Porcupine stands out among the tested libraries below. It is fast in detecting the spoken wakeword.

### Tested python libraries
- **SnowBoy (da KITT.AI)**
	-  does not exist anymore
- **PocketSphinx da CMUSphinx**
	- not very accurate
	- offline
	- open source
	- Pypi: https://pypi.org/project/pocketsphinx/
- **Pvporcupine** 
	- needs AcessKey
	- only three models per month
  - only 3 computers to use a model per month 
	- needs to train another ppn every month
	- Two types:
	 - **Porcupine wake word**
		  - fast detection
		  - efficient
		  - Source: https://picovoice.ai/docs/quick-start/porcupine-go/
	  - **Rhino Speech-to-Intent**
		  - can only make 10 commands in free version
		  - Source: https://picovoice.ai/platform/rhino/
- **EfficientWord-Net**
  - needs to train a model for specific words
	- models for words like Alexa, siri, Mycrosoft
	- Source code: https://github.com/Ant-Brain/EfficientWord-Net
- **Mycroft Precise**
	- requires python 3.6 until 3.9
  - not precise
	- Research paper: https://worldscientific.com/doi/10.1142/S0219649222500599
	- https://ant-brain.github.io/EfficientWord-Net/
	- Source code: https://github.com/MycroftAI/mycroft-precise

## Install requirements
```bash
$ pip install -r requirements.txt
```
It also requires the archive ```din-ding.mp3``` and the ppn file from the picovoice console.

### How to run
Please read Notes below before you run this code.
```bash
$ git clone https://github.com/pinguimbotsathome/Hotword
$ cd Hotword
$ python porcupine.py
```
### How the code works
It uses pvrecorder to open the mic and start listening to the audio stream. When it hears the wakeword "Hey Theta", it prints ```Detected``` on the screen and plays the audio file ```din-ding.mp3```.

#### Notes
This instructions are crucial to run the script:
1. Access key => in code: ```key``` => key from picovoice account. Create an account in picovoice and copy the Access key.
2. ```keyword_p``` => path to ppn file. Go to picovoice console and train the wakeword "Hey Theta". Choose Linux as device and download the file. Put the file inside the Hotword directory.
3. ```sensitivities``` => It is a number between 0 and 1. Deafult is 0.55.A higher sensitivity results in fewer misses at the cost of increasing the false alarm rate.
4. ```device_index``` => the default number is -1. Change it to match your device input. Usually is 1.
