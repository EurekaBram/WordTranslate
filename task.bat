@ECHO OFF
cd /D "%~dp0"
PAUSE
ECHO running python script on file words.csv
python main.py words.csv
ECHO done
PAUSE