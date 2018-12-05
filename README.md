# WifiLMR
A land mobile radio-like product for unlicensed campus-wide use.

Getting Started
---------------

### Python Projects

1. Be on a GNU/Linux system, preferably a Debian-derivative (such as Ubuntu or Mint).
2. Make sure Python 3.x (where x >= 6) is installed.
3. Install pip (`sudo apt install python3-pip`)
4. Install virtualenv (`pip3 install --user virtualenv`)
5. Make a virtual environment for each project:
    * **radiomanager**: $REPO/env-man (`virtualenv env-man`)
    * **radioapp**: $REPO/env-app (`virtualenv env-app`)
6. Enter the environment for the project you're working on (`source env-$PROJ/bin/activate`)
7. Restore the project dependencies (`pip install -r requirements.txt` in the corresponding folder)