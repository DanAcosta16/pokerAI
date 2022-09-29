# Poker AI Game
## Dan Acosta, John Wolf
---

1. Running the Program
2. File Descriptions

# 1: Running the Program

To run the program, run launch.py. It will run the necessary files to launch Poker.py

***

# 2: File Descriptions

## launch.py

* Checks if the virtual environment 'app-env' is installed
	* Runs install.bat or install.sh if not found
* Launches Poker.py

### install.bat

* Creates virtual environment, upgrades venv's pip and installs the dependency pydealer for Windows

### install.sh

* Creates virtual environment, upgrades venv's pip and installs the dependency pydealer for Linux or Mac

## Poker.py

* Checks if file 'cheat.json' exists
	* Runs loader.py if not
* Runs Poker game

### loader.py

* Creates 'cheat.json' and adds all winning hand combinations
	* Used to preload winning hand combinations for cheat engine
