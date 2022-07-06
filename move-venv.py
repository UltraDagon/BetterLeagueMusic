import os
source = 'venv/Lib/site-packages/'
allfiles = os.listdir(source)

for f in allfiles:
    os.rename(source + f, f)

quit()