import os
import subprocess
import sys
import time
import re


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def wait():
    for x in range(1, 6):
        print('WAITING FOR FILE', ('.' * x))
        time.sleep(1)
        os.system('cls')


homepath = os.environ["HOMEPATH"]
desktops = []
if 'time' not in sys.modules:
    install(time)
    print('\nTime Module Successfully Installed')
else:
    print('\nTime module already installed')
print()


########################################################################

SEARCH_FOR = 'Desktop'  # change this to search for any directory

########################################################################

print('Searching for', SEARCH_FOR, '\n')

for root, dirs, files in os.walk(homepath):
    for dir_ in dirs:
        if dir_ == SEARCH_FOR:
            desktops.append(os.path.join(root, dir_))

if len(desktops) == 1:
    print('PATH_TO_DESKTOP')
    print(desktops[0])
    os.chdir(desktops[0])
else:
    usrdesk = min([desktop for desktop in desktops], key=len)
    print('PATH_TO_DESKTOP')
    print(usrdesk)
    print()
    os.chdir(usrdesk)

print('Waiting for file')
working_path = os.path.join(os.getcwd(), 'Convert-sentence-length')
if not os.path.isdir(working_path):
    os.mkdir(working_path)
    os.chdir(working_path)
else:
    os.chdir(working_path)

try:
    while not any(val.is_dir() or val.is_file() for val in os.scandir(working_path)):
        wait()
except AttributeError:
    print('Found a file!')
    time.sleep(3)
finally:
    for entry in os.scandir(working_path):
        with open(entry, 'r') as f:
            text = f.read().replace('\r', '').replace('\n', '')
        sentences = re.split(r' *[.?!][\'")\]]* *', text)
        with open('formatted-file.txt', 'w') as f:
            for i, sentence in enumerate(sentences):
                if i % 2 == 0:
                    f.write('{}.\n\n'.format(sentence))
                else:
                    f.write('{}. '.format(sentence))