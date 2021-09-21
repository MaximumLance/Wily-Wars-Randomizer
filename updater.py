import pathlib
import time
import urllib.request
import hashlib
import os

print("Now Updating...")

classes = False
srm = False
gatelib = False
update = 0

CHash = "7f8f916d3df87b713a95b3bdb8570bc9"
GHash = "63bc1507356f8496eac71e3789adda86"
SRMHash = "a1669b6c5c31743a62bb96f75713d759"

file = pathlib.Path('classes.py')
if file.exists() == False:
	classes = True

elif file.exists() == True:
        with open("classes.py", "rb") as f:
                Data = f.read()
                Hash = hashlib.md5(Data).hexdigest()
                if Hash != CHash:
                        classes = True
if classes == True:
	updatedfile = urllib.request.urlopen("https://raw.githubusercontent.com/MaximumLance/Wily-Wars-Randomizer/main/classes.py")
	updatedata = updatedfile.read()

	with open("classes.py", "wb") as f:
		f.write(updatedata)
	update += 1


file = pathlib.Path('gatelib.py')
if file.exists() == False:
	gatelib = True

elif file.exists() == True:
        with open("gatelib.py", "rb") as f:
                Data = f.read()
                Hash = hashlib.md5(Data).hexdigest()
                if Hash != GHash:
                        gatelib = True
if gatelib == True:
	updatedfile = urllib.request.urlopen("https://raw.githubusercontent.com/MaximumLance/Wily-Wars-Randomizer/main/gatelib.py")
	updatedata = updatedfile.read()

	with open("gatelib.py", "wb") as f:
		f.write(updatedata)
	update += 1


file = pathlib.Path('srm.py')
if file.exists() == False:
	srm = True

elif file.exists() == True:
        with open("srm.py", "rb") as f:
                Data = f.read()
                Hash = hashlib.md5(Data).hexdigest()
                if Hash != SRMHash:
                        srm = True
if srm == True:
	updatedfile = urllib.request.urlopen("https://raw.githubusercontent.com/MaximumLance/Wily-Wars-Randomizer/main/srm.py")
	updatedata = updatedfile.read()

	with open("srm.py", "wb") as f:
		f.write(updatedata)
	update += 1


file = pathlib.Path('randomizer.py')
url = "https://raw.githubusercontent.com/MaximumLance/Wily-Wars-Randomizer/main/randomizer.py"
urllib.request.urlretrieve(url, "randomizer2.py")
if file.exists() == False:
        os.rename("randomizer2.py", "randomizer.py")
        update += 1

elif file.exists() == True:
        with open("randomizer.py", "rb") as f:
                Data = f.read()
                Hash = hashlib.md5(Data).hexdigest()
                
        with open("randomizer2.py", "rb") as f:
                Data = f.read()
                Hash2 = hashlib.md5(Data).hexdigest()
                
        if Hash != Hash2:
                os.remove("randomizer.py")
                os.rename("randomizer2.py", "randomizer.py")
                update += 1
                
        elif Hash == Hash2:
                os.remove("randomizer2.py")


file = pathlib.Path('Logic.py')
url = "https://raw.githubusercontent.com/MaximumLance/Wily-Wars-Randomizer/main/Logic.py"
urllib.request.urlretrieve(url, "Logic2.py")
if file.exists() == False:
        os.rename("Logic2.py", "Logic.py")
        update += 1

elif file.exists() == True:
        with open("Logic.py", "rb") as f:
                Data = f.read()
                Hash = hashlib.md5(Data).hexdigest()
                
        with open("Logic2.py", "rb") as f:
                Data = f.read()
                Hash2 = hashlib.md5(Data).hexdigest()
                
        if Hash != Hash2:
                os.remove("Logic.py")
                os.rename("Logic2.py", "Logic.py")
                update += 1
                
        elif Hash == Hash2:
                os.remove("Logic2.py")


file = pathlib.Path('Wily Wars Randomizer Patch.ips')
url = "https://github.com/MaximumLance/Wily-Wars-Randomizer/raw/main/Wily%20Wars%20Randomizer%20patch.ips"
urllib.request.urlretrieve(url, "Wily Wars Randomizer Patch2.ips")
if file.exists() == False:
        os.rename("Wily Wars Randomizer Patch2.ips", "Wily Wars Randomizer Patch.ips")
        update += 1

elif file.exists() == True:
        with open("Wily Wars Randomizer Patch.ips", "rb") as f:
                Data = f.read()
                Hash = hashlib.md5(Data).hexdigest()
                
        with open("Wily Wars Randomizer Patch2.ips", "rb") as f:
                Data = f.read()
                Hash2 = hashlib.md5(Data).hexdigest()
                
        if Hash != Hash2:
                os.remove("Wily Wars Randomizer Patch.ips")
                os.rename("Wily Wars Randomizer Patch2.ips", "Wily Wars Randomizer Patch.ips")
                update += 1
                
        elif Hash == Hash2:
                os.remove("Wily Wars Randomizer Patch2.ips")


file = pathlib.Path('Wily Wars Randomizer Instructions.txt')
url = "https://raw.githubusercontent.com/MaximumLance/Wily-Wars-Randomizer/main/Wily%20Wars%20Randomizer%20Instructions.txt"
urllib.request.urlretrieve(url, "Wily Wars Randomizer Instructions2.txt")
if file.exists() == False:
        os.rename("Wily Wars Randomizer Instructions2.txt", "Wily Wars Randomizer Instructions.txt")
        update += 1

elif file.exists() == True:
        with open("Wily Wars Randomizer Instructions.txt", "rb") as f:
                Data = f.read()
                Hash = hashlib.md5(Data).hexdigest()
                
        with open("Wily Wars Randomizer Instructions2.txt", "rb") as f:
                Data = f.read()
                Hash2 = hashlib.md5(Data).hexdigest()
                
        if Hash != Hash2:
                os.remove("Wily Wars Randomizer Instructions.txt")
                os.rename("Wily Wars Randomizer Instructions2.txt", "Wily Wars Randomizer Instructions.txt")
                update += 1
                
        elif Hash == Hash2:
                os.remove("Wily Wars Randomizer Instructions2.txt")


file = pathlib.Path('Release Notes.txt')
url = "https://raw.githubusercontent.com/MaximumLance/Wily-Wars-Randomizer/main/Release%20notes.txt"
urllib.request.urlretrieve(url, "Release Notes2.txt")
if file.exists() == False:
        os.rename("Release Notes2.txt", "Release Notes.txt")
        update += 1

elif file.exists() == True:
        with open("Release Notes.txt", "rb") as f:
                Data = f.read()
                Hash = hashlib.md5(Data).hexdigest()
                
        with open("Release Notes2.txt", "rb") as f:
                Data = f.read()
                Hash2 = hashlib.md5(Data).hexdigest()
                
        if Hash != Hash2:
                os.remove("Release Notes.txt")
                os.rename("Release Notes.txt2", "Release Notes.txt")
                update += 1
                
        elif Hash == Hash2:
                os.remove("Release Notes.txt")


if update == 0:
	print("All files are up to date!")
if update > 0:
	print("Files were updated to the newest version!")
time.sleep(3)
