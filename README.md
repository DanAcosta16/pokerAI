# Poker AI Game
## Dan Acosta, John Wolf

## Table of Contents
1. Running the Program
2. File Descriptions

# 1: Running the Program

To run the program, run launch.py. It will ensure the virtual environment is installed and launch Poker.py in it

# 2: File Descriptions

## launch.py

* Checks if the virtual environment 'app-env' is installed
	* Creates virtual environment and adds dependencies if not found
* Launches Poker.py

## Poker.py

* Checks if file 'cheat.json' exists
	* Runs loader.py if not
* Runs Poker game

### loader.py

* Creates 'cheat.json' and adds all winning hand combinations
	* Used to preload winning hand combinations for cheat engine
	* May move into Poker.py -- there is no reason it should be a stand alone program

### cheat.json

* Contains all possible hands that could win, generated the first time the program is run
* Contains ranking each win type: 0-6 for high card to straight flush
* May add variables to check when to cheat

## app-env

* Python virtual environment containing the dependencies for this project (pydealer)
* launcher.py will install this if it is not detected
