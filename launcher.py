import os, sys

def isWindows(): return sys.platform in {"win32", "msys", "cygwin"}

debug = False
if "-debug" in sys.argv: debug = True

venv = "app-env"
if(not os.path.isdir(venv)):
	# virtual environment does not exist
	#if(isWindows()): os.system("install.bat")
	#else: os.system("sh install.sh")
	os.system("python -m venv app-env")
	command = "python -m pip install --upgrade pip && python -m pip install pydealer"
	if(isWindows()): os.system(f"app-env\\Scripts\\activate.bat && {command}")
	else: os.system(f"source app-env/bin/activate && {command}")

# launch Poker.py
if(isWindows()): os.system("app-env\\Scripts\\activate.bat && python Poker.py")
else: os.system("source app-env/bin/activate && python3 Poker.py")
