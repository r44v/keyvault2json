for %%X in (py.exe) do (set FOUND=%%~$PATH:X)
if defined FOUND GOTO found_py

for %%X in (python3.exe) do (set FOUND=%%~$PATH:X)
if defined FOUND GOTO found_python

GOTO missing

:found_python
   python3 -m pip install -U .
   GOTO:eof

:found_py
   py -3 -m pip install -U .
   GOTO:eof

:missing
   Echo Cannot find python
   GOTO:eof