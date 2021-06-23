from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pathlib import Path
import binascii
import time

Tk().withdraw() 
RandomizedROM = askopenfilename()
Filepath = Path(RandomizedROM)
Seed = (str(Filepath)) #Converts filepath to string.
Seed2=Seed.rpartition("-") #Trims everything after the last - in the file path
Seed = Seed2[2] #Assigns Seed to 2nd element in tuple from trim. Should be the seed value and file extension.
Seed2=Seed.rpartition(".")#Like before, trims everything around the last period
Seed = Seed2[0] #Assigns Seed to actual seed value

with open(RandomizedROM, "rb+") as ROM:
    Pointer = 0x85800 #Opens randomized Rom and sets offset to Pointer value
    Flag = []
    Seek = ROM.seek(Pointer,0)
    Vanilla = True
    MM3 = True
    MM2 = False
    for x in range(5): #Adds values from x85800-4 and joins them to the Flag list
        Byte = (ROM.read(1))
        Flag.append(Byte)
        Pointer+=1

    for x in range(5): #Checks to see what mode user took in previous program
        Flag1 = b'\x01'# by checking each value in the list.
        Flag2 = b'\x03'
        if Flag[x] == Flag1:
            randomboss = True
            Vanilla = False
        elif Flag[x] == Flag2:
            randomboss = True
            Vanilla = False
        else: #If no mode was chosen, sets value to false
            randomboss = False
            break

    for x in range(5): #Checks to see what mode user took in previous program
        Flag3 = b'\x02'# by checking each value in the list.
        Flag4 = b'\x03'
        if Flag[x] == Flag3:
            randomweapons = True
            Vanilla = False
        elif Flag[x] == Flag4:
            randomweapons = True
            Vanilla = False
        else: #If no mode was chosen, sets value to false
            randomweapons = False
            break
        
    randombuster = False
    randomdamage = False
    randomammo = False
    Pointer = 0x85A09 #Checks to see if user wants Random Buster,Damage from Bosses, or Ammo Usage
    Seek = ROM.seek(Pointer,0)
    Value = ROM.read(1)
    Flag5 = b'\x00'
    Flag6 = b'\x01'
    if Value == Flag5:
        Pointer = 0x85A0A
        Seek = ROM.seek(Pointer,0)
        Value = ROM.read(1)
        if Value == Flag6:
            randombuster = True

    Pointer = 0x85A0B
    Seek = ROM.seek(Pointer,0)
    Value = ROM.read(1)
    if Value == Flag5:
        Pointer = 0x85A0C
        Seek = ROM.seek(Pointer,0)
        Value = ROM.read(1)
        if Value == Flag6:
            randomdamage = True

    Pointer = 0x85A0D
    Seek = ROM.seek(Pointer,0)
    Value = ROM.read(1)
    if Value == Flag5:
        Pointer = 0x85A0E
        Seek = ROM.seek(Pointer,0)
        Value = ROM.read(1)
        if Value == Flag6:
            randomammo = True

    Pointer = 0x85A19 #Checking to see if User wants MM2
    Seek = ROM.seek(Pointer,0)
    Value = ROM.read(1)
    Flag3 = b'\x02'
    if Value == Flag5:
        Pointer = 0x85A1A
        Seek = ROM.seek(Pointer,0)
        Value = ROM.read(1)
        if Value == Flag3:
            MM2 = True
            MM3 = False
            

#This is the seed value writing section.        
    if len(Seed) <= 12: 
        Seedlist = []
        Seedlist[:] = Seed #Splits characters of seed into individual elements
        Seedbyte = []
        for x in range(len(Seed)): #Checks what the character of the element is and assigns value to Seedbyte once match is found.
            if Seedlist[x] == "0":
                Value = b'\x30'
            elif Seedlist[x] == "1":
                Value = b'\x31'
            elif Seedlist[x] == "2":
                Value = b'\x32'
            elif Seedlist[x] == "3":
                Value = b'\x33'
            elif Seedlist[x] == "4":
                Value = b'\x34'
            elif Seedlist[x] == "5":
                Value = b'\x35'
            elif Seedlist[x] == "6":
                Value = b'\x36'
            elif Seedlist[x] == "7":
                Value = b'\x37'
            elif Seedlist[x] == "8":
                Value = b'\x38'
            elif Seedlist[x] == "9":
                Value = b'\x39'
            elif Seedlist[x] == "A":
                Value = b'\x41'
            elif Seedlist[x] == "B":
                Value = b'\x42'
            elif Seedlist[x] == "C":
                Value = b'\x43'
            elif Seedlist[x] == "D":
                Value = b'\x44'
            elif Seedlist[x] == "E":
                Value = b'\x45'
            elif Seedlist[x] == "F":
                Value = b'\x46'
            elif Seedlist[x] == "G":
                Value = b'\x47'
            elif Seedlist[x] == "H":
                Value = b'\x48'
            elif Seedlist[x] == "I":
                Value = b'\x49'
            elif Seedlist[x] == "J":
                Value = b'\x4A'
            elif Seedlist[x] == "K":
                Value = b'\x4B'
            elif Seedlist[x] == "L":
                Value = b'\x4C'
            elif Seedlist[x] == "M":
                Value = b'\x4D'
            elif Seedlist[x] == "N":
                Value = b'\x4E'
            elif Seedlist[x] == "O":
                Value = b'\x4F'
            elif Seedlist[x] == "P":
                Value = b'\x50'
            elif Seedlist[x] == "Q":
                Value = b'\x51'
            elif Seedlist[x] == "R":
                Value = b'\x52'
            elif Seedlist[x] == "S":
                Value = b'\x53'
            elif Seedlist[x] == "T":
                Value = b'\x54'
            elif Seedlist[x] == "U":
                Value = b'\x55'
            elif Seedlist[x] == "V":
                Value = b'\x56'
            elif Seedlist[x] == "W":
                Value = b'\x57'
            elif Seedlist[x] == "X":
                Value = b'\x58'
            elif Seedlist[x] == "Y":
                Value = b'\x59'
            elif Seedlist[x] == "Z":
                Value = b'\x5A'
            Seedbyte.append(Value)
        Pointer = [0x199B4D,0x199B4F,0x199B55,0x199B57,0x199B5D,0x199B5F,0x199B65,0x199B67,0x199B6D,0x199B6F,0x199B75,0x199B77] #Addresses for seed value
        for x in range(len(Seed)): #Writes values to addresses
            Seek = ROM.seek(Pointer[x],0)
            ROM.write(Seedbyte[x])
    else:
        print("Seed value is more than 12.")

#This is the Boss encountered list writing if no randomboss #!   
    Cutman = b'\x00'
    Cutmanboss =  b'\x18'
    Gutsman = b'\x01'
    Gutsmanboss =  b'\x19'
    Iceman = b'\x02'
    Icemanboss =  b'\x14'
    Bombman = b'\x03'
    Bombmanboss =  b'\x15'
    Fireman = b'\x04'
    Firemanboss =  b'\x16'
    Elecman = b'\x05'
    Elecmanboss =  b'\x17'

    Bubbleman = b'\x14'
    Bubblemanboss =  b'G'
    Airman = b'\x15'
    Airmanboss =  b'A'
    Quickman = b'\x16'
    Quickmanboss =  b'F'
    Heatman = b'\x17'
    Heatmanboss =  b'H'
    Woodman = b'\x18'
    Woodmanboss =  b'D'
    Metalman = b'\x19'
    Metalmanboss =  b'C'
    Flashman = b'\x1A'
    Flashmanboss =  b'E'
    Crashman = b'\x1B'
    Crashmanboss =  b'B'

    Sparkman = b'('
    Sparkmanboss =  b'x'
    Snakeman = b')'
    Snakemanboss =  b'v'
    Needleman = b'*'
    Needlemanboss =  b'z'
    Hardman = b'+'
    Hardmanboss =  b't'
    Topman = b','
    Topmanboss =  b'u'
    Geminiman = b'-'
    Geminimanboss =  b'{'
    Magnetman = b'.'
    Magnetmanboss =  b'w'
    Shadowman = b'/'
    Shadowmanboss =  b'y'
    pos = []
    Stages = []
    Bosses = []
    Epos = []
    Next = [b'\x19',b'\x2A',b'\x03',b'\x15',b'\x2E',b'\x16',b'\x18',b'\x00',b'\x1A',]
    Pointer = 0x644C2
    Seek = ROM.seek(Pointer,0)
    for x in range(8): #!Adds values from x644C2-9 and joins them to the Stages list
        Byte = ROM.read(1)
        Stages.append(Byte)
        Pointer+=1
    Error = False
    for x in range(8): # Error checking section for stages
        Value = Stages[x]
        for y in range(8):
                if Value == Stages[y]:
                    if x != y:
                        Error = True
                        Epos.append(y)                   
    if Error == True:
        for x in range(9):
            Value = Stages.count(Next[x])
            if Value == 0:
                Backup = Next[x]
                Value2 = x
                break
        Errors = len(Epos)
        Value = Epos.pop()
        Stages.pop(Value)
        Stages.append(Backup)
        Errors -= 2
        Epos.pop()
        if Errors > 1:
            Errors -= 1
            for x in range(Errors):
                Value = Epos.pop()
                Epos.pop()
                Stages.pop(Value)
                Value2 += 1
                Value3 = Next[Value2]
                Retry = False
                if Value2 == 9:
                    print("Something went wrong with the logic script when trying to replace duplicate stages. Please run this script again. If this continues to happen, contact me.")
                    ROM.close()
                    time.sleep(13)  
                for y in range(7):
                    if Stages[y] == Value3:
                        Retry = True
                        Value2 += 1
                        break
                if Retry == False:
                    Stages.append(Value3)
                    
        
    for x in range(8): #Checks to see what the bosses are based on stages, gives them a true value if matched, and adds them to the pos list for future values
        if Stages[x] == Cutman:
            if Vanilla == True:
                Cutman = True
            pos.append(["Cutman" , x]) 
        elif Stages[x] == Gutsman:
            if Vanilla == True:
                Gutsman = True
            pos.append(["Gutsman" , x])
        elif Stages[x] == Iceman:
            if Vanilla == True:
                Iceman = True
            pos.append(["Iceman" , x])
        elif Stages[x] == Bombman:
            if Vanilla == True:
                Bombman = True
            pos.append(["Bombman" , x])
        elif Stages[x] == Fireman:
            if Vanilla == True:
                Fireman = True
            pos.append(["Fireman" , x])
        elif Stages[x] == Elecman:
            if Vanilla == True:
                Elecman = True
            pos.append(["Elecman" , x])
        elif Stages[x] == Bubbleman:
            if Vanilla == True:
                Bubbleman = True
            pos.append(["Bubbleman" , x])
        elif Stages[x] == Airman:
            if Vanilla == True:
                Airman = True
            pos.append(["Airman" , x])
        elif Stages[x] == Quickman:
            if Vanilla == True:
                Quickman = True
            pos.append(["Quickman" , x])
        elif Stages[x] == Heatman:
            if Vanilla == True:
                Heatman = True
            pos.append(["Heatman" , x])
        elif Stages[x] == Woodman:
            if Vanilla == True:
                Woodman = True
            pos.append(["Woodman" , x])
        elif Stages[x] == Metalman:
            if Vanilla == True:
                Metalman = True
            pos.append(["Metalman" , x])
        elif Stages[x] == Flashman:
            if Vanilla == True:
                Flashman = True
            pos.append(["Flashman" , x])
        elif Stages[x] == Crashman:
            if Vanilla == True:
                Crashman = True
            pos.append(["Crashman" , x])
        elif Stages[x] == Sparkman:
            if Vanilla == True:
                Sparkman = True
            pos.append(["Sparkman" , x])
        elif Stages[x] == Snakeman:
            if Vanilla == True:
                Snakeman = True
            pos.append(["Snakeman" , x])
        elif Stages[x] == Needleman:
            if Vanilla == True:
                Needleman = True
            pos.append(["Needleman" , x])
        elif Stages[x] == Hardman:
            if Vanilla == True:
                Hardman = True
            pos.append(["Hardman" , x])
        elif Stages[x] == Topman:
            if Vanilla == True:
                Topman = True
            pos.append(["Topman" , x])
        elif Stages[x] == Geminiman:
            if Vanilla == True:
                Geminiman = True
            pos.append(["Geminiman" , x])
        elif Stages[x] == Magnetman:
            if Vanilla == True:
                Magnetman = True
            pos.append(["Magnetman" , x])
        elif Stages[x] == Shadowman:
            if Vanilla == True:
                Shadowman = True
            pos.append(["Shadowman" , x])

    #If encountering MM3 stage, rearranges pos list to have them placed in their respective positions
    rearrange = False
    pos2 = []
    if MM3 == True: #!
        for x in range(8):
            if pos[x][0] == "Sparkman":
                if x != 0:
                    rearrange = True
            elif pos[x][0] == "Snakeman":
                if x != 1:
                    rearrange = True
            elif pos[x][0] == "Needleman":
                if x != 2:
                    rearrange = True
            elif pos[x][0] == "Hardman":
                if x != 3:
                    rearrange = True
            elif pos[x][0] == "Topman":
                if x != 4:
                    rearrange = True
            elif pos[x][0] == "Geminiman":
                if x != 5:
                    rearrange = True
            elif pos[x][0] == "Magnetman":
                if x != 6:
                    rearrange = True
            elif pos[x][0] == "Shadowman":
                if x != 7:
                    rearrange = True
        if rearrange == True: #If a MM3 stage was found, rebuilds the pos list
                for x in range(8):
                    pos2.append(pos[x][0])
                        
                pos.clear()
                    
                for y in range(3):
                    for x in range(8): #Runs through this loop three times for accuracy on proper positioning
                        if pos2[x] == "Sparkman":
                            pos2.pop(x)
                            pos2.insert(0, "Sparkman")
                        elif pos2[x] == "Snakeman":
                            pos2.pop(x)
                            pos2.insert(1, "Snakeman")
                        elif pos2[x] == "Needleman":
                            pos2.pop(x)
                            pos2.insert(2,"Needleman")
                        elif pos2[x] == "Hardman":
                            pos2.pop(x)
                            pos2.insert(3,"Hardman")
                        elif pos2[x] == "Topman":
                            pos2.pop(x)
                            pos2.insert(4, "Topman")
                        elif pos2[x] == "Geminiman":
                            pos2.pop(x)
                            pos2.insert(5, "Geminiman")
                        elif pos2[x] == "Magnetman":
                            pos2.pop(x)
                            pos2.insert(6, "Magnetman")
                        elif pos2[x] == "Shadowman":
                            pos2.pop(x)
                            pos2.insert(7, "Shadowman")

                 

                for x in range(8): #Reassigns boss and position id to old pos list
                    pos.append([pos2[x], x])

                pos2.clear()
    #If encountering MM2 stage in MM2 Mode, rearranges pos list to have them placed in their respective positions            
    if MM2 == True: #!
        for x in range(8):
            if pos[x][0] == "Bubbleman":
                if x != 0:
                    rearrange = True
            elif pos[x][0] == "Airman":
                if x != 1:
                    rearrange = True
            elif pos[x][0] == "Quickman":
                if x != 2:
                    rearrange = True
            elif pos[x][0] == "Heatman":
                if x != 3:
                    rearrange = True
            elif pos[x][0] == "Woodman":
                if x != 4:
                    rearrange = True
            elif pos[x][0] == "Metalman":
                if x != 5:
                    rearrange = True
            elif pos[x][0] == "Flashman":
                if x != 6:
                    rearrange = True
            elif pos[x][0] == "Crashman":
                if x != 7:
                    rearrange = True
        if rearrange == True: #If a MM2 stage was found, rebuilds the pos list
                for x in range(8):
                    pos2.append(pos[x][0])
                        
                pos.clear()
                    
                for y in range(3):
                    for x in range(8): #Runs through this loop three times for accuracy on proper positioning
                        if pos2[x] == "Bubbleman":
                            pos2.pop(x)
                            pos2.insert(0, "Bubbleman")
                        elif pos2[x] == "Airman":
                            pos2.pop(x)
                            pos2.insert(1, "Airman")
                        elif pos2[x] == "Quickman":
                            pos2.pop(x)
                            pos2.insert(2,"Quickman")
                        elif pos2[x] == "Heatman":
                            pos2.pop(x)
                            pos2.insert(3,"Heatman")
                        elif pos2[x] == "Woodman":
                            pos2.pop(x)
                            pos2.insert(4, "Woodman")
                        elif pos2[x] == "Metalman":
                            pos2.pop(x)
                            pos2.insert(5, "Metalman")
                        elif pos2[x] == "Flashman":
                            pos2.pop(x)
                            pos2.insert(6, "Flashman")
                        elif pos2[x] == "Crashman":
                            pos2.pop(x)
                            pos2.insert(7, "Crashman")

                for x in range(8): #Reassigns boss and position id to old pos list
                    pos.append([pos2[x], x])

                pos2.clear()
                
    Pointer = 0x644C2
    Seek = ROM.seek(Pointer,0)
    for x in range(8): #Sets values for stages based on new pos
        if pos[x][0] == "Cutman":
            ROM.write(b'\x00')
            Pointer+=1
        elif pos[x][0] == "Gutsman":
            ROM.write(b'\x01')
            Pointer+=1
        elif pos[x][0] == "Iceman":
            ROM.write(b'\x02')
            Pointer+=1
        elif pos[x][0] == "Bombman":
            ROM.write(b'\x03')
            Pointer+=1
        elif pos[x][0] == "Fireman":
            ROM.write(b'\x04')
            Pointer+=1
        elif pos[x][0] == "Elecman":
            ROM.write(b'\x05')
            Pointer+=1
        elif pos[x][0] == "Bubbleman":
            ROM.write(b'\x14')
            Pointer+=1
        elif pos[x][0] == "Airman":
            ROM.write(b'\x15')
            Pointer+=1
        elif pos[x][0] == "Quickman":
            ROM.write(b'\x16')
            Pointer+=1
        elif pos[x][0] == "Heatman":
            ROM.write(b'\x17')
            Pointer+=1
        elif pos[x][0] == "Woodman":
            ROM.write(b'\x18')
            Pointer+=1
        elif pos[x][0] == "Metalman":
            ROM.write(b'\x19')
            Pointer+=1
        elif pos[x][0] == "Flashman":
            ROM.write(b'\x1A')
            Pointer+=1
        elif pos[x][0] == "Crashman":
            ROM.write(b'\x1B')
            Pointer+=1
        elif pos[x][0] == "Sparkman":
            ROM.write(b'\x28')
            Pointer+=1
        elif pos[x][0] == "Snakeman":
            ROM.write(b'\x29')
            Pointer+=1
        elif pos[x][0] == "Needleman":
            ROM.write(b'\x2A')
            Pointer+=1
        elif pos[x][0] == "Hardman":
            ROM.write(b'\x2B')
            Pointer+=1
        elif pos[x][0] == "Topman":
            ROM.write(b'\x2C')
            Pointer+=1
        elif pos[x][0] == "Geminiman":
            ROM.write(b'\x2D')
            Pointer+=1
        elif pos[x][0] == "Magnetman":
            ROM.write(b'\x2E')
            Pointer+=1
        elif pos[x][0] == "Shadowman":
            ROM.write(b'\x2F')
            Pointer+=1
            

#This is the Boss encountered list writing if randomboss
    if randomboss == True: #!
        posB = []
        Next.clear()
        Epos.clear()
        Next = [b'\x48',b'\x47',b'\x74',b'\x76',b'\x46',b'\x18',b'\x43',b'\x7B',b'\x15']
        Pointer = 0x85990
        Seek = ROM.seek(Pointer,0)
        for x in range(8): #Adds values from x85990-7 and joins them to the Bosses list
            Byte = (ROM.read(1))
            Bosses.append(Byte)
            Pointer+=1
 
        Error = False
        for x in range(8): # Error checking section for bosses
            Value = Bosses[x]
            for y in range(8):
                    if Value == Bosses[y]:
                        if x != y:
                            Error = True
                            Epos.append(y)
        if Error == True:
            for x in range(9):
                Value = Bosses.count(Next[x])
                if Value == 0:
                    Backup = Next[x]
                    Value2 = x
                    break
            Errors = len(Epos)
            Value = Epos.pop()
            Bosses.pop(Value)
            Bosses.append(Backup)
            Errors -= 2
            Epos.pop()
            if Errors > 1:
                Errors -= 1
                for x in range(Errors):
                    Value = Epos.pop()
                    Epos.pop()
                    Bosses.pop(Value)
                    Value2 += 1
                    Value3 = Next[Value2]
                    Retry = False
                    if Value2 == 9:
                        print("Something went wrong with the logic script when trying to replace duplicate bosses. Please run this script again. If this continues to happen, contact me.")
                        ROM.close()
                        time.sleep(13)  
                    for y in range(7):
                        if Bosses[y] == Value3:
                            Retry = True
                            Value2 += 1
                            break
                    if Retry == False:
                        Bosses.append(Value3)
                        
        for x in range(8): #Checks to see what the bosses are based on generated values, gives them a true value if matched, and adds them to the pos list for future values
            if Bosses[x] == Cutmanboss:
                Cutman = True
                posB.append(["Cutman" , x]) 
            elif Bosses[x] == Gutsmanboss:
                Gutsman = True
                posB.append(["Gutsman" , x])
            elif Bosses[x] == Icemanboss:
                Iceman = True
                posB.append(["Iceman" , x])
            elif Bosses[x] == Bombmanboss:
                Bombman = True
                posB.append(["Bombman" , x])
            elif Bosses[x] == Firemanboss:
                Fireman = True
                posB.append(["Fireman" , x])
            elif Bosses[x] == Elecmanboss:
                Elecman = True
                posB.append(["Elecman" , x])
            elif Bosses[x] == Bubblemanboss:
                Bubbleman = True
                posB.append(["Bubbleman" , x])
            elif Bosses[x] == Airmanboss:
                Airman = True
                posB.append(["Airman" , x])
            elif Bosses[x] == Quickmanboss:
                Quickman = True
                posB.append(["Quickman" , x])
            elif Bosses[x] == Heatmanboss:
                Heatman = True
                posB.append(["Heatman" , x])
            elif Bosses[x] == Woodmanboss:
                Woodman = True
                posB.append(["Woodman" , x])
            elif Bosses[x] == Metalmanboss:
                Metalman = True
                posB.append(["Metalman" , x])
            elif Bosses[x] == Flashmanboss:
                Flashman = True
                posB.append(["Flashman" , x])
            elif Bosses[x] == Crashmanboss:
                Crashman = True
                posB.append(["Crashman" , x])
            elif Bosses[x] == Sparkmanboss:
                Sparkman = True
                posB.append(["Sparkman" , x])
            elif Bosses[x] == Snakemanboss:
                Snakeman = True
                posB.append(["Snakeman" , x])
            elif Bosses[x] == Needlemanboss:
                Needleman = True
                posB.append(["Needleman" , x])
            elif Bosses[x] == Hardmanboss:
                Hardman = True
                posB.append(["Hardman" , x])
            elif Bosses[x] == Topmanboss:
                Topman = True
                posB.append(["Topman" , x])
            elif Bosses[x] == Geminimanboss:
                Geminiman = True
                posB.append(["Geminiman" , x])
            elif Bosses[x] == Magnetmanboss:
                Magnetman = True
                posB.append(["Magnetman" , x])
            elif Bosses[x] == Shadowmanboss:
                Shadowman = True
                posB.append(["Shadowman" , x])
                
#Converts pos list to addresses to write value for boss encountered                
        Stageaddress = []
        for x in range(8): #!
            if pos[x][0] == "Cutman":
                Value = 0x77E19
                Stageaddress.append(Value)
            elif pos[x][0] == "Gutsman":
                Value = 0x77FBB
                Stageaddress.append(Value)
            elif pos[x][0] == "Iceman":
                Value = 0x781BB
                Stageaddress.append(Value)
            elif pos[x][0] == "Bombman":
                Value = 0x783DB
                Stageaddress.append(Value)
            elif pos[x][0] == "Fireman":
                Value = 0x7860B
                Stageaddress.append(Value)
            elif pos[x][0] == "Elecman":
                Value = 0x78903
                Stageaddress.append(Value)
            elif pos[x][0] == "Bubbleman":
                Value = 0x7914D
                Stageaddress.append(Value)
            elif pos[x][0] == "Airman":
                Value = 0x792B1
                Stageaddress.append(Value)
            elif pos[x][0] == "Quickman":
                Value = 0x79591
                Stageaddress.append(Value)
            elif pos[x][0] == "Heatman":
                Value = 0x79811
                Stageaddress.append(Value)
            elif pos[x][0] == "Woodman":
                Value = 0x799D1
                Stageaddress.append(Value)
            elif pos[x][0] == "Metalman":
                Value = 0x79B25
                Stageaddress.append(Value)
            elif pos[x][0] == "Flashman":
                Value = 0x79C9D
                Stageaddress.append(Value)
            elif pos[x][0] == "Crashman":
                Value = 0x79E65
                Stageaddress.append(Value)
            elif pos[x][0] == "Sparkman":
                Value = 0x7A7ED
                Stageaddress.append(Value)
            elif pos[x][0] == "Snakeman":
                Value = 0x7AAD9
                Stageaddress.append(Value)
            elif pos[x][0] == "Needleman":
                Value = 0x7AC63
                Stageaddress.append(Value)
            elif pos[x][0] == "Hardman":
                Value = 0x7AE53
                Stageaddress.append(Value)
            elif pos[x][0] == "Topman":
                Value = 0x7B027
                Stageaddress.append(Value)
            elif pos[x][0] == "Geminiman":
                Value = 0x7B2F3
                Stageaddress.append(Value)
            elif pos[x][0] == "Magnetman":
                Value = 0x7B4A9
                Stageaddress.append(Value)
            elif pos[x][0] == "Shadowman":
                Value = 0x7B6BB
                Stageaddress.append(Value)
                
#Writes boss value to stage address based on bosses chosen
        Mirror = b'\x01' #Guts, Fire, and Bomb need to be mirrored
        RearrangeMe = False
        RearrangeMa = False
        for x in range(8): #!
            if posB[x][1] == x: #This condition is unneccessary.
                if posB[x][0] == "Cutman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    if Pointer == 0x7AC63: # If MM1 Boss is in Hardman or Needleman stage, adjust vertical position
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xD4')
                    elif Pointer == 0x7AE53:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB4')
                    elif Pointer == 0x79591:# If MM1 Boss is in Quick,Heat,Wood, or Metal, adjust vertical position
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xA5')
                    elif Pointer == 0x79811:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                    elif Pointer == 0x799D1:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                    elif Pointer == 0x79B25:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                elif posB[x][0] == "Gutsman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    if Pointer == 0x7AC63:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xD4')
                        Pointer = Stageaddress[x]# Since Guts, Bomb, and Fire need to be mirrored, this will bring back to original address
                    elif Pointer == 0x7AE53:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB4')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79591:
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xA5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79811:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x799D1:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79B25:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    Pointer += 3
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Mirror)
                elif posB[x][0] == "Iceman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    if Pointer == 0x7AC63:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xD4')
                    elif Pointer == 0x7AE53:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB4')
                    elif Pointer == 0x79591:
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xA5')
                    elif Pointer == 0x79811:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                    elif Pointer == 0x799D1:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                    elif Pointer == 0x79B25:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                elif posB[x][0] == "Bombman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    if Pointer == 0x7AC63:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xD4')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x7AE53:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB4')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79591:
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xA5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79811:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x799D1:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79B25:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    Pointer += 3
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Mirror)
                elif posB[x][0] == "Fireman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    if Pointer == 0x7AC63:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xD4')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x7AE53:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB4')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79591:
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xA5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79811:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x799D1:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    elif Pointer == 0x79B25:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                        Pointer = Stageaddress[x]
                    Pointer += 3
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Mirror)
                elif posB[x][0] == "Elecman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    if Pointer == 0x7AC63:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xD4')
                    elif Pointer == 0x7AE53:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB4')
                    elif Pointer == 0x79591:
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xA5')
                    elif Pointer == 0x79811:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                    elif Pointer == 0x799D1:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                    elif Pointer == 0x79B25:
                        Pointer += 2
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xB5')
                elif posB[x][0] == "Bubbleman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Airman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Quickman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Heatman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Woodman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Metalman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    if Pointer == 0x7AE53:
                        RearrangeMe = True
                        Posi = x
                    elif Pointer == 0x7B2F3:
                        RearrangeMe = True
                        Posi = x
                    elif Pointer == 0x7B4A9:
                        RearrangeMe = True
                        Posi = x
                    elif Pointer == 0x7B6BB:
                        RearrangeMe = True
                        Posi = x
                elif posB[x][0] == "Flashman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Crashman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Sparkman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Snakeman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Needleman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Hardman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Topman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Geminiman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                elif posB[x][0] == "Magnetman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    if Pointer == 0x77FBB:
                        RearrangeMa = True
                        Posi2 = x
                    elif Pointer == 0x792B1:
                        RearrangeMa = True
                        Posi2 = x
                    elif Pointer == 0x79591:
                        RearrangeMa = True
                        Posi2 = x
                    elif Pointer == 0x79E65:
                        RearrangeMa = True
                        Posi2 = x
                elif posB[x][0] == "Shadowman":
                    Pointer = Stageaddress[x]
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Bosses[x])
                    
        Unmirror = b'\x00'
        MetalV = b'\x43'
        MagnetV = b'\x77'
        Remir = False
        if RearrangeMe == True: #! If Metalman is a boss in Hard, Gemini, Magnet, or Shadow, replace him with another boss
            if posB[1][0] == "Gutsman": #Because of MM3 rearrange, there will never be a condition where Stage 1 is a forbidden stage
                 Remir = True
            elif posB[1][0] == "Bombman":
                 Remir = True
            elif posB[1][0] == "Fireman":
                 Remir = True
            Pointer = Stageaddress[1] #Saving boss value in Stage 1 for swap then writing Metalman value
            Seek = ROM.seek(Pointer,0)
            Value = ROM.read(1)
            Seek = ROM.seek(Pointer,0)
            ROM.write(MetalV)
            if Remir == True: #If if was Bomb, Guts, or Fire, unmirror boss sprite
                Pointer += 3
                Seek = ROM.seek(Pointer,0)
                ROM.write(Unmirror)
                
            Pointer = Stageaddress[Posi] #Write boss value from 1 to where Metalman was
            Seek = ROM.seek(Pointer,0)
            ROM.write(Value)
            if Remir == True:
                Pointer += 3
                Seek = ROM.seek(Pointer,0)
                ROM.write(Mirror)
                
            String = posB[1][0] #Exchange posB values to accurately reflect which boss is where
            String2 = posB[Posi][0]
            posB.pop(1)
            posB.insert(1, [String2, 1])
            posB.pop(Posi)
            posB.insert(Posi, [String, Posi])
            Remir = False

        if RearrangeMa == True:
            if Posi2 != 5: #Checks to see if Magnetman is already in Stage 5. If not, will write there. If so, uses Stage 4.
                y = 5
            elif Posi2 == 5:
                y = 4
                
            Pointer = Stageaddress[y]
            Seek = ROM.seek(Pointer, 0)
            Value = ROM.read(1)
            Seek = ROM.seek(Pointer, 0)
            ROM.write(MagnetV)
            if posB[y][0] == "Gutsman":
                Remir = True
            elif posB[y][0] == "Bombman":
                Remir = True
            elif posB[y][0] == "Fireman":
                Remir = True
            if Remir == True:
                Pointer += 3
                Seek = ROM.seek(Pointer, 0)
                ROM.write(Unmirror)
            Pointer = Stageaddress[Posi2]
            Seek = ROM.seek(Pointer, 0)
            ROM.write(Value)
            if Remir == True:
                Pointer += 3
                Seek = ROM.seek(Pointer, 0)
                ROM.write(Mirror)

            String = posB[y][0]
            String2 = posB[Posi2][0]
            posB.pop(y)
            posB.insert(y, [String2, y])
            posB.pop(Posi2)
            posB.insert(Posi2, [String, Posi2])
                
                   
#Checks to see if player will receive Time Stopper
    Flash = False
    TimeS = 9
    if randomweapons == True: #!
        Pointer = 0x859A0
        Seek = ROM.seek(Pointer,0)
        Stopper = b'\x0e'
        for x in range(8):
            Value = ROM.read(1)
            if Value == Stopper:
                Flash = True
                TimeS = x
                    
    if Flashman == True:
        Flash = True

    if Flash == True:
        First = True
        Pointer = 0x8580A 
        Seek = ROM.seek(Pointer,0)
        TimeStopperAffected = (ROM.read(1))
        Stopper = int.from_bytes(TimeStopperAffected, "big")
        Stopper -= 1
        if Vanilla == True:
            BossAffected = pos[Stopper][0] #Assigns a random boss to be affected by Time Stopper
        if randomboss == True:
            BossAffected = posB[Stopper][0]
        if BossAffected == "Flashman": #But not Flashman
            First = False
            Pointer = 0x8580B #Goes to next randomly generated value if Flashman
            Seek = ROM.seek(Pointer,0)
            TimeStopperAffected = (ROM.read(1))
            Stopper = int.from_bytes(TimeStopperAffected, "big")
            Stopper -= 1
            if Vanilla == True:
                BossAffected = pos[Stopper][0]
            if randomboss == True:
                BossAffected = posB[Stopper][0]   
        if BossAffected == "Cutman": #Assigns boss value by randomly chosen boss
            Value = b'\x18'
        elif BossAffected == "Gutsman":
            Value = b'\x19'
        elif BossAffected == "Iceman":
            Value = b'\x14'
        elif BossAffected == "Bombman":
            Value = b'\x15'
        elif BossAffected == "Fireman":
            Value = b'\x16'
        elif BossAffected == "Elecman":
            Value = b'\x17'
        elif BossAffected == "Bubbleman":
            Value = b'\x47'
        elif BossAffected == "Airman":
            Value = b'\x41'
        elif BossAffected == "Quickman":
            Value = b'\x46'
        elif BossAffected == "Heatman":
            Value = b'\x48'
        elif BossAffected == "Woodman":
            Value = b'\x44'
        elif BossAffected == "Metalman":
            Value = b'\x43'
        elif BossAffected == "Crashman":
            Value = b'\x42'
        elif BossAffected == "Sparkman":
            Value = b'\x78'
        elif BossAffected == "Snakeman":
            Value = b'\x76'
        elif BossAffected == "Needleman":
            Value = b'\x7A'
        elif BossAffected == "Hardman":
            Value = b'\x74'
        elif BossAffected == "Topman":
            Value = b'\x75'
        elif BossAffected == "Geminiman":
            Value = b'\x7B'
        elif BossAffected == "Magnetman":
            Value = b'\x77'
        elif BossAffected == "Shadowman" :
            Value = b'\x79'
        Pointer = 0x85633 #Sets value from if statements to have game check which boss is affected by Time Stopper
        Seek = ROM.seek(Pointer,0)
        ROM.write(Value)
        
        if MM2 == True: #!
            if First == True:
                Pointer = 0x8580B #Checks to see if next value generated is Flashman
            elif First == False:
                Pointer = 0x8580C
            Seek = ROM.seek(Pointer,0)
            TimeStopperAffected = (ROM.read(1))
            Stopper2 = int.from_bytes(TimeStopperAffected, "big")
            Stopper2 -= 1
            if Stopper == Stopper2: #Check for 30 different ways to make sure there isn't a duplicate value or the value is Flashman...
                Stopper2 -= 1
                if Stopper2 < 0:
                    Stopper2 += 2
            if Vanilla == True:
                BossAffected = pos[Stopper2][0]
            if randomboss == True:
                BossAffected = posB[Stopper2][0]
                
            if BossAffected == "Flashman":
                if First == True:
                    Pointer = 0x8580C #Goes to next randomly generated value if Flashman
                    Seek = ROM.seek(Pointer,0)
                    TimeStopperAffected = (ROM.read(1))
                    Stopper3 = int.from_bytes(TimeStopperAffected, "big")
                    Stopper3 -= 1
                    if Stopper3 != Stopper:
                        if Stopper3 != Stopper2:
                            if Vanilla == True:
                                BossAffected = pos[Stopper3][0]
                            if randomboss == True:
                                BossAffected = posB[Stopper3][0]
                    elif Stopper3 == Stopper:
                        First = False
                    elif Stopper3 == Stopper2:
                        First = False
                if First == False:
                    if Stopper != Stopper2:
                        Stopper3 = Stopper + 1
                    if Stopper3 == Stopper2:
                        Stopper3 = Stopper2 + 1
                    if Stopper3 > 7:
                        Stopper3 -= 3
                    if Vanilla == True:
                        BossAffected = pos[Stopper3][0]
                    if randomboss == True:
                        BossAffected = posB[Stopper3][0]
                        
        if BossAffected == "Cutman": #Assigns boss value by randomly chosen boss
            Value = b'\x18'
        elif BossAffected == "Gutsman":
            Value = b'\x19'
        elif BossAffected == "Iceman":
            Value = b'\x14'
        elif BossAffected == "Bombman":
            Value = b'\x15'
        elif BossAffected == "Fireman":
            Value = b'\x16'
        elif BossAffected == "Elecman":
            Value = b'\x17'
        elif BossAffected == "Bubbleman":
            Value = b'\x47'
        elif BossAffected == "Airman":
            Value = b'\x41'
        elif BossAffected == "Quickman":
            Value = b'\x46'
        elif BossAffected == "Heatman":
            Value = b'\x48'
        elif BossAffected == "Woodman":
            Value = b'\x44'
        elif BossAffected == "Metalman":
            Value = b'\x43'
        elif BossAffected == "Crashman":
            Value = b'\x42'
        elif BossAffected == "Sparkman":
            Value = b'\x78'
        elif BossAffected == "Snakeman":
            Value = b'\x76'
        elif BossAffected == "Needleman":
            Value = b'\x7A'
        elif BossAffected == "Hardman":
            Value = b'\x74'
        elif BossAffected == "Topman":
            Value = b'\x75'
        elif BossAffected == "Geminiman":
            Value = b'\x7B'
        elif BossAffected == "Magnetman":
            Value = b'\x77'
        elif BossAffected == "Shadowman" :
            Value = b'\x79'
        Pointer = 0x8563B #Sets value from if statements to have game check which boss is affected by Time Stopper
        Seek = ROM.seek(Pointer,0)
        ROM.write(Value)
                

#Rush item writing section
#Intializes default values to FF
    Pointer = 0x66507  #!
    Seek = ROM.seek(Pointer,0)
    ROM.write(b'\xFF')
    Pointer = 0x66511
    Seek = ROM.seek(Pointer,0)
    ROM.write(b'\xFF')

    if MM2 == True:
        Pointer = 0x664DD 
        Seek = ROM.seek(Pointer,0)
        ROM.write(b'\xFF')
        Pointer = 0x664E1
        Seek = ROM.seek(Pointer,0)
        ROM.write(b'\xFF')
        Pointer = 0x664E7
        Seek = ROM.seek(Pointer,0)
        ROM.write(b'\xFF')

    Pointer = 0x85805 #!Gets random value from address
    Seek = ROM.seek(Pointer,0)
    RushMarine = (ROM.read(1)) #Boss to give Rush Marine
    Pointer+=1
    RushJet = (ROM.read(1)) #Boss to give Rush Jet
    Pointer = 0x8580D #!Gets random value from address
    Seek = ROM.seek(Pointer,0)
    Item3 = (ROM.read(1))
    GiveMarine = int.from_bytes(RushMarine, "big")#Changes byte object to int and grabs boss from pos list based on byte
    GiveJet = int.from_bytes(RushJet, "big")
    GiveI3 = int.from_bytes(Item3, "big")
    GiveMarine -= 1 #Offset to change 1-8 from randomizer to 0-7 for pos
    GiveJet -= 1
    GiveI3 -= 1
    MarineFlag = []
    JetFlag = []
    I3Flag = []
    Check = ["Cutman", "Gutsman", "Bombman", "Iceman", "Fireman", "Elecman"]
    GetMarine = pos[GiveMarine][0] 
    GetJet = pos[GiveJet][0]
    GetI3 = pos[GiveI3][0]
    
    if MM2 == True:
        GetI3 = pos[GiveI3][0]
    
    if GetMarine == "Cutman": #If MM1 is a stage for GiveMarine, find another stage instead.
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    GetMarine = pos[x][0]
                    GiveMarine = x
                    Retry = False
				
    elif GetMarine == "Gutsman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    GetMarine = pos[x][0]
                    GiveMarine = x
                    Retry = False
			
    elif GetMarine == "Iceman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    GetMarine = pos[x][0]
                    GiveMarine = x
                    Retry = False
			
    elif GetMarine == "Bombman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    GetMarine = pos[x][0]
                    GiveMarine = x
                    Retry = False
			
    elif GetMarine == "Fireman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    GetMarine = pos[x][0]
                    GiveMarine = x
                    Retry = False
			
    elif GetMarine == "Elecman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    GetMarine = pos[x][0]
                    GiveMarine = x
                    Retry = False

    if GetMarine == "Flashman": #If boss was X, sets address pointer to the address that will give them an item
        Pointer = 0x664E7
        MarineFlag.append(["Flashman", GiveMarine]) #Flag to reference later who got Marine or Jet
    elif GetMarine == "Bubbleman":
        Pointer = 0x664DB
        MarineFlag.append(["Bubbleman", GiveMarine])
    elif GetMarine == "Airman":
        Pointer = 0x664DD
        MarineFlag.append(["Airman", GiveMarine])
    elif GetMarine == "Quickman":
        Pointer = 0x664DF
        MarineFlag.append(["Quickman", GiveMarine])
    elif GetMarine == "Heatman":
        Pointer = 0x664E1
        MarineFlag.append(["Heatman", GiveMarine])
    elif GetMarine == "Woodman":
        Pointer = 0x664E3
        MarineFlag.append(["Woodman", GiveMarine])
    elif GetMarine == "Metalman":
        Pointer = 0x664E5
        MarineFlag.append(["Metalman", GiveMarine])
    elif GetMarine == "Crashman":
        Pointer = 0x664E9
        MarineFlag.append(["Crashman", GiveMarine])
    elif GetMarine == "Sparkman":
        Pointer = 0x66503
        MarineFlag.append(["Sparkman", GiveMarine])
    elif GetMarine == "Snakeman":
        Pointer = 0x66505
        MarineFlag.append(["Snakeman", GiveMarine])
    elif GetMarine == "Needleman":
        Pointer = 0x66507
        MarineFlag.append(["Needleman", GiveMarine])
    elif GetMarine == "Hardman":
         Pointer = 0x66509
         MarineFlag.append(["Hardman", GiveMarine])
    elif GetMarine == "Topman":
        Pointer = 0x6650B
        MarineFlag.append(["Topman", GiveMarine])
    elif GetMarine == "Geminiman":
        Pointer = 0x6650D
        MarineFlag.append(["Geminiman", GiveMarine])
    elif GetMarine == "Magnetman":
        Pointer = 0x6650F
        MarineFlag.append(["Magnetman", GiveMarine])
    elif GetMarine == "Shadowman" :
        Pointer = 0x66511
        MarineFlag.append(["Shadowman", GiveMarine])
    Seek = ROM.seek(Pointer,0)
    Value = b'\x1D' #Writes Rush Marine value at address specified above
    if MM2 == True:
        Value = b'\x11'
    ROM.write(Value)

#Writes RushJet value to randomly chosen boss
    
    if GetJet == "Cutman": #!Checks to see if MM1 stage is GetJet. Then chooses a non GetMarine value.
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    if GiveMarine != x:
                        GetJet = pos[x][0]
                        GiveJet = x
                        Retry = False

    elif GetJet == "Gutsman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    if GiveMarine != x:
                        GetJet = pos[x][0]
                        GiveJet = x
                        Retry = False
			    
    elif GetJet == "Iceman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    if GiveMarine != x:
                        GetJet = pos[x][0]
                        GiveJet = x
                        Retry = False
			    
    elif GetJet == "Bombman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    if GiveMarine != x:
                        GetJet = pos[x][0]
                        GiveJet = x
                        Retry = False
			    
    elif GetJet == "Fireman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    if GiveMarine != x:
                        GetJet = pos[x][0]
                        GiveJet = x
                        Retry = False
			    
    elif GetJet == "Elecman":
        Retry = True
        for x in range(8):
            Value = 0
            if Retry == False:
                break
            for y in range(6):
                if pos[x][0] != Check[y]:
                    Value += 1
                if Value >= 6:
                    if GiveMarine != x:
                        GetJet = pos[x][0]
                        GiveJet = x
                        Retry = False
        
    if GetJet == "Flashman":
        Pointer = 0x664E7
        JetFlag.append(["Flashman", GiveJet])
    elif GetJet == "Bubbleman":
        Pointer = 0x664DB
        JetFlag.append(["Bubbleman", GiveJet])
    elif GetJet == "Airman":
        Pointer = 0x664DD
        JetFlag.append(["Airman", GiveJet])
    elif GetJet == "Quickman":
        Pointer = 0x664DF
        JetFlag.append(["Quickman", GiveJet])
    elif GetJet == "Heatman":
        Pointer = 0x664E1
        JetFlag.append(["Heatman", GiveJet])
    elif GetJet == "Woodman":
        Pointer = 0x664E3
        JetFlag.append(["Woodman", GiveJet])
    elif GetJet == "Metalman":
        Pointer = 0x664E5
        JetFlag.append(["Metalman", GiveJet])
    elif GetJet == "Crashman":
        Pointer = 0x664E9
        JetFlag.append(["Crashman", GiveJet])
    elif GetJet == "Sparkman":
        Pointer = 0x66503
        JetFlag.append(["Sparkman", GiveJet])
    elif GetJet == "Snakeman":
        Pointer = 0x66505
        JetFlag.append(["Snakeman", GiveJet])
    elif GetJet == "Needleman":
        Pointer = 0x66507
        JetFlag.append(["Needleman", GiveJet])
    elif GetJet == "Hardman":
         Pointer = 0x66509
         JetFlag.append(["Hardman", GiveJet])
    elif GetJet == "Topman":
        Pointer = 0x6650B
        JetFlag.append(["Topman", GiveJet])
    elif GetJet == "Geminiman":
        Pointer = 0x6650D
        JetFlag.append(["Geminiman", GiveJet])
    elif GetJet == "Magnetman":
        Pointer = 0x6650F
        JetFlag.append(["Magnetman", GiveJet])
    elif GetJet == "Shadowman" :
        Pointer = 0x66511
        JetFlag.append(["Shadowman", GiveJet])
    Seek = ROM.seek(Pointer,0)
    Value = b'\x1E' #Same thing here for Rush Jet
    if MM2 == True:
        Value = b'\x12'
    ROM.write(Value)
    
    if MM2 == True: #!
        if GetI3 == "Cutman": #If MM1 is a stage for GiveItem3, find another stage instead.
            Retry = True
            for x in range(8):
                Value = 0
                if Retry == False:
                    break
                for y in range(6):
                    if pos[x][0] != Check[y]:
                        Value += 1
                    if Value >= 6:
                        if GiveMarine != x:
                            if GiveJet != x:
                                GetI3 = pos[x][0]
                                GiveI3 = x
                                Retry = False
                            else:
                                Retry = True
                        else:
                            Retry = True
                                    
        elif GetI3 == "Gutsman":
            Retry = True
            for x in range(8):
                Value = 0
                if Retry == False:
                    break
                for y in range(6):
                    if pos[x][0] != Check[y]:
                        Value += 1
                    if Value >= 6:
                        if GiveMarine != x:
                            if GiveJet != x:
                                GetI3 = pos[x][0]
                                GiveI3 = x
                                Retry = False
                            else:
                                Retry = True
                        else:
                            Retry = True
                            
        elif GetI3 == "Iceman":
            Retry = True
            for x in range(8):
                Value = 0
                if Retry == False:
                    break
                for y in range(6):
                    if pos[x][0] != Check[y]:
                        Value += 1
                    if Value >= 6:
                        if GiveMarine != x:
                            if GiveJet != x:
                                GetI3 = pos[x][0]
                                GiveI3 = x
                                Retry = False
                            else:
                                Retry = True
                        else:
                            Retry = True
                            
        elif GetI3 == "Bombman":
            Retry = True
            for x in range(8):
                Value = 0
                if Retry == False:
                    break
                for y in range(6):
                    if pos[x][0] != Check[y]:
                        Value += 1
                    if Value >= 6:
                        if GiveMarine != x:
                            if GiveJet != x:
                                GetI3 = pos[x][0]
                                GiveI3 = x
                                Retry = False
                            else:
                                Retry = True
                        else:
                            Retry = True
                            
        elif GetI3 == "Fireman":
            Retry = True
            for x in range(8):
                Value = 0
                if Retry == False:
                    break
                for y in range(6):
                    if pos[x][0] != Check[y]:
                        Value += 1
                    if Value >= 6:
                        if GiveMarine != x:
                            if GiveJet != x:
                                GetI3 = pos[x][0]
                                GiveI3 = x
                                Retry = False
                            else:
                                Retry = True
                        else:
                            Retry = True
                            
        elif GetI3 == "Elecman":
            Retry = True
            for x in range(8):
                Value = 0
                if Retry == False:
                    break
                for y in range(6):
                    if pos[x][0] != Check[y]:
                        Value += 1
                    if Value >= 6:
                        if GiveMarine != x:
                            if GiveJet != x:
                                GetI3 = pos[x][0]
                                GiveI3 = x
                                Retry = False
                            else:
                                Retry = True
                        else:
                            Retry = True
        
        if GetI3 == "Flashman": #If boss was X, sets address pointer to the address that will give them an item
            Pointer = 0x664E7
            I3Flag.append(["Flashman", GiveI3]) #Flag to reference later who got Item 3
        elif GetI3 == "Bubbleman":
            Pointer = 0x664DB
            I3Flag.append(["Bubbleman", GiveI3])
        elif GetI3 == "Airman":
            Pointer = 0x664DD
            I3Flag.append(["Airman", GiveI3])
        elif GetI3 == "Quickman":
            Pointer = 0x664DF
            I3Flag.append(["Quickman", GiveI3])
        elif GetI3 == "Heatman":
            Pointer = 0x664E1
            I3Flag.append(["Heatman", GiveI3])
        elif GetI3 == "Woodman":
            Pointer = 0x664E3
            I3Flag.append(["Woodman", GiveI3])
        elif GetI3 == "Metalman":
            Pointer = 0x664E5
            I3Flag.append(["Metalman", GiveI3])
        elif GetI3 == "Crashman":
            Pointer = 0x664E9
            I3Flag.append(["Crashman", GiveI3])
        elif GetI3 == "Sparkman":
            Pointer = 0x66503
            I3Flag.append(["Sparkman", GiveI3])
        elif GetI3 == "Snakeman":
            Pointer = 0x66505
            I3Flag.append(["Snakeman", GiveI3])
        elif GetI3 == "Needleman":
            Pointer = 0x66507
            I3Flag.append(["Needleman", GiveI3])
        elif GetI3 == "Hardman":
             Pointer = 0x66509
             I3Flag.append(["Hardman", GiveI3])
        elif GetI3 == "Topman":
            Pointer = 0x6650B
            I3Flag.append(["Topman", GiveI3])
        elif GetI3 == "Geminiman":
            Pointer = 0x6650D
            I3Flag.append(["Geminiman", GiveI3])
        elif GetI3 == "Magnetman":
            Pointer = 0x6650F
            I3Flag.append(["Magnetman", GiveI3])
        elif GetI3 == "Shadowman" :
            Pointer = 0x66511
            I3Flag.append(["Shadowman", GiveI3])
        Seek = ROM.seek(Pointer,0)
        Value = b'\x13' #Writes Item 3 value at address specified above
        ROM.write(Value)


#!Doc Bot duo byte writing section
    Pointer = [0x7B7F3,0x7B8DF,0x7BA41,0x7BC11,0x7BDF9,0x7BF1B,0x7C0DB,0x7C1C7] #Doc Robot Programming addresses
    Pointer2 = [0x7B7FB,0x7B8E7,0x7BA49,0x7BC19,0x7BE01,0x7BF23,0x7C0D3,0x7C1CF] #Doc Robot Boss Addresses
    DocRobots = []
    DocHeat = b'\xA7' #What values to look for when determining duo byte
    DocMetal = b'|'
    DocQuick = b'\xA8'
    DocAir = b'\xA9'
    DocCrash = b'\xAA'
    DocFlash = b'\xAB'
    DocWood = b'\xAD'
    DocBubble = b'\xAC'
    DocRobots2 = [b'|',b'\xA7',b'\xA8',b'\xA9',b'\xAA',b'\xAB',b'\xAC',b'\xAD']
    Docs0 = []
    Docs2 = []
    DocRobots0 = []
    First = [b'|',b'\xA9',b'\xAB',b'\xAD']
    Morethan2 = False
    for x in range(8):
        Seek = ROM.seek(Pointer[x],0) #Grab randomized values from addresses
        Byte =(ROM.read(1))
        DocRobots0.append(Byte)

    Error = False
    for x in range(8):
        Value = DocRobots0.count(DocRobots2[x])
        if Value == 0:
            Error = True
            Docs0.append(DocRobots2[x])
        elif Value >= 2:
            Error = True
            Docs2.append(DocRobots2[x])
            if Value > 2:
                Docs2.append(DocRobots2[x])
                Morethan2 = True


    if Error == True:
        Value = len(Docs0)
        for x in range(Value):
            Group1 = False
            Group2 = False
            Notfound = Docs0.pop()
            Multiple = Docs2.pop()
            Index = DocRobots0.index(Multiple)
            for y in range(4):
                if Notfound == First[y]:
                    Group1 = True
                    break
            if Group1 == False:
                Group2 = True
            if Group1 == True:
                if Index % 2 != 0:
                    Index += 1
                    Index2 = DocRobots0.index(Multiple, Index)
                    if Morethan2 == False:
                        Index = Index2
                    elif Morethan2 == True:
                        if Index2 % 2 != 0:
                            Index2 += 1
                            Index = DocRobots0.index(Multiple, Index2)
      
            elif Group2 == True:
                if Index % 2 != 1:
                    Index += 1
                    Index2 = DocRobots0.index(Multiple, Index)
                    if Morethan2 == False:
                        Index = Index2
                    elif Morethan2 == True:
                        if Index2 % 2 != 1:
                            Index2 += 1
                            Index = DocRobots0.index(Multiple, Index2)
                            
            DocRobots0.pop(Index)
            DocRobots0.insert(Index, Notfound)
            Pointer3 = Pointer[Index]
            Seek = ROM.seek(Pointer3, 0)
            ROM.write(Notfound)

    for x in range(8):
        DocRobots.append([DocRobots0[x], x])

        
    for x in range(8):
        if DocRobots[x][0] == DocHeat: #If value from DocRobots matches values, writes duo byte at that address from Pointer2
            Value = DocRobots[x][1]
            Pointer3 = Pointer2[Value]
            Seek = ROM.seek(Pointer3,0)
            ROM.write(b'\x48')
        elif DocRobots[x][0] == DocMetal:
            Value = DocRobots[x][1]
            Pointer3 = Pointer2[Value]
            Seek = ROM.seek(Pointer3,0)
            ROM.write(b'\x43')
        elif DocRobots[x][0] == DocQuick:
            Value = DocRobots[x][1]
            Pointer3 = Pointer2[Value]
            Seek = ROM.seek(Pointer3,0)
            ROM.write(b'\x46')
        elif DocRobots[x][0] == DocAir:
            Value = DocRobots[x][1]
            Pointer3 = Pointer2[Value]
            Seek = ROM.seek(Pointer3,0)
            ROM.write(b'\x41')
        elif DocRobots[x][0] == DocCrash:
            Value = DocRobots[x][1]
            Pointer3 = Pointer2[Value]
            Seek = ROM.seek(Pointer3,0)
            ROM.write(b'\x42')
        elif DocRobots[x][0] == DocFlash:
            Value = DocRobots[x][1]
            Pointer3 = Pointer2[Value]
            Seek = ROM.seek(Pointer3,0)
            ROM.write(b'\x45')
        elif DocRobots[x][0] == DocWood:
            Value = DocRobots[x][1]
            Pointer3 = Pointer2[Value]
            Seek = ROM.seek(Pointer3,0)
            ROM.write(b'\x44')
        elif DocRobots[x][0] == DocBubble:
            Value = DocRobots[x][1]
            Pointer3 = Pointer2[Value]
            Seek = ROM.seek(Pointer3,0)
            ROM.write(b'\x47')
    
#!Wily Refight Capsule boss writing section
    Pointer=[0x859B0,0x859B1,0x859B2,0x859B3,0x859B4,0x859B5,0x859B6,0x859B7] #Wily4 random capsule bosses values
    Capsuleorder = []
    Bossorder = []
    Bossvalue = []
    first = False
    second = False
    FlatSp4Arena = False
    FlatSn4Arena = False
    Adjust = False
    Pointer2=[0x7C88D,0x7C89F,0x7C8D5,0x7C8E7]
    Ypos = [b'\xC4',b'\xB4',b'\xB4',b'\xB5']
    y = 9
    y2 = 9
    Order0 = []
    Order2 = []
    for x in range(8):
        Seek = ROM.seek(Pointer[x],0)
        Value = ROM.read(1)
        Boss = int.from_bytes(Value, "big") #Grabs randomized values and converts them to int, appends to Capsuleorder
        Boss -= 1
        Capsuleorder.append(Boss)

    Error = False
    for x in range(8):
        Value = Capsuleorder.count(x)
        if Value == 0:
            Error = True
            Order0.append(x)
        elif Value >= 2:
            Error = True
            Order2.append(x)
            if Value > 2:
                Order2.append(x)
    
    if Error == True:
        Value = len(Order0)
        for x in range(Value):
            Notfound = Order0.pop()
            Multiple = Order2.pop()
            Index = Capsuleorder.index(Multiple)
            Capsuleorder.pop(Index)
            Capsuleorder.insert(Index, Notfound)

        
    if randomboss == False:
        for x in range(8):
            Value=Capsuleorder.pop() #Finds boss based on randomized value and appends them to Bossorder
            if Value == pos[0][1]:
                Bossorder.append(pos[0][0])
            elif Value == pos[1][1]:
                Bossorder.append(pos[1][0])
            elif Value == pos[2][1]:
                Bossorder.append(pos[2][0])
            elif Value == pos[3][1]:
                Bossorder.append(pos[3][0])
            elif Value == pos[4][1]:
                Bossorder.append(pos[4][0])
            elif Value == pos[5][1]:
                Bossorder.append(pos[5][0])
            elif Value == pos[6][1]:
                Bossorder.append(pos[6][0])
            elif Value == pos[7][1]:
                Bossorder.append(pos[7][0])
    elif randomboss == True:
        for x in range(8):
            Value=Capsuleorder.pop() #Finds boss based on randomized value and appends them to Bossorder
            if Value == posB[0][1]:
                Bossorder.append(posB[0][0])
            elif Value == posB[1][1]:
                Bossorder.append(posB[1][0])
            elif Value == posB[2][1]:
                Bossorder.append(posB[2][0])
            elif Value == posB[3][1]:
                Bossorder.append(posB[3][0])
            elif Value == posB[4][1]:
                Bossorder.append(posB[4][0])
            elif Value == posB[5][1]:
                Bossorder.append(posB[5][0])
            elif Value == posB[6][1]:
                Bossorder.append(posB[6][0])
            elif Value == posB[7][1]:
                Bossorder.append(posB[7][0])
    Bossorder.reverse() #Reverses boss order to be correct
    for x in range(8):
        if Bossorder[x] == "Flashman": #Appends byte to Bossvalue based on boss
            Value = b'\x45'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Cutman":
            Value = b'\x18'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Gutsman":
            Value = b'\x19'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Iceman":
            Value = b'\x14'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Bombman":
            Value = b'\x15'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Fireman":
            Value = b'\x16'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Elecman":
            Value = b'\x17'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Bubbleman":
            Value = b'\x47'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Airman":
            Value = b'\x41'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Quickman":
            Value = b'\x46'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Heatman":
            Value = b'\x48'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Woodman":
            Value = b'\x44'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Metalman":
            Value = b'\x43'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Crashman":
            Value = b'\x42'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Sparkman":
            Value = b'\x78'
            first = True
            y = x
            Bossvalue.append(Value)
        elif Bossorder[x] == "Snakeman":
            Value = b'\x76'
            second = True
            y2 = x
            Bossvalue.append(Value)
        elif Bossorder[x] == "Needleman":
            Value = b'\x7A'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Hardman":
            Value = b'\x74'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Topman":
            Value = b'\x75'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Geminiman":
            Value = b'\x7B'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Magnetman":
            Value = b'\x77'
            Bossvalue.append(Value)
        elif Bossorder[x] == "Shadowman" :
            Value = b'\x79'
            Bossvalue.append(Value)
            
    if MM3 == True:        
        if first == True: #If Sparkman is a boss, makes him have his capsule
            Value = Bossvalue.pop(y)
            Bossvalue.insert(0, Value)
            
    if MM3 == True:    
        if second == True: #If Snakeman is a boss, makes him have his capsule
            Value = Bossvalue.pop(y2)
            Bossvalue.insert(1, Value)
        
    Pointer = 0x7C869
    if MM2 == True:
        Pointer = 0x7A463
    Value = b'\x14'
    ValueC = b'\x18'
    ValueG = b'\x19'
    ValueB = b'\x15'
    ValueF = b'\x16'
    ValueE = b'\x17'
    ValueL = b'\xB4'
    for x in range(8): #Writes bossvalue to ROM address
        Seek = ROM.seek(Pointer,0)
        ROM.write(Bossvalue[x])
        if MM3 == True:
            if Bossvalue[x] == Value:
                Pointer += 2
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\xC5')
                Pointer -= 2
            Pointer+=18
        elif MM2 == True:
            Lower = False #Checks to see if Value is MM1 Boss. If so, lowers them to the floor
            if Bossvalue[x] == ValueC:
                Lower = True
            elif Bossvalue[x] == Value:
                Lower = True
            elif Bossvalue[x] == ValueG:
                Lower = True
            elif Bossvalue[x] == ValueB:
                Lower = True
            elif Bossvalue[x] == ValueF:
                Lower = True
            elif Bossvalue[x] == ValueE:
                Lower = True
            if Lower == True:
                Pointer += 2
                Seek = ROM.seek(Pointer,0)
                ROM.write(ValueL)
                Pointer += 16
            if Lower == False:    
                Pointer+=18

    if MM3 == True: #!
        Pointer = 0x7C869
        Seek = ROM.seek(Pointer, 0)
        Value = ROM.read(1)
        if Value == Icemanboss:
            FlatSp4Arena = True
        elif Value == Bombmanboss:
            FlatSp4Arena = True
        elif Value == Firemanboss:
            FlatSp4Arena = True
        elif Value == Elecmanboss:
            FlatSp4Arena = True
        elif Value == Crashmanboss:
            FlatSp4Arena = True
        elif Value == Woodmanboss:
            FlatSp4Arena = True
        elif Value == Metalmanboss:
            FlatSp4Arena = True
        elif Value == Bubblemanboss:
            FlatSp4Arena = True
        elif Value == Heatmanboss:
            FlatSp4Arena = True
        elif Value == Hardmanboss:
            FlatSp4Arena = True
        elif Value == Topmanboss:
            FlatSp4Arena = True
        elif Value == Magnetmanboss:
            FlatSp4Arena = True
        elif Value == Needlemanboss:
            FlatSp4Arena = True
        elif Value == Geminimanboss:
            FlatSp4Arena = True

        if FlatSp4Arena == True:
            Pointer = 0x16D85C
            Seek = ROM.seek(Pointer, 0)
            ROM.write(b'\xE3')
            Pointer += 1
            Seek = ROM.seek(Pointer, 0)
            ROM.write(b'\xBA')
            Pointer = 0x7C863
            Seek = ROM.seek(Pointer, 0)
            ROM.write(b'\xB0')

        Pointer = 0x7C87B
        Seek = ROM.seek(Pointer, 0)
        Value = ROM.read(1)
        if Value == Icemanboss:
            FlatSn4Arena = True
        elif Value == Flashmanboss:
            FlatSn4Arena = True
        elif Value == Firemanboss:
            FlatSn4Arena = True
        elif Value == Elecmanboss:
            FlatSn4Arena = True
        elif Value == Crashmanboss:
            FlatSn4Arena = True
        elif Value == Woodmanboss:
            FlatSn4Arena = True
        elif Value == Bubblemanboss:
            FlatSn4Arena = True
        elif Value == Heatmanboss:
            FlatSn4Arena = True
        elif Value == Hardmanboss:
            FlatSn4Arena = True
        elif Value == Topmanboss:
            FlatSn4Arena = True
        elif Value == Magnetmanboss:
            FlatSn4Arena = True
        elif Value == Needlemanboss:
            FlatSn4Arena = True
        elif Value == Geminimanboss:
            FlatSn4Arena = True

        if FlatSn4Arena == True: # Adjust teleporter sprite to be reachable
            Pointer = 0x16D860
            Seek = ROM.seek(Pointer, 0)
            ROM.write(b'\xE3')
            Pointer += 1
            Seek = ROM.seek(Pointer, 0)
            ROM.write(b'\xBA')

        for x in range(4): #!If MM1 boss is in Shadow,Hard, Needle, or Magnet capsules, adjust vertical positioning
            Pointer = Pointer2[x]
            Seek = ROM.seek(Pointer, 0)
            Value = ROM.read(1)
            if Value == b'\x14':
                 Adjust = True
            elif Value == b'\x15':
                Adjust = True
            elif Value == b'\x16':
                Adjust = True
            elif Value == b'\x17':
                Adjust = True
            elif Value == b'\x18':
                Adjust = True
            elif Value == b'\x19':
                Adjust = True
            if Adjust == True:
                Pointer += 2
                Seek = ROM.seek(Pointer, 0)
                ROM.write(Ypos[x])
        

#!You got weapon text writing for MM3
    Pointer = 0x6482A
    Yougottext = [b'\x00',b'\x00',b'\x59',b'\x4F',b'\x55',b'\x20',b'\x47',b'\x4F',b'\x54',b'\x0A']
    RushMarinetext = [b'\x0A',b'\x41',b'\x4E',b'\x44',b'\x0A',b'\x52',b'\x55',b'\x53',b'\x48',b'\x20',b'\x4D',b'\x41',b'\x52',b'\x49',b'\x4E',b'\x45']
    RushJettext = [b'\x0A',b'\x41',b'\x4E',b'\x44',b'\x0A',b'\x52',b'\x55',b'\x53',b'\x48',b'\x20',b'\x4A',b'\x45',b'\x54']
    RollingCutterReceived = [b'\x52',b'\x4F',b'\x4C',b'\x4C',b'\x49',b'\x4E',b'\x47',b'\x20',b'\x43',b'\x55',b'\x54',b'\x54',b'\x45',b'\x52']
    ThunderBeamReceived = [b'\x54',b'\x48',b'\x55',b'\x4E',b'\x44',b'\x45',b'\x52',b'\x20',b'\x42',b'\x45',b'\x41',b'\x4D']
    HyperBombReceived = [b'\x48',b'\x59',b'\x50',b'\x45',b'\x52',b'\x20',b'\x42',b'\x4F',b'\x4D',b'\x42']
    IceSlasherReceived = [b'\x49',b'\x43',b'\x45',b'\x20',b'\x53',b'\x4C',b'\x41',b'\x53',b'\x48',b'\x45',b'\x52']
    FireStormReceived = [b'\x46',b'\x49',b'\x52',b'\x45',b'\x20',b'\x53',b'\x54',b'\x4F',b'\x52',b'\x4D']
    SuperArmReceived = [b'\x53',b'\x55',b'\x50',b'\x45',b'\x52',b'\x20',b'\x41',b'\x52',b'\x4D']

    AtomicFireReceived = [b'\x41',b'\x54',b'\x4F',b'\x4D',b'\x49',b'\x43',b'\x20',b'\x46',b'\x49',b'\x52',b'\x45']
    AirShooterReceived = [b'\x41',b'\x49',b'\x52',b'\x20',b'\x53',b'\x48',b'\x4F',b'\x4F',b'\x54',b'\x45',b'\x52']
    LeafShieldReceived = [b'\x4C',b'\x45',b'\x41',b'\x46',b'\x20',b'\x53',b'\x48',b'\x49',b'\x45',b'\x4C',b'\x44']
    BubbleLeadReceived = [b'\x42',b'\x55',b'\x42',b'\x42',b'\x4C',b'\x45',b'\x20',b'\x4C',b'\x45',b'\x41',b'\x44']
    QuickBoomerangReceived = [b'\x51',b'\x55',b'\x49',b'\x43',b'\x4B',b'\x20',b'\x42',b'\x4F',b'\x4F',b'\x4D',b'\x45',b'\x52',b'\x41',b'\x4E',b'\x47']
    TimeStopperReceived = [b'\x54',b'\x49',b'\x4D',b'\x45',b'\x20',b'\x53',b'\x54',b'\x4F',b'\x50',b'\x50',b'\x45',b'\x52']
    MetalBladeReceived = [b'\x4D',b'\x45',b'\x54',b'\x41',b'\x4C',b'\x20',b'\x42',b'\x4C',b'\x41',b'\x44',b'\x45']
    CrashBomberReceived = [b'\x43',b'\x52',b'\x41',b'\x53',b'\x48',b'\x20',b'\x42',b'\x4F',b'\x4D',b'\x42',b'\x45',b'\x52']

    SparkShotReceived = [b'\x53',b'\x50',b'\x41',b'\x52',b'\x4B',b'\x20',b'\x53',b'\x48',b'\x4F',b'\x43',b'\x4B']
    SearchSnakeReceived = [b'\x53',b'\x45',b'\x41',b'\x52',b'\x43',b'\x48',b'\x20',b'\x53',b'\x4E',b'\x41',b'\x4B',b'\x45']
    NeedleCannonReceived = [b'\x4E',b'\x45',b'\x45',b'\x44',b'\x4C',b'\x45',b'\x20',b'\x43',b'\x41',b'\x4E',b'\x4E',b'\x4F',b'\x4E']
    HardKnuckleReceived = [b'\x48',b'\x41',b'\x52',b'\x44',b'\x20',b'\x4B',b'\x4E',b'\x55',b'\x43',b'\x4B',b'\x4C',b'\x45']
    TopSpinReceived = [b'\x54',b'\x4F',b'\x50',b'\x20',b'\x53',b'\x50',b'\x49',b'\x4E']
    GeminiLaserReceived = [b'\x47',b'\x45',b'\x4D',b'\x49',b'\x4E',b'\x49',b'\x20',b'\x4C',b'\x41',b'\x53',b'\x45',b'\x52']
    MagnetMissileReceived = [b'\x4D',b'\x41',b'\x47',b'\x4E',b'\x45',b'\x54',b'\x20',b'\x4D',b'\x49',b'\x53',b'\x53',b'\x49',b'\x4C',b'\x45']
    ShadowBladeReceived = [b'\x53',b'\x48',b'\x41',b'\x44',b'\x4F',b'\x57',b'\x20',b'\x42',b'\x4C',b'\x41',b'\x44',b'\x45']
    End = []
    if MM3 == True:
        if Vanilla == True:
            for y in range(8):
                if pos[y][0] == "Airman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)): #Writes first part
                        ROM.write(Yougottext[x])
                        Pointer+=1
                    for x in range(len(AirShooterReceived)):#Writes second part
                        ROM.write(AirShooterReceived[x])
                        Pointer+=1
                    if MarineFlag[0][0] == "Airman":
                        for x in range(len(RushMarinetext)): #If they are supposed to give Marine or Jet, write text
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Airman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer) #Used to recalculate offsets for text
                elif pos[y][0] == "Crashman": #Repeat 21 more times for each boss
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(CrashBomberReceived)):
                            ROM.write(CrashBomberReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Crashman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Crashman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Bubbleman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(BubbleLeadReceived)):
                            ROM.write(BubbleLeadReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Bubbleman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Bubbleman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Quickman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(QuickBoomerangReceived)):
                            ROM.write(QuickBoomerangReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Quickman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Quickman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Heatman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(AtomicFireReceived)):
                            ROM.write(AtomicFireReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Heatman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Heatman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Woodman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(LeafShieldReceived)):
                            ROM.write(LeafShieldReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Woodman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Woodman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Metalman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(MetalBladeReceived)):
                            ROM.write(MetalBladeReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Metalman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Metalman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Flashman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(TimeStopperReceived)):
                            ROM.write(TimeStopperReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Flashman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Flashman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Cutman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(RollingCutterReceived)):
                            ROM.write(RollingCutterReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Cutman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Cutman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Gutsman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(SuperArmReceived)):
                            ROM.write(SuperArmReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Gutsman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Gutsman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Iceman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(IceSlasherReceived)):
                            ROM.write(IceSlasherReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Iceman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Iceman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Bombman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(HyperBombReceived)):
                            ROM.write(HyperBombReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Bombman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Bombman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Fireman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(FireStormReceived)):
                            ROM.write(FireStormReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Fireman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Fireman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Elecman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(ThunderBeamReceived)):
                            ROM.write(ThunderBeamReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Elecman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Elecman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Sparkman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(SparkShotReceived)):
                            ROM.write(SparkShotReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Sparkman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Sparkman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Snakeman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(SearchSnakeReceived)):
                            ROM.write(SearchSnakeReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Snakeman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Snakeman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Needleman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(NeedleCannonReceived)):
                            ROM.write(NeedleCannonReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Needleman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Needleman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Hardman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(HardKnuckleReceived)):
                            ROM.write(HardKnuckleReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Hardman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Hardman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Topman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(TopSpinReceived)):
                            ROM.write(TopSpinReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Topman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Topman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Geminiman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(GeminiLaserReceived)):
                            ROM.write(GeminiLaserReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Geminiman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Geminiman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Magnetman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(MagnetMissileReceived)):
                            ROM.write(MagnetMissileReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Magnetman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Magnetman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif pos[y][0] == "Shadowman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(ShadowBladeReceived)):
                            ROM.write(ShadowBladeReceived[x])
                            Pointer+=1
                    if MarineFlag[0][0] == "Shadowman":
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Shadowman":
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                    
        if randomboss == True: #!
            if randomweapons == False:
                for y in range(8):
                    if posB[y][0] == "Airman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)): #Writes first part
                            ROM.write(Yougottext[x])
                            Pointer+=1
                        for x in range(len(AirShooterReceived)):#Writes second part
                            ROM.write(AirShooterReceived[x])
                            Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)): #If they are supposed to give Marine or Jet, write text
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer) #Used to recalculate offsets for text
                    elif posB[y][0] == "Crashman": #Repeat 21 more times for each boss
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(CrashBomberReceived)):
                                ROM.write(CrashBomberReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Bubbleman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(BubbleLeadReceived)):
                                ROM.write(BubbleLeadReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Quickman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(QuickBoomerangReceived)):
                                ROM.write(QuickBoomerangReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Heatman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(AtomicFireReceived)):
                                ROM.write(AtomicFireReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Woodman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(LeafShieldReceived)):
                                ROM.write(LeafShieldReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Metalman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(MetalBladeReceived)):
                                ROM.write(MetalBladeReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Flashman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(TimeStopperReceived)):
                                ROM.write(TimeStopperReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Cutman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(RollingCutterReceived)):
                                ROM.write(RollingCutterReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Gutsman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(SuperArmReceived)):
                                ROM.write(SuperArmReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Iceman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(IceSlasherReceived)):
                                ROM.write(IceSlasherReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Bombman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(HyperBombReceived)):
                                ROM.write(HyperBombReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Fireman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(FireStormReceived)):
                                ROM.write(FireStormReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Elecman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(ThunderBeamReceived)):
                                ROM.write(ThunderBeamReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Sparkman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(SparkShotReceived)):
                                ROM.write(SparkShotReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Snakeman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(SearchSnakeReceived)):
                                ROM.write(SearchSnakeReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Needleman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(NeedleCannonReceived)):
                                ROM.write(NeedleCannonReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Hardman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(HardKnuckleReceived)):
                                ROM.write(HardKnuckleReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Topman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(TopSpinReceived)):
                                ROM.write(TopSpinReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Geminiman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(GeminiLaserReceived)):
                                ROM.write(GeminiLaserReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Magnetman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(MagnetMissileReceived)):
                                ROM.write(MagnetMissileReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)
                    elif posB[y][0] == "Shadowman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(len(Yougottext)):
                                ROM.write(Yougottext[x])
                                Pointer+=1
                        for x in range(len(ShadowBladeReceived)):
                                ROM.write(ShadowBladeReceived[x])
                                Pointer+=1
                        if y == GiveMarine:
                            for x in range(len(RushMarinetext)):
                                ROM.write(RushMarinetext[x])
                                Pointer+=1
                        elif y == GiveJet:
                            for x in range(len(RushJettext)):
                                ROM.write(RushJettext[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00')
                            Pointer+=1
                            ROM.write(b'\x00')
                        End.append(Pointer)

#!Writes randomly generated weapon values to a list and then writes the You Got Weapon text                
    weapons = []
    Cutbyte = b'\x05'
    Gutsbyte = b'\x03'
    Icebyte = b'\x04'
    Bombbyte = b'\x01'
    Firebyte = b'\x06'
    Elecbyte = b'\x02'

    Bubblebyte = b'\x0b'
    Airbyte = b'\x09'
    Quickbyte = b'\x0c'
    Heatbyte = b'\x08'
    Woodbyte = b'\x0a'
    Metalbyte = b'\x0f'
    Flashbyte = b'\x0e'
    Crashbyte = b'\x10'

    Sparkbyte = b'\x1a'
    Snakebyte = b'\x19'
    Needlebyte = b'\x14'
    Hardbyte = b'\x17'
    Topbyte = b'\x18'
    Geminibyte = b'\x16'
    Magnetbyte = b'\x15'
    Shadowbyte = b'\x1b'
    if randomweapons == True: 
        Pointer = 0x859A0
        Seek = ROM.seek(Pointer,0)
        for x in range(8):
            Byte = (ROM.read(1))#Grabs randomly generated values for weapons
            weapons.append(Byte)
            Pointer += 1
            
        Epos.clear()
        Next.clear()
        Next = [b'\x06',b'\x09',b'\x0B',b'\x1A',b'\x02',b'\x1B',b'\x0A',b'\x19',b'\x16',]
        Error = False
        for x in range(8): # Error checking section for weapons
            Value = weapons[x]
            for y in range(8):
                    if Value == weapons[y]:
                        if x != y:
                            Error = True
                            Epos.append(y)
        if Error == True:
            for x in range(9):
                Value = weapons.count(Next[x])
                if Value == 0:
                    Backup = Next[x]
                    Value2 = x
                    break
            Errors = len(Epos)
            Value = Epos.pop()
            weapons.pop(Value)
            weapons.append(Backup)
            Errors -= 2
            Epos.pop()
            if Errors > 1:
                Errors -= 1
                for x in range(Errors):
                    Value = Epos.pop()
                    Epos.pop()
                    weapons.pop(Value)
                    Value2 += 1
                    Value3 = Next[Value2]
                    Retry = False
                    if Value2 == 9:
                        print("Something went wrong with the logic script when trying to replace duplicate weapons. Please run this script again. If this continues to happen, contact me.")
                        ROM.close()
                        time.sleep(13)  
                    for y in range(7):
                        if weapons[y] == Value3:
                            Retry = True
                            Value2 += 1
                            break
                    if Retry == False:
                        weapons.append(Value3)
                
        if MM3 == True:
            Pointer = 0x6482A
            for y in range(8): #Mostly the same as above, except Rush items
                if weapons[y] == Airbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)): #Writes first part
                        ROM.write(Yougottext[x])
                        Pointer+=1
                    for x in range(len(AirShooterReceived)):#Writes second part
                        ROM.write(AirShooterReceived[x])
                        Pointer+=1
                    if MarineFlag[0][1] == y :
                        for x in range(len(RushMarinetext)): #Based on position of boss defeated rather than boss
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer) #Used to recalculate offsets for text
                elif weapons[y] == Crashbyte: #Repeat 21 more times for each boss
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(CrashBomberReceived)):
                            ROM.write(CrashBomberReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Bubblebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(BubbleLeadReceived)):
                            ROM.write(BubbleLeadReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] ==y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Quickbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(QuickBoomerangReceived)):
                            ROM.write(QuickBoomerangReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Heatbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(AtomicFireReceived)):
                            ROM.write(AtomicFireReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Woodbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(LeafShieldReceived)):
                            ROM.write(LeafShieldReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Metalbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(MetalBladeReceived)):
                            ROM.write(MetalBladeReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Flashbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(TimeStopperReceived)):
                            ROM.write(TimeStopperReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Cutbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(RollingCutterReceived)):
                            ROM.write(RollingCutterReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Gutsbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(SuperArmReceived)):
                            ROM.write(SuperArmReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Icebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(IceSlasherReceived)):
                            ROM.write(IceSlasherReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Bombbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(HyperBombReceived)):
                            ROM.write(HyperBombReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Firebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(FireStormReceived)):
                            ROM.write(FireStormReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Elecbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(ThunderBeamReceived)):
                            ROM.write(ThunderBeamReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Sparkbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(SparkShotReceived)):
                            ROM.write(SparkShotReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Snakebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(SearchSnakeReceived)):
                            ROM.write(SearchSnakeReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Needlebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(NeedleCannonReceived)):
                            ROM.write(NeedleCannonReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Hardbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(HardKnuckleReceived)):
                            ROM.write(HardKnuckleReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Topbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(TopSpinReceived)):
                            ROM.write(TopSpinReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Geminibyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(GeminiLaserReceived)):
                            ROM.write(GeminiLaserReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Magnetbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(MagnetMissileReceived)):
                            ROM.write(MagnetMissileReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)
                elif weapons[y] == Shadowbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(len(Yougottext)):
                            ROM.write(Yougottext[x])
                            Pointer+=1
                    for x in range(len(ShadowBladeReceived)):
                            ROM.write(ShadowBladeReceived[x])
                            Pointer+=1
                    if MarineFlag[0][1] == y:
                        for x in range(len(RushMarinetext)):
                            ROM.write(RushMarinetext[x])
                            Pointer+=1
                    if JetFlag[0][1] == y:
                        for x in range(len(RushJettext)):
                            ROM.write(RushJettext[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00')
                        Pointer+=1
                        ROM.write(b'\x00')
                    End.append(Pointer)

#!Start of MM2 Weapon Text section                
    Pointer = 0x648F3
    GetEquippedtext = [b'\x00',b'\x47',b'\x45',b'\x54',b'\x20',b'\x45',b'\x51',b'\x55',b'\x49',b'\x50',b'\x50',
                       b'\x45',b'\x44',b'\x0A',b'\x57',b'\x49',b'\x54',b'\x48',b'\x20']
    Item1text = [b'\x0A',b'\x41',b'\x4E',b'\x44',b'\x20',b'\x49',b'\x54',b'\x45',b'\x4D',b'\x2D',b'\x31',b'\x0B',b'\x38']
    Item2text = [b'\x0A',b'\x41',b'\x4E',b'\x44',b'\x20',b'\x49',b'\x54',b'\x45',b'\x4D',b'\x2D',b'\x32',b'\x0B',b'\x38']
    Item3text = [b'\x0A',b'\x41',b'\x4E',b'\x44',b'\x20',b'\x49',b'\x54',b'\x45',b'\x4D',b'\x2D',b'\x33',b'\x0B',b'\x38']
    End2 = []
    if MM2 == True:
        if Vanilla == True:
            for y in range(8):
                if pos[y][0] == "Airman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(AirShooterReceived)
                    AirShooterReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 3:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(AirShooterReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Airman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Airman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Airman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Bubbleman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(BubbleLeadReceived)
                    BubbleLeadReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(BubbleLeadReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Bubbleman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Bubbleman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Bubbleman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Quickman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(QuickBoomerangReceived)
                    QuickBoomerangReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(QuickBoomerangReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Quickman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Quickman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Quickman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Heatman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(AtomicFireReceived)
                    AtomicFireReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(AtomicFireReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Heatman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Heatman":
                        ROM.write(b'\x0A')
                        Pointer+=1
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Heatman":
                        ROM.write(b'\x0A')
                        Pointer+=1
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Woodman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(LeafShieldReceived)
                    LeafShieldReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 4:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(LeafShieldReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Woodman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Woodman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Woodman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Metalman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(MetalBladeReceived)
                    MetalBladeReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(MetalBladeReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Metalman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Metalman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Metalman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Flashman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(TimeStopperReceived)
                    TimeStopperReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 4:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(TimeStopperReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Flashman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Flashman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Flashman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Crashman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(CrashBomberReceived)
                    CrashBomberReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(CrashBomberReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Crashman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Crashman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Crashman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Cutman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1
                        
                    z = len(RollingCutterReceived)
                    RollingCutterReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 7:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(RollingCutterReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Cutman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Cutman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Cutman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Gutsman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(SuperArmReceived)
                    SuperArmReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(SuperArmReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Gutsman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Gutsman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Gutsman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Iceman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(IceSlasherReceived)
                    IceSlasherReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 3:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(IceSlasherReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Iceman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Iceman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Iceman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Bombman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(HyperBombReceived)
                    HyperBombReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(HyperBombReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Bombman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Bombman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Bombman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Fireman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(FireStormReceived)
                    FireStormReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 4:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(FireStormReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Fireman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Fireman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Fireman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Elecman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(ThunderBeamReceived)
                    ThunderBeamReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 7:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(ThunderBeamReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Elecman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Elecman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Elecman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Sparkman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(SparkShotReceived)
                    SparkShotReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(SparkShotReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Sparkman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Sparkman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Sparkman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Snakeman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(SearchSnakeReceived)
                    SearchSnakeReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(SearchSnakeReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Snakeman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Snakeman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Snakeman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Needleman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(NeedleCannonReceived)
                    NeedleCannonReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(NeedleCannonReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Needleman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Needleman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Needleman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Hardman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(HardKnuckleReceived)
                    HardKnuckleReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 4:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(HardKnuckleReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Hardman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Hardman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Hardman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Topman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1
                    
                    for x in range(len(TopSpinReceived)):#Writes second part
                        ROM.write(TopSpinReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Topman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Topman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Topman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Geminiman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(GeminiLaserReceived)
                    GeminiLaserReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(GeminiLaserReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Geminiman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Geminiman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Geminiman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Magnetman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(MagnetMissileReceived)
                    MagnetMissileReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(MagnetMissileReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Magnetman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Magnetman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Magnetman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif pos[y][0] == "Shadowman":
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(ShadowBladeReceived)
                    ShadowBladeReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(ShadowBladeReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if MarineFlag[0][0] == "Shadowman":
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if JetFlag[0][0] == "Shadowman":
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if I3Flag[0][0] == "Shadowman":
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
    if randomboss == True: #!
        if randomweapons == False:
                for y in range(8):
                    if posB[y][0] == "Airman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(AirShooterReceived)
                        AirShooterReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 3:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(AirShooterReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Bubbleman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(BubbleLeadReceived)
                        BubbleLeadReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 6:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(BubbleLeadReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Quickman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(QuickBoomerangReceived)
                        QuickBoomerangReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 5:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(QuickBoomerangReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Heatman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(AtomicFireReceived)
                        AtomicFireReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 6:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(AtomicFireReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            ROM.write(b'\x0A')
                            Pointer+=1
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            ROM.write(b'\x0A')
                            Pointer+=1
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Woodman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(LeafShieldReceived)
                        LeafShieldReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 4:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(LeafShieldReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Metalman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(MetalBladeReceived)
                        MetalBladeReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 5:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(MetalBladeReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Flashman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(TimeStopperReceived)
                        TimeStopperReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 4:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(TimeStopperReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Crashman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1
                            
                        z = len(CrashBomberReceived)
                        CrashBomberReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 5:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(CrashBomberReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Cutman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(RollingCutterReceived)
                        RollingCutterReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 7:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(RollingCutterReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Gutsman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(SuperArmReceived)
                        SuperArmReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 5:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(SuperArmReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Iceman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(IceSlasherReceived)
                        IceSlasherReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 3:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(IceSlasherReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Bombman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(HyperBombReceived)
                        HyperBombReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 5:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(HyperBombReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Fireman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(FireStormReceived)
                        FireStormReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 4:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(FireStormReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Elecman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(ThunderBeamReceived)
                        ThunderBeamReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 7:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(ThunderBeamReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == cy:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Sparkman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(SparkShotReceived)
                        SparkShotReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 5:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(SparkShotReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Snakeman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(SearchSnakeReceived)
                        SearchSnakeReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 6:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(SearchSnakeReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Needleman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(NeedleCannonReceived)
                        NeedleCannonReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 6:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(NeedleCannonReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Hardman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(HardKnuckleReceived)
                        HardKnuckleReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 4:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(HardKnuckleReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Topman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1
                        
                        for x in range(len(TopSpinReceived)):#Writes second part
                            ROM.write(TopSpinReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Geminiman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(GeminiLaserReceived)
                        GeminiLaserReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 6:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(GeminiLaserReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Magnetman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(MagnetMissileReceived)
                        MagnetMissileReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 6:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(MagnetMissileReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
                    elif posB[y][0] == "Shadowman":
                        Seek = ROM.seek(Pointer,0)
                        for x in range(19): #Writes first part
                            ROM.write(GetEquippedtext[x])
                            Pointer+=1

                        z = len(ShadowBladeReceived)
                        ShadowBladeReceived.remove(b'\x20')
                        z -= 1
                    
                        for x in range(z):#Writes second part
                            if x == 6:
                                ROM.write(b'\x0A')
                                Pointer+=1
                            ROM.write(ShadowBladeReceived[x])
                            Pointer+=1
                            
                        ROM.write(b'\x0B')
                        Pointer+=1
                        
                        if y == 0: #Checks to see what palette value should be written based on position
                            Value = (b'\x30')
                        elif y == 1:
                            Value = (b'\x31')
                        elif y == 2:
                            Value = (b'\x32')
                        elif y == 3:
                            Value = (b'\x33')
                        elif y == 4:
                            Value = (b'\x34')
                        elif y == 5:
                            Value = (b'\x35')
                        elif y == 6:
                            Value = (b'\x36')
                        elif y == 7:
                            Value = (b'\x37')
                            
                        ROM.write(Value)
                        Pointer+=1
                        if GiveMarine == y:
                            for x in range(13): #If they are supposed to give Item, write text
                                ROM.write(Item1text[x])
                                Pointer+=1
                        if GiveJet == y:
                            for x in range(13):
                                ROM.write(Item2text[x])
                                Pointer+=1
                        if GiveI3 == y:
                            for x in range(13):
                                ROM.write(Item3text[x])
                                Pointer+=1
                        if y == 7:
                            ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                        End2.append(Pointer) #Used to recalculate offsets for text
                        
    if randomweapons == True: #!
            for y in range(8):
                if weapons[y] == Airbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(AirShooterReceived)
                    AirShooterReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 3:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(AirShooterReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Bubblebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(BubbleLeadReceived)
                    BubbleLeadReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(BubbleLeadReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Quickbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(QuickBoomerangReceived)
                    QuickBoomerangReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(QuickBoomerangReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Heatbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(AtomicFireReceived)
                    AtomicFireReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(AtomicFireReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        ROM.write(b'\x0A')
                        Pointer+=1
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        ROM.write(b'\x0A')
                        Pointer+=1
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Woodbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(LeafShieldReceived)
                    LeafShieldReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 4:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(LeafShieldReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Metalbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(MetalBladeReceived)
                    MetalBladeReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(MetalBladeReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Flashbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(TimeStopperReceived)
                    TimeStopperReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 4:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(TimeStopperReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Crashbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(CrashBomberReceived)
                    CrashBomberReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(CrashBomberReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Cutbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(RollingCutterReceived)
                    RollingCutterReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 7:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(RollingCutterReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Gutsbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(SuperArmReceived)
                    SuperArmReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(SuperArmReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Icebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(IceSlasherReceived)
                    IceSlasherReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 3:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(IceSlasherReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Bombbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(HyperBombReceived)
                    HyperBombReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(HyperBombReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Firebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(FireStormReceived)
                    FireStormReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 4:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(FireStormReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Elecbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(ThunderBeamReceived)
                    ThunderBeamReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 7:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(ThunderBeamReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Sparkbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(SparkShotReceived)
                    SparkShotReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 5:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(SparkShotReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Snakebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(SearchSnakeReceived)
                    SearchSnakeReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(SearchSnakeReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Needlebyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(NeedleCannonReceived)
                    NeedleCannonReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(NeedleCannonReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Hardbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(HardKnuckleReceived)
                    HardKnuckleReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 4:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(HardKnuckleReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Topbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1
                    
                    for x in range(len(TopSpinReceived)):#Writes second part
                        ROM.write(TopSpinReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Geminibyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(GeminiLaserReceived)
                    GeminiLaserReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(GeminiLaserReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Magnetbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(MagnetMissileReceived)
                    MagnetMissileReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(MagnetMissileReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
                    
                elif weapons[y] == Shadowbyte:
                    Seek = ROM.seek(Pointer,0)
                    for x in range(19): #Writes first part
                        ROM.write(GetEquippedtext[x])
                        Pointer+=1

                    z = len(ShadowBladeReceived)
                    ShadowBladeReceived.remove(b'\x20')
                    z -= 1
                    
                    for x in range(z):#Writes second part
                        if x == 6:
                            ROM.write(b'\x0A')
                            Pointer+=1
                        ROM.write(ShadowBladeReceived[x])
                        Pointer+=1
                        
                    ROM.write(b'\x0B')
                    Pointer+=1
                    
                    if y == 0: #Checks to see what palette value should be written based on position
                        Value = (b'\x30')
                    elif y == 1:
                        Value = (b'\x31')
                    elif y == 2:
                        Value = (b'\x32')
                    elif y == 3:
                        Value = (b'\x33')
                    elif y == 4:
                        Value = (b'\x34')
                    elif y == 5:
                        Value = (b'\x35')
                    elif y == 6:
                        Value = (b'\x36')
                    elif y == 7:
                        Value = (b'\x37')
                        
                    ROM.write(Value)
                    Pointer+=1
                    if GiveMarine == y:
                        for x in range(13): #If they are supposed to give Item, write text
                            ROM.write(Item1text[x])
                            Pointer+=1
                    if GiveJet == y:
                        for x in range(13):
                            ROM.write(Item2text[x])
                            Pointer+=1
                    if GiveI3 == y:
                        for x in range(13):
                            ROM.write(Item3text[x])
                            Pointer+=1
                    if y == 7:
                        ROM.write(b'\x00') #If this is the last one, write the terminator at the end
                    End2.append(Pointer) #Used to recalculate offsets for text
   
#!Weapon text pointer reclculation section
    for x in range(8):#Add 2 to each pointer to get to next beginning of text
        if MM3 == True:
            End[x] += 2
        elif MM2 == True:
            End2[x] += 1
    for x in range(8):
        Value = 0
        if MM3 == True:
            if Value < End[x]: #Finds the last pointer written, discards it, and adds beginning of offsets to pointer
                Value = End[x]
        elif MM2 == True:
            if Value < End2[x]:
                Value = End2[x]
        if x == 7:
            if MM3 == True:
                End.remove(Value)
                End.append(411692)
            elif MM2 == True:
                End2.remove(Value)
                End2.append(411892)
            
    End3 = []
    Pointers = [0x646AC,0x646AD,0x646B4,0x646B5,0x646BC,0x646BD,0x646C4,0x646C5,
                0x646CC,0x646CD,0x646D4,0x646D5,0x646DC,0x646DD,0x646E4,0x646E5]
    if MM3 == True:
        for x in range(8):
            Value = End.pop() #Changes pointers to Int, then hex value, then binary form with binascii
            int(Value)
            Hex = hex(Value)
            Value2 = (Hex[5:7])
            Value3 = binascii.a2b_hex(Value2)
            End3.append(Value3)
        End3.sort()
        Pointer = 0x646ED
        for x in range(8):
            Seek = ROM.seek(Pointer,0) #Writes the last byte of the offset
            ROM.write(End3[x])
            Pointer += 4 #This code may need to be adjusted if there is an offset at exceeds 648FF

    elif MM2 == True:
        End2.sort(reverse=True)
        for x in range(8):
            Value = End2.pop()
            int(Value)
            Hex = hex(Value)
            Value2a = (Hex[3:5])
            Value2b = (Hex[5:7])
            Value3a = binascii.a2b_hex(Value2a)
            Value3b = binascii.a2b_hex(Value2b)
            End3.append(Value3a)
            End3.append(Value3b)
        for x in range(16):
            Pointer = Pointers[x]
            Seek = ROM.seek(Pointer,0)
            ROM.write(End3[x])
      

#!Get weapon screen and palette writing section if no random weapons
    Value = [b'\x08',b'\x09', b'\x0A', b'\x0B', b'\x0C', b'\x0D', b'\x0E', b'\x0F'] #Values for Get Weapon Screen
    Palette = [[0x6472E,0x6472F,0x64730,0x64731,0x64732,0x64733,0x64734,0x64735,0x64746,0x64747], #Sparkman
               [0x6474E,0x6474F,0x64750,0x64751,0x64752,0x64753,0x64754,0x64755,0x64766,0x64767], #Snakeman
               [0x6476E,0x6476F,0x64770,0x64771,0x64772,0x64773,0x64774,0x64775,0x64786,0x64787], #Needleman
               [0x6478E,0x6478F,0x64790,0x64791,0x64792,0x64793,0x64794,0x64795,0x647A6,0x647A7], #Hardman
               [0x647AE,0x647AF,0x647B0,0x647B1,0x647B2,0x647B3,0x647B4,0x647B5,0x647C6,0x647C7], #Topman
               [0x647CE,0x647CF,0x647D0,0x647D1,0x647D2,0x647D3,0x647D4,0x647D5,0x647E6,0x647E7], #Geminiman
               [0x647EE,0x647EF,0x647F0,0x647F1,0x647F2,0x647F3,0x647F4,0x647F5,0x64806,0x64807], #Magnetman
               [0x6480E,0x6480F,0x64810,0x64811,0x64812,0x64813,0x64814,0x64815,0x64826,0x64827]] #Shadowman
    RollingCutter = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x04',b'\x44',b'\x02',b'\x22',b'\x06',b'\x66'] #Values for Palettes
    IceSlasher = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x06',b'\x00',b'\x05',b'\x00',b'\x08',b'\x00']
    HyperBomb = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x04',b'\x82',b'\x02',b'\x40',b'\x06',b'\xA4']
    FireStorm = [b'\x03',b'\xCC',b'\x02',b'\x88',b'\x00',b'\x0A',b'\x00',b'\x06',b'\x00',b'\x0E']
    ThunderBeam = [b'\x06',b'\xCC',b'\x02',b'\x88',b'\x04',b'\x44',b'\x02',b'\x22',b'\x06',b'\x66']
    SuperArm = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x01',b'\x25',b'\x00',b'\x13',b'\x02',b'\x47']

    BubbleLead = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x04',b'\x44',b'\x02',b'\x22',b'\x08',b'\x88']
    AirShooter = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x08',b'\x20',b'\x05',b'\x00',b'\x0A',b'\x50']
    LeafShield = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x04',b'\x82',b'\x02',b'\x40',b'\x06',b'\xA4']
    QuickBoomerang = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x04',b'\x0C',b'\x02',b'\x04',b'\x06',b'\x2C']
    CrashBomber = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x00',b'\x2A',b'\x00',b'\x28',b'\x00',b'\x6C']
    TimeStopper = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x06',b'\x06',b'\x04',b'\x04',b'\x0C',b'\x48']
    MetalBlade = [b'\x06',b'\xCC',b'\x02',b'\x88',b'\x00',b'\x46',b'\x00',b'\x24',b'\x02',b'\x48']
    AtomicFire = [b'\x03',b'\xCC',b'\x02',b'\x88',b'\x00',b'\x08',b'\x00',b'\x04',b'\x00',b'\x0C']

    SparkShock = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x00',b'\x2A',b'\x00',b'\x2A',b'\x00',b'\x8E']
    SearchSnake = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x02',b'\x82',b'\x00',b'\x40',b'\x04',b'\xA4']
    NeedleCannon = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x02',b'\x48',b'\x00',b'\x24',b'\x02',b'\x6A']
    HardKnuckle = [b'\x0A',b'\x88',b'\x06',b'\x44',b'\x0A',b'\x44',b'\x06',b'\x22',b'\x0C',b'\x66']
    TopSpin = [b'\x06',b'\xCC',b'\x02',b'\x88',b'\x04',b'\x44',b'\x02',b'\x22',b'\x08',b'\x88']
    GeminiLaser = [b'\x0C',b'\xCC',b'\x0C',b'\xA8',b'\x0E',b'\x82',b'\x0A',b'\x40',b'\x0E',b'\xA4']
    MagnetMissile = [b'\x08',b'\x88',b'\x04',b'\x44',b'\x00',b'\x08',b'\x00',b'\x04',b'\x00',b'\x0C']
    ShadowBlade = [b'\x08',b'\x6E',b'\x04',b'\x2C',b'\x06',b'\x08',b'\x04',b'\x04',b'\x08',b'\x2A']
    if MM3 == True:
        if Vanilla == True:
            for y in range(8):
                if pos[y][0] == "Cutman": #Checks to see which bosses are generated
                    Value2 = pos[y][1]
                    Pointer = 0x6465A
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2]) #Writes the Get weapon screen value based on position
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0) #Writes the palette data at those addresses
                        ROM.write(RollingCutter[x])
                elif pos[y][0] == "Flashman": #Repeat 21 more times.
                    Value2 = pos[y][1]
                    Pointer = 0x64674
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(TimeStopper[x])
                elif pos[y][0] == "Metalman":
                    Value2 = pos[y][1]
                    Pointer = 0x64673
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(MetalBlade[x])
                elif pos[y][0] == "Topman":
                    Value2 = pos[y][1]
                    Pointer = 0x64686
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(TopSpin[x])
                elif pos[y][0] == "Airman":
                    Value2 = pos[y][1]
                    Pointer = 0x6466F
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(AirShooter[x])
                elif pos[y][0] == "Geminiman":
                    Value2 = pos[y][1]
                    Pointer = 0x64687
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(GeminiLaser[x])
                elif pos[y][0] == "Quickman":
                    Value2 = pos[y][1]
                    Pointer = 0x64670
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(QuickBoomerang[x])
                elif pos[y][0] == "Iceman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465C
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(IceSlasher[x])
                elif pos[y][0] == "Sparkman":
                    Value2 = pos[y][1]
                    Pointer = 0x64682
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(SparkShock[x])
                elif pos[y][0] == "Gutsman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465B
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(SuperArm[x])
                elif pos[y][0] == "Bombman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465D
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(HyperBomb[x])
                elif pos[y][0] == "Fireman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465E
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(FireStorm[x])
                elif pos[y][0] == "Elecman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465F
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(ThunderBeam[x])
                elif pos[y][0] == "Bubbleman":
                    Value2 = pos[y][1]
                    Pointer = 0x6466E
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(BubbleLead[x])
                elif pos[y][0] == "Heatman":
                    Value2 = pos[y][1]
                    Pointer = 0x64671
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(AtomicFire[x])
                elif pos[y][0] == "Woodman":
                    Value2 = pos[y][1]
                    Pointer = 0x64672
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(LeafShield[x])
                elif pos[y][0] == "Crashman":
                    Value2 = pos[y][1]
                    Pointer = 0x64675
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(CrashBomber[x])
                elif pos[y][0] == "Snakeman":
                    Value2 = pos[y][1]
                    Pointer = 0x64683
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(SearchSnake[x])
                elif pos[y][0] == "Needleman":
                    Value2 = pos[y][1]
                    Pointer = 0x64684
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(NeedleCannon[x])
                elif pos[y][0] == "Hardman":
                    Value2 = pos[y][1]
                    Pointer = 0x64685
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(HardKnuckle[x])
                elif pos[y][0] == "Magnetman":
                    Value2 = pos[y][1]
                    Pointer = 0x64688
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(MagnetMissile[x])
                elif pos[y][0] == "Shadowman":
                    Value2 = pos[y][1]
                    Pointer = 0x64689
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(ShadowBlade[x])

#!Get weapon screen if randomboss/weapons and palette writing if random weapons for MM3
        if Vanilla == False:
            for x in range(8):
                if pos[x][0] == "Cutman": #Based on position, if Stage is ____man's, writes Value[x] to the address
                      Pointer = 0x6465A
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Gutsman":
                      Pointer = 0x6465B
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Iceman":
                      Pointer = 0x6465C
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Bombman":
                      Pointer = 0x6465D
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Fireman":
                      Pointer = 0x6465E
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Elecman":
                      Pointer = 0x6465F
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Bubbleman":
                      Pointer = 0x6466E
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Airman":
                      Pointer = 0x6466F
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Quickman":
                      Pointer = 0x64670
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Heatman":
                      Pointer = 0x64671
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Woodman":
                      Pointer = 0x64672
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Metalman":
                      Pointer = 0x64673
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Flashman":
                      Pointer = 0x64674
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Crashman":
                      Pointer = 0x64675
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Sparkman":
                      Pointer = 0x64682
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Snakeman":
                      Pointer = 0x64683
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Needleman":
                      Pointer = 0x64684
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Hardman":
                      Pointer = 0x64685
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Topman":
                      Pointer = 0x64686
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Geminiman":
                      Pointer = 0x64687
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Magnetman":
                      Pointer = 0x64688
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Shadowman":
                      Pointer = 0x64689
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                      
        if randomboss == True: #!
            for y in range(8):
                if posB[y][0] == "Cutman": #Checks to see which bosses are generated
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0) #Writes the palette data at those addresses
                        ROM.write(RollingCutter[x])
                elif posB[y][0] == "Flashman": #Repeat 21 more times.
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(TimeStopper[x])
                elif posB[y][0] == "Metalman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(MetalBlade[x])
                elif posB[y][0] == "Topman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(TopSpin[x])
                elif posB[y][0] == "Airman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(AirShooter[x])
                elif posB[y][0] == "Geminiman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(GeminiLaser[x])
                elif posB[y][0] == "Quickman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(QuickBoomerang[x])
                elif posB[y][0] == "Iceman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(IceSlasher[x])
                elif posB[y][0] == "Sparkman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(SparkShock[x])
                elif posB[y][0] == "Gutsman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(SuperArm[x])
                elif posB[y][0] == "Bombman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(HyperBomb[x])
                elif posB[y][0] == "Fireman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(FireStorm[x])
                elif posB[y][0] == "Elecman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(ThunderBeam[x])
                elif posB[y][0] == "Bubbleman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(BubbleLead[x])
                elif posB[y][0] == "Heatman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(AtomicFire[x])
                elif posB[y][0] == "Woodman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(LeafShield[x])
                elif posB[y][0] == "Crashman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(CrashBomber[x])
                elif posB[y][0] == "Snakeman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(SearchSnake[x])
                elif posB[y][0] == "Needleman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(NeedleCannon[x])
                elif posB[y][0] == "Hardman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(HardKnuckle[x])
                elif posB[y][0] == "Magnetman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(MagnetMissile[x])
                elif posB[y][0] == "Shadowman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    for x in range(10):
                        Seek = ROM.seek(Pointer[x],0)
                        ROM.write(ShadowBlade[x])
                        
        if randomweapons == True: #!
            for x in range(8):
                #Compares weapons to what is in the list. If match is found, based on position it will write address
                if weapons[x] == Airbyte: 
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0) #Seeking Addresses
                        ROM.write(AirShooter[y]) #Writing Values
                elif weapons[x] == Cutbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(RollingCutter[y])
                elif weapons[x] == Gutsbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(SuperArm[y])
                elif weapons[x] == Icebyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(IceSlasher[y])
                elif weapons[x] == Bombbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(HyperBomb[y])
                elif weapons[x] == Firebyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(FireStorm[y])
                elif weapons[x] == Elecbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(ThunderBeam[y])
                elif weapons[x] == Bubblebyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(BubbleLead[y])
                elif weapons[x] == Quickbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(QuickBoomerang[y])
                elif weapons[x] == Heatbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(AtomicFire[y])
                elif weapons[x] == Woodbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(LeafShield[y])
                elif weapons[x] == Metalbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(MetalBlade[y])
                elif weapons[x] == Flashbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(TimeStopper[y])
                elif weapons[x] == Crashbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(CrashBomber[y])
                elif weapons[x] == Sparkbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(SparkShock[y])
                elif weapons[x] == Snakebyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(SearchSnake[y])
                elif weapons[x] == Needlebyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(NeedleCannon[y])
                elif weapons[x] == Hardbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(HardKnuckle[y])
                elif weapons[x] == Topbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(TopSpin[y])
                elif weapons[x] == Geminibyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(GeminiLaser[y])
                elif weapons[x] == Magnetbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(MagnetMissile[y])
                elif weapons[x] == Shadowbyte:
                    Pointer = Palette[x]
                    for y in range(10):
                        Seek = ROM.seek(Pointer[y],0)
                        ROM.write(ShadowBlade[y])

#MM2 Weapon Text Writing section
    Value = [b'\x00',b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07'] #Values for Get Weapon Screen
    Palette = [0x1E3836,0x1E3776,0x1E3816,0x1E3856,0x1E37D6,0x1E37B6,0x1E37F6,0x1E3796]
    RollingCutter = [b'\x0E',b'\xEE',b'\x0C',b'\xCC',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x04',b'\x44',b'\x02',b'\x22',b'\x02',b'\x00'] #Values for Palettes
    IceSlasher = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x0A',b'\x20',b'\x08',b'\x00',b'\x06',b'\x00',b'\x04',b'\x00']
    HyperBomb = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x04',b'\xC0',b'\x02',b'\x80',b'\x00',b'\x40',b'\x00',b'\x20']
    FireStorm = [b'\x00',b'\xAE',b'\x00',b'\x8C',b'\x00',b'\x4A',b'\x06',b'\x0E',b'\x04',b'\x0A',b'\x00',b'\x06',b'\x00',b'\x04']
    ThunderBeam = [b'\x04',b'\xCE',b'\x00',b'\x8C',b'\x00',b'\x4A',b'\x06',b'\x66',b'\x04',b'\x44',b'\x02',b'\x22',b'\x02',b'\x00']
    SuperArm = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x00',b'\x68',b'\x00',b'\x24',b'\x00',b'\x12',b'\x00',b'\x02']

    BubbleLead = [b'\x0E',b'\xEE',b'\x0C',b'\xCC',b'\x0A',b'\xAA',b'\x08',b'\x88',b'\x06',b'\x66',b'\x04',b'\x44',b'\x02',b'\x20']
    AirShooter = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x0E',b'\x40',b'\x0C',b'\x20',b'\x0A',b'\x00',b'\x06',b'\x00']
    LeafShield = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x04',b'\xC0',b'\x02',b'\x80',b'\x00',b'\x40',b'\x00',b'\x20']
    QuickBoomerang = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x0A',b'\x6C',b'\x06',b'\x2A',b'\x04',b'\x06',b'\x02',b'\x02']
    CrashBomber = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x00',b'\x8E',b'\x00',b'\x4C',b'\x00',b'\x08',b'\x00',b'\x04']
    TimeStopper = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x0C',b'\x2C',b'\x08',b'\x08',b'\x04',b'\x04',b'\x02',b'\x02']
    MetalBlade = [b'\x04',b'\xCE',b'\x00',b'\x8C',b'\x00',b'\x4A',b'\x02',b'\x68',b'\x00',b'\x46',b'\x00',b'\x24',b'\x00',b'\x02']
    AtomicFire = [b'\x00',b'\xAE',b'\x00',b'\x8C',b'\x00',b'\x4A',b'\x04',b'\x0C',b'\x02',b'\x08',b'\x00',b'\x04',b'\x00',b'\x02']

    SparkShock = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x00',b'\xAE',b'\x00',b'\x6E',b'\x00',b'\x2A',b'\x00',b'\x06']
    SearchSnake = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x06',b'\xC0',b'\x04',b'\x80',b'\x02',b'\x40',b'\x00',b'\x20']
    NeedleCannon = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x00',b'\xAC',b'\x00',b'\x68',b'\x00',b'\x46',b'\x00',b'\x04']
    HardKnuckle = [b'\x0C',b'\xAA',b'\x08',b'\x66',b'\x04',b'\x22',b'\x0C',b'\x66',b'\x0A',b'\x44',b'\x06',b'\x22',b'\x04',b'\x00']
    TopSpin = [b'\x04',b'\xCE',b'\x00',b'\x8C',b'\x00',b'\x4A',b'\x08',b'\x88',b'\x06',b'\x66',b'\x04',b'\x44',b'\x02',b'\x20']
    GeminiLaser = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66',b'\x0E',b'\x84',b'\x0C',b'\x62',b'\x0A',b'\x40',b'\x08',b'\x00']
    MagnetMissile = [b'\x0A',b'\xAA',b'\x08',b'\x88',b'\x06',b'\x66',b'\x00',b'\x0A',b'\x00',b'\x08',b'\x00',b'\x04',b'\x00',b'\x02']
    ShadowBlade = [b'\x0C',b'\x8E',b'\x08',b'\x6A',b'\x04',b'\x46',b'\x08',b'\x28',b'\x06',b'\x06',b'\x04',b'\x04',b'\x02',b'\x02']
    ItemX = [b'\x0E',b'\xEE',b'\x0A',b'\xAA',b'\x06',b'\x66']
    if MM2 == True: #!
        Pointer = 0x1E3876 # Updates MM2 Item underarmor palette to less dark
        Seek = ROM.seek(Pointer,0)
        for x in range(6):
            ValueI = ItemX[x]
            ROM.write(ValueI)
            Pointer+=1
        if Vanilla == True:
            for y in range(8):
                if pos[y][0] == "Cutman": #Checks to see which bosses are generated
                    Value2 = pos[y][1]
                    Pointer = 0x6465A
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2]) #Writes the Get weapon screen value based on position
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(RollingCutter[x])#Writes the palette data at those addresses
                        Pointer += 1
                elif pos[y][0] == "Flashman": #Repeat 21 more times.
                    Value2 = pos[y][1]
                    Pointer = 0x64674
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Alien,0)
                    for x in range(14):
                        ROM.write(TimeStopper[x])
                        Pointer += 1
                elif pos[y][0] == "Metalman":
                    Value2 = pos[y][1]
                    Pointer = 0x64673
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(MetalBlade[x])
                        Pointer += 1
                elif pos[y][0] == "Topman":
                    Value2 = pos[y][1]
                    Pointer = 0x64686
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(TopSpin[x])
                        Pointer += 1
                elif pos[y][0] == "Airman":
                    Value2 = pos[y][1]
                    Pointer = 0x6466F
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(AirShooter[x])
                        Pointer += 1
                elif pos[y][0] == "Geminiman":
                    Value2 = pos[y][1]
                    Pointer = 0x64687
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(GeminiLaser[x])
                        Pointer += 1
                elif pos[y][0] == "Quickman":
                    Value2 = pos[y][1]
                    Pointer = 0x64670
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(QuickBoomerang[x])
                        Pointer += 1
                elif pos[y][0] == "Iceman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465C
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(IceSlasher[x])
                        Pointer += 1
                elif pos[y][0] == "Sparkman":
                    Value2 = pos[y][1]
                    Pointer = 0x64682
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(SparkShock[x])
                        Pointer += 1
                elif pos[y][0] == "Gutsman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465B
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(SuperArm[x])
                        Pointer += 1
                elif pos[y][0] == "Bombman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465D
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(HyperBomb[x])
                        Pointer += 1
                elif pos[y][0] == "Fireman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465E
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(FireStorm[x])
                        Pointer += 1
                elif pos[y][0] == "Elecman":
                    Value2 = pos[y][1]
                    Pointer = 0x6465F
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(ThunderBeam[x])
                        Pointer += 1
                elif pos[y][0] == "Bubbleman":
                    Value2 = pos[y][1]
                    Pointer = 0x6466E
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(BubbleLead[x])
                        Pointer += 1
                elif pos[y][0] == "Heatman":
                    Value2 = pos[y][1]
                    Pointer = 0x64671
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(AtomicFire[x])
                        Pointer += 1
                elif pos[y][0] == "Woodman":
                    Value2 = pos[y][1]
                    Pointer = 0x64672
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(LeafShield[x])
                        Pointer += 1
                elif pos[y][0] == "Crashman":
                    Value2 = pos[y][1]
                    Pointer = 0x64675
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(CrashBomber[x])
                        Pointer += 1
                elif pos[y][0] == "Snakeman":
                    Value2 = pos[y][1]
                    Pointer = 0x64683
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(SearchSnake[x])
                        Pointer += 1
                elif pos[y][0] == "Needleman":
                    Value2 = pos[y][1]
                    Pointer = 0x64684
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(NeedleCannon[x])
                        Pointer += 1
                elif pos[y][0] == "Hardman":
                    Value2 = pos[y][1]
                    Pointer = 0x64685
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(HardKnuckle[x])
                        Pointer += 1
                elif pos[y][0] == "Magnetman":
                    Value2 = pos[y][1]
                    Pointer = 0x64688
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(MagnetMissile[x])
                        Pointer += 1
                elif pos[y][0] == "Shadowman":
                    Value2 = pos[y][1]
                    Pointer = 0x64689
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value[Value2])
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(ShadowBlade[x])
                        Pointer += 1

#Get weapon screen if randomboss/weapons and palette writing if random weapons for MM2
        if Vanilla == False: #!
            for x in range(8):
                if pos[x][0] == "Cutman": #Based on position, if Stage is ____man's, writes Value[x] to the address
                      Pointer = 0x6465A
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Gutsman":
                      Pointer = 0x6465B
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Iceman":
                      Pointer = 0x6465C
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Bombman":
                      Pointer = 0x6465D
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Fireman":
                      Pointer = 0x6465E
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Elecman":
                      Pointer = 0x6465F
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Bubbleman":
                      Pointer = 0x6466E
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Airman":
                      Pointer = 0x6466F
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Quickman":
                      Pointer = 0x64670
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Heatman":
                      Pointer = 0x64671
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Woodman":
                      Pointer = 0x64672
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Metalman":
                      Pointer = 0x64673
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Flashman":
                      Pointer = 0x64674
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Crashman":
                      Pointer = 0x64675
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Sparkman":
                      Pointer = 0x64682
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Snakeman":
                      Pointer = 0x64683
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Needleman":
                      Pointer = 0x64684
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Hardman":
                      Pointer = 0x64685
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Topman":
                      Pointer = 0x64686
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Geminiman":
                      Pointer = 0x64687
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Magnetman":
                      Pointer = 0x64688
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                elif pos[x][0] == "Shadowman":
                      Pointer = 0x64689
                      Seek = ROM.seek(Pointer, 0)
                      ROM.write(Value[x])
                      
        if randomboss == True: #!
            for y in range(8):
                if posB[y][0] == "Cutman": #Checks to see which bosses are generated
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14): #Writes the palette data at those addresses
                        ROM.write(RollingCutter[x])
                        Pointer += 1
                elif posB[y][0] == "Flashman": #Repeat 21 more times.
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(TimeStopper[x])
                        Pointer += 1
                elif posB[y][0] == "Metalman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(MetalBlade[x])
                        Pointer += 1
                elif posB[y][0] == "Topman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(TopSpin[x])
                        Pointer += 1
                elif posB[y][0] == "Airman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(AirShooter[x])
                        Pointer += 1
                elif posB[y][0] == "Geminiman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(GeminiLaser[x])
                        Pointer += 1
                elif posB[y][0] == "Quickman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(QuickBoomerang[x])
                        Pointer += 1
                elif posB[y][0] == "Iceman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(IceSlasher[x])
                        Pointer += 1
                elif posB[y][0] == "Sparkman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(SparkShock[x])
                        Pointer += 1
                elif posB[y][0] == "Gutsman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(SuperArm[x])
                        Pointer += 1
                elif posB[y][0] == "Bombman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(HyperBomb[x])
                        Pointer += 1
                elif posB[y][0] == "Fireman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(FireStorm[x])
                        Pointer += 1
                elif posB[y][0] == "Elecman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(ThunderBeam[x])
                        Pointer += 1
                elif posB[y][0] == "Bubbleman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(BubbleLead[x])
                        Pointer += 1
                elif posB[y][0] == "Heatman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(AtomicFire[x])
                        Pointer += 1
                elif posB[y][0] == "Woodman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(LeafShield[x])
                        Pointer += 1
                elif posB[y][0] == "Crashman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(CrashBomber[x])
                        Pointer += 1
                elif posB[y][0] == "Snakeman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(SearchSnake[x])
                        Pointer += 1
                elif posB[y][0] == "Needleman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(NeedleCannon[x])
                        Pointer += 1
                elif posB[y][0] == "Hardman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(HardKnuckle[x])
                        Pointer += 1
                elif posB[y][0] == "Magnetman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(MagnetMissile[x])
                        Pointer += 1
                elif posB[y][0] == "Shadowman":
                    Value2 = posB[y][1]
                    Pointer = Palette[Value2]
                    Seek = ROM.seek(Pointer,0)
                    for x in range(14):
                        ROM.write(ShadowBlade[x])
                        Pointer += 1
                                   
        if randomweapons == True: #!
            for x in range(8):
                #Compares weapons to what is in the list. If match is found, based on position it will write address
                if weapons[x] == Airbyte: 
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(AirShooter[y]) #Writing Values
                        Pointer += 1
                elif weapons[x] == Cutbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(RollingCutter[y])
                        Pointer += 1
                elif weapons[x] == Gutsbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(SuperArm[y])
                        Pointer += 1
                elif weapons[x] == Icebyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(IceSlasher[y])
                        Pointer += 1
                elif weapons[x] == Bombbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(HyperBomb[y])
                        Pointer += 1
                elif weapons[x] == Firebyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(FireStorm[y])
                        Pointer += 1
                elif weapons[x] == Elecbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(ThunderBeam[y])
                        Pointer += 1
                elif weapons[x] == Bubblebyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(BubbleLead[y])
                        Pointer += 1
                elif weapons[x] == Quickbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(QuickBoomerang[y])
                        Pointer += 1
                elif weapons[x] == Heatbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(AtomicFire[y])
                        Pointer += 1
                elif weapons[x] == Woodbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(LeafShield[y])
                        Pointer += 1
                elif weapons[x] == Metalbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(MetalBlade[y])
                        Pointer += 1
                elif weapons[x] == Flashbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(TimeStopper[y])
                        Pointer += 1
                elif weapons[x] == Crashbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(CrashBomber[y])
                        Pointer += 1
                elif weapons[x] == Sparkbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(SparkShock[y])
                        Pointer += 1
                elif weapons[x] == Snakebyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(SearchSnake[y])
                        Pointer += 1
                elif weapons[x] == Needlebyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(NeedleCannon[y])
                        Pointer += 1
                elif weapons[x] == Hardbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(HardKnuckle[y])
                        Pointer += 1
                elif weapons[x] == Topbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(TopSpin[y])
                        Pointer += 1
                elif weapons[x] == Geminibyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(GeminiLaser[y])
                        Pointer += 1
                elif weapons[x] == Magnetbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(MagnetMissile[y])
                        Pointer += 1
                elif weapons[x] == Shadowbyte:
                    Pointer = Palette[x]
                    Seek = ROM.seek(Pointer,0)
                    for y in range(14):
                        ROM.write(ShadowBlade[y])
                        Pointer += 1
                
#Writing weapon data if no random weapons
    Weaponmenu = [0x65A53,0x65A55,0x65A57,0x65A59,0x65A5B,0x65A61,0x65A63,0x65A65]
    Weapongraphics = [0x709CC,0x709D0,0x709D4,0x709D8,0x709DC,0x709E0,0x709E4,0x709E8]
    Weaponname = [0x65A79,0x65A7F,0x65A85,0x65A8B,0x65A91,0x65AA3,0x65AA9,0x65AAF]
    Cut = [b'\x05',b'\x3C',b'\x22',b'\x1B',b'\x0C']
    Guts = [b'\x03',b'\x39',b'\xE2',b'\x1C',b'\x0A']
    Ice = [b'\x04',b'\x3B',b'\x02',b'\x12',b'\x1C']
    Bomb = [b'\x01',b'\x37',b'\xA2',b'\x11',b'\x0B']
    Fire = [b'\x06',b'\x3D',b'\x42',b'\x0F',b'\x1C']
    Elec = [b'\x02',b'\x38',b'\xC2',b'\x1D',b'\x0B']

    Bubble = [b'\x0B',b'\x49',b'\xA2',b'\x0B',b'\x15']
    Air = [b'\x09',b'\x47',b'\x62',b'\x0A',b'\x1C']
    Quick = [b'\x0C',b'\x4A',b'\xC2',b'\x1A',b'\x0B']
    Heat = [b'\x08',b'\x46',b'\x42',b'\x0A',b'\x0F']
    Wood = [b'\x0A',b'\x48',b'\x82',b'\x15',b'\x1C']
    Metal = [b'\x0F',b'\x4D',b'\x02',b'\x16',b'\x0B']
    Flash = [b'\x0E',b'\x4B',b'\xE2',b'\x1D',b'\x1C']
    Crash = [b'\x10',b'\x4E',b'\x22',b'\x0C',b'\x0B']

    Spark = [b'\x1A',b'\x27',b'\xE2',b'\x1C',b'\x19']
    Snake = [b'\x19',b'\x26',b'\xC2',b'\x1C',b'\x17']
    Needle = [b'\x14',b'\x21',b'\x22',b'\x17',b'\x0C']
    Hard = [b'\x17',b'\x24',b'\x82',b'\x11',b'\x14']
    Top = [b'\x18',b'\x25',b'\xA2',b'\x1D',b'\x1C']
    Gemini = [b'\x16',b'\x23',b'\x62',b'\x10',b'\x15']
    Magnet = [b'\x15',b'\x22',b'\x42',b'\x16',b'\x16']
    Shadow = [b'\x1B',b'\x29',b'\x02',b'\x1C',b'\x0B']
    if MM3 == True: #!
        if randomweapons == False:
            if Flashman == True: #Finds which bosses have been generated and assigns weapon data
                Pointer = Weaponmenu.pop(0)
                Value = Flash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
            
                Pointer = Weapongraphics.pop(0)
                Value = Flash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
            
                Value = Flash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Flash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Flash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Cutman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Cut.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Cut.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Cut.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Cut.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Cut.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Gutsman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Guts.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Guts.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Guts.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Guts.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Guts.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Iceman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Ice.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Ice.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Ice.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Ice.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Ice.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Bombman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Bomb.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Bomb.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Bomb.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Bomb.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Bomb.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Fireman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Fire.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Fire.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Fire.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Fire.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Fire.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Elecman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Elec.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Elec.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Elec.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Elec.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Elec.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Bubbleman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Bubble.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Bubble.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Bubble.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Bubble.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Bubble.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Airman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Air.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Air.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Air.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Air.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Air.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Quickman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Quick.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Quick.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Quick.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Quick.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Quick.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Heatman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Heat.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Heat.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Heat.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Heat.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Heat.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Woodman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Wood.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Wood.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Wood.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Wood.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Wood.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Metalman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Metal.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Metal.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Metal.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Metal.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Metal.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Crashman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Crash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Crash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Crash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Crash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Crash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Sparkman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Spark.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Spark.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Spark.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Spark.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Spark.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Snakeman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Snake.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Snake.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Snake.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Snake.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Snake.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Needleman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Needle.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Needle.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Needle.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Needle.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Needle.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Hardman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Hard.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Hard.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Hard.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Hard.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Hard.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Topman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Top.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Top.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Top.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Top.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Top.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Geminiman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Gemini.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Gemini.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Gemini.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Gemini.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Gemini.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Magnetman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Magnet.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Magnet.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Magnet.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Magnet.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Magnet.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
            if Shadowman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Shadow.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weapongraphics.pop(0)
                Value = Shadow.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics Offset 1
                Pointer +=1
                
                Value = Shadow.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Graphics 2
                
                Pointer = Weaponname.pop(0)
                Value = Shadow.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 1
                Pointer +=2
                
                Value = Shadow.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Name 2
                
    #!Writing data if Randomweapons mode
        if randomweapons == True:#Similar to the code section above, but gives weapon data based on randomly generated weapons
            for x in range(8):
                if weapons[x] == Cutbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Cut.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Cut.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Cut.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Cut.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Cut.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2

                elif weapons[x] == Gutsbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Guts.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Guts.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Guts.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Guts.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Guts.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Icebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Ice.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Ice.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Ice.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Ice.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Ice.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Bombbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Bomb.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Bomb.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Bomb.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Bomb.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Bomb.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Firebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Fire.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Fire.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Fire.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Fire.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Fire.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Elecbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Elec.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Elec.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Elec.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Elec.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Elec.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Bubblebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Bubble.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Bubble.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Bubble.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Bubble.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Bubble.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Airbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Air.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Air.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Air.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Air.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Air.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Quickbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Quick.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Quick.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Quick.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Quick.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Quick.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Heatbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Heat.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Heat.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Heat.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Heat.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Heat.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Woodbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Wood.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Wood.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Wood.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Wood.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Wood.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Metalbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Metal.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Metal.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Metal.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Metal.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Metal.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Flashbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Flash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Flash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Flash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Flash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Flash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Crashbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Crash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Crash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Crash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Crash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Crash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
                elif weapons[x] == Sparkbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Spark.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Spark.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Spark.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Spark.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Spark.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                elif weapons[x] == Snakebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Snake.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Snake.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Snake.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Snake.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Snake.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                elif weapons[x] == Needlebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Needle.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Needle.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Needle.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Needle.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Needle.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                elif weapons[x] == Hardbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Hard.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Hard.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Hard.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Hard.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Hard.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                elif weapons[x] == Topbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Top.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Top.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Top.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Top.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Top.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                elif weapons[x] == Geminibyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Gemini.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Gemini.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Gemini.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Gemini.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Gemini.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                elif weapons[x] == Magnetbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Magnet.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Magnet.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Magnet.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Magnet.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Magnet.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                elif weapons[x] == Shadowbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Shadow.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weapongraphics.pop(0)
                    Value = Shadow.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics Offset 1
                    Pointer +=1
                    
                    Value = Shadow.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Graphics 2
                    
                    Pointer = Weaponname.pop(0)
                    Value = Shadow.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name 1
                    Pointer +=2
                    
                    Value = Shadow.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Name 2
                    
#MM2 Weapon Menu writing
    Weaponmenu = [0x659C5,0x659C7,0x659C9,0x659CB,0x659CD,0x659D3,0x659D5,0x659D7]
    Weaponname = [0x659E9,0x659ED,0x659F1,0x659F5,0x659F9,0x65A05,0x65A09,0x65A0D]
    Cut = [b'\x05',b'\x0C']
    Guts = [b'\x03',b'\x10']
    Ice = [b'\x04',b'\x12']
    Bomb = [b'\x01',b'\x0B']
    Fire = [b'\x06',b'\x0F']
    Elec = [b'\x02',b'\x0E']

    Bubble = [b'\x0B',b'\x0B']
    Air = [b'\x09',b'\x0A']
    Quick = [b'\x0C',b'\x1A']
    Heat = [b'\x08',b'\x11']
    Wood = [b'\x0A',b'\x20']
    Metal = [b'\x0F',b'\x16']
    Flash = [b'\x0E',b'\x0F']
    Crash = [b'\x10',b'\x0C']

    Spark = [b'\x1A',b'\x1C']
    Snake = [b'\x19',b'\x1C']
    Needle = [b'\x14',b'\x17']
    Hard = [b'\x17',b'\x11']
    Top = [b'\x18',b'\x1D']
    Gemini = [b'\x16',b'\x10']
    Magnet = [b'\x15',b'\x16']
    Shadow = [b'\x1B',b'\x1C']                
    if MM2 == True: #!
        if randomweapons == False:
            if Flashman == True: #Finds which bosses have been generated and assigns weapon data
                Pointer = Weaponmenu.pop(0)
                Value = Flash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
            
                Pointer = Weaponname.pop(0)
                Value = Flash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Cutman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Cut.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weaponname.pop(0)
                Value = Cut.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Gutsman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Guts.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weaponname.pop(0)
                Value = Guts.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Iceman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Ice.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Ice.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name 
                
            if Bombman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Bomb.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Bomb.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Fireman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Fire.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Fire.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Elecman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Elec.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Elec.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Bubbleman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Bubble.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Bubble.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Airman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Air.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Air.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Quickman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Quick.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Quick.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Heatman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Heat.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Heat.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Woodman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Wood.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Wood.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Metalman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Metal.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Metal.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Crashman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Crash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Crash.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Sparkman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Spark.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Spark.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Snakeman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Snake.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Snake.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Needleman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Needle.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Needle.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Hardman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Hard.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Hard.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Topman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Top.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written
                
                Pointer = Weaponname.pop(0)
                Value = Top.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Geminiman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Gemini.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Gemini.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Magnetman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Magnet.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Magnet.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
            if Shadowman == True:
                Pointer = Weaponmenu.pop(0)
                Value = Shadow.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value) #Weapon value written

                Pointer = Weaponname.pop(0)
                Value = Shadow.pop(0)
                Seek = ROM.seek(Pointer,0)
                ROM.write(Value)#Name
                
    #Writing data if Randomweapons mode
        if randomweapons == True:#!Similar to the code section above, but gives weapon data based on randomly generated weapons
            for x in range(8):
                if weapons[x] == Cutbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Cut.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Cut.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name

                elif weapons[x] == Gutsbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Guts.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Guts.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Icebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Ice.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weaponname.pop(0)
                    Value = Ice.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Bombbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Bomb.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Bomb.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Firebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Fire.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Fire.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Elecbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Elec.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Elec.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Bubblebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Bubble.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Bubble.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Airbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Air.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                                      
                    Pointer = Weaponname.pop(0)
                    Value = Air.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Quickbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Quick.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Quick.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Heatbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Heat.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Heat.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Woodbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Wood.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Wood.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Metalbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Metal.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Metal.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Flashbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Flash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Flash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Crashbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Crash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Crash.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Sparkbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Spark.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Spark.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Snakebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Snake.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weaponname.pop(0)
                    Value = Snake.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Needlebyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Needle.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Needle.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Hardbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Hard.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weaponname.pop(0)
                    Value = Hard.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Topbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Top.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Top.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Geminibyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Gemini.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Gemini.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Magnetbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Magnet.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written

                    Pointer = Weaponname.pop(0)
                    Value = Magnet.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                    
                elif weapons[x] == Shadowbyte:
                    Pointer = Weaponmenu.pop(0)
                    Value = Shadow.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value) #Weapon value written
                    
                    Pointer = Weaponname.pop(0)
                    Value = Shadow.pop(0)
                    Seek = ROM.seek(Pointer,0)
                    ROM.write(Value)#Name
                
#Stage Select Text and animation writing if no random bosses
    Pointer = [0x66D64,0x66D68,0x66D6C,0x66D70,0x66D74,0x66D78,0x66D7C,0x66D80]
    Pointer2 = [0x66E55,0x66E5D,0x66E65,0x66E6D,0x66E75,0x66E7D,0x66E85,0x66E8D] 
    Flash = [b'\x6C',b'\x50',b'\x45',b'\x78',b'\x0F']
    Cut = [b'\x6B',b'\x3E',b'\x18',b'\x7A',b'\x5A']
    Guts = [b'\x6B',b'\x46',b'\x19',b'\xB0',b'\x55']
    Ice = [b'\x6B',b'\x4E',b'\x14',b'\xD0',b'\x89']
    Bomb = [b'\x6B',b'\x56',b'\x15',b'\xB0',b'\xC0']
    Fire = [b'\x6B',b'\x5E',b'\x16',b'\x7A',b'\xBC']
    Elec = [b'\x6B',b'\x66',b'\x17',b'\x55',b'\x89']

    Bubble = [b'\x6C',b'\x1A',b'\x47',b'\x78',b'\x0F']
    Air = [b'\x6C',b'\x24',b'\x41',b'\x78',b'\x0F']
    Quick = [b'\x6C',b'\x2C',b'\x46',b'\x78',b'\x0F']
    Heat = [b'\x6C',b'\x36',b'\x48',b'\x78',b'\x0F']
    Wood = [b'\x6C',b'\x3E',b'\x44',b'\x78',b'\x0F']
    Metal = [b'\x6C',b'\x46',b'\x43',b'\x78',b'\x0F']
    Crash = [b'\x6C',b'\x5A',b'\x42',b'\x78',b'\x0F']

    Spark = [b'\x6D',b'\x82',b'\x78',b'\x18',b'\x20']
    Snake = [b'\x6D',b'\x8C',b'\x76',b'\x68',b'\x20']
    Needle = [b'\x6D',b'\x96',b'\x7A',b'\xB8',b'\x20']
    Hard = [b'\x6D',b'\xA0',b'\x74',b'\x18',b'\x60']
    Top = [b'\x6D',b'\xA8',b'\x75',b'\xB8',b'\x60']
    Gemini = [b'\x6D',b'\xB0',b'\x7B',b'\x18',b'\xA0']
    Magnet = [b'\x6D',b'\xBA',b'\x77',b'\x68',b'\xA0']
    Shadow = [b'\x6D',b'\xC4',b'\x79',b'\xB8',b'\xA0']
    Random = [b'\x6E',b'\x58',b'\xB5',b'\x80',b'\x80']
    if MM3 == True: #!
        if randomboss == False:
            for x in range(8):
                 if pos[x][1] == x: #If x matches position boss is in pos list
                        if pos[x][0] == "Flashman": #If the boss is found in the previous element
                            Pointer3 = Pointer[x] #Text pointers
                            Seek = ROM.seek(Pointer3,0)
                            Value = Flash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Flash.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x] #Animation data
                            Seek = ROM.seek(Pointer3,0)
                            Value = Flash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Flash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Flash.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Cutman": #Repeat 21 more times
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Cut.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Cut.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Cut.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Cut.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Cut.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Gutsman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Guts.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Guts.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Guts.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Guts.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Guts.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Iceman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Ice.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Ice.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Ice.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Ice.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Ice.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Bombman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Fireman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Fire.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Fire.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Fire.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Fire.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Fire.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Elecman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Elec.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Elec.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Elec.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Elec.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Elec.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Bubbleman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Airman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Air.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Air.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Air.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Air.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Air.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Quickman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Quick.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Quick.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Quick.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Quick.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Quick.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Heatman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Heat.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Heat.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Heat.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Heat.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Heat.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Woodman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Wood.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Wood.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Wood.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Wood.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Wood.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Metalman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Metal.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Metal.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Metal.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Metal.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Metal.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Crashman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Crash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Crash.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Crash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Crash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Crash.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Sparkman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Spark.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Spark.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Spark.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Spark.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Spark.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Snakeman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Snake.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Snake.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Snake.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Snake.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Snake.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Needleman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Needle.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Needle.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Needle.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Needle.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Needle.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Hardman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Hard.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Hard.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Hard.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Hard.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Hard.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Topman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Top.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Top.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Top.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Top.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Top.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Geminiman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Magnetman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Shadowman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                        
#Stage select text and animation writing if random boss
    if MM3 == True: #!
        if randomboss == True:
            for x in range(8): #Writes values to each different address as ? with no text
                Pointer3 = Pointer[x]
                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[0])
                
                Pointer3 += 1
                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[1])

                Pointer3 = Pointer2[x]
                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[2])
                Pointer3 += 1
                
                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[3])
                Pointer3 += 1

                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[4])
                
#MM2 Mode Stage Selected text and animation
    Pointer = [0x66BFC,0x66C00,0x66C04,0x66C08,0x66C0C,0x66C10,0x66C14,0x66C18]
    Pointer2 = [0x66CB7,0x66CBF,0x66CC7,0x66CCF,0x66CD7,0x66CDF,0x66CE7,0x66CEF] 
    Flash = [b'\x6C',b'\x50',b'\x45',b'\x78',b'\x08']
    Cut = [b'\x6B',b'\x3E',b'\x18',b'\x80',b'\x56']
    Guts = [b'\x6B',b'\x46',b'\x19',b'\xB6',b'\x50']
    Bomb = [b'\x6B',b'\x56',b'\x15',b'\xB0',b'\xBC']
    Elec = [b'\x6B',b'\x66',b'\x17',b'\x55',b'\x86']

    Bubble = [b'\x6C',b'\x1A',b'\x47',b'\x78',b'\x08']
    Air = [b'\x6C',b'\x24',b'\x41',b'\x78',b'\x08']
    Quick = [b'\x6C',b'\x2C',b'\x46',b'\x78',b'\x08']
    Heat = [b'\x6C',b'\x36',b'\x48',b'\x78',b'\x08']
    Wood = [b'\x6C',b'\x3E',b'\x44',b'\x78',b'\x08']
    Metal = [b'\x6C',b'\x46',b'\x43',b'\x78',b'\x08']
    Crash = [b'\x6C',b'\x5A',b'\x42',b'\x78',b'\x08']

    Spark = [b'\x6D',b'\x82',b'\x78',b'\x20',b'\x1C']
    Snake = [b'\x6D',b'\x8C',b'\x76',b'\x70',b'\x18']
    Needle = [b'\x6D',b'\x96',b'\x7A',b'\xC0',b'\x18']
    Hard = [b'\x6D',b'\xA0',b'\x74',b'\x18',b'\x58']
    Top = [b'\x6D',b'\xA8',b'\x75',b'\xC0',b'\x5A']
    Gemini = [b'\x6D',b'\xB0',b'\x7B',b'\x20',b'\x96']
    Magnet = [b'\x6D',b'\xBA',b'\x77',b'\x70',b'\x98']
    Shadow = [b'\x6D',b'\xC4',b'\x79',b'\xC6',b'\x98']
    Random = [b'\x6E',b'\x58',b'\xB5',b'\x75',b'\x78']
    if MM2 == True: #!
        if randomboss == False:
            for x in range(8):
                 if pos[x][1] == x: #If x matches position boss is in pos list
                        if pos[x][0] == "Flashman": #If the boss is found in the previous element
                            Pointer3 = Pointer[x] #Text pointers
                            Seek = ROM.seek(Pointer3,0)
                            Value = Flash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Flash.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x] #Animation data
                            Seek = ROM.seek(Pointer3,0)
                            Value = Flash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Flash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Flash.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Cutman": #Repeat 21 more times
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Cut.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Cut.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Cut.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Cut.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Cut.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Gutsman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Guts.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Guts.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Guts.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Guts.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Guts.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Iceman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Ice.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Ice.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Ice.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Ice.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Ice.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Bombman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bomb.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Fireman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Fire.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Fire.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Fire.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Fire.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Fire.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Elecman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Elec.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Elec.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Elec.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Elec.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Elec.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Bubbleman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Bubble.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Airman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Air.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Air.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Air.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Air.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Air.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Quickman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Quick.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Quick.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Quick.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Quick.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Quick.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Heatman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Heat.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Heat.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Heat.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Heat.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Heat.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Woodman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Wood.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Wood.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Wood.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Wood.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Wood.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Metalman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Metal.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Metal.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Metal.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Metal.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Metal.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Crashman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Crash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Crash.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Crash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Crash.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Crash.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Sparkman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Spark.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Spark.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Spark.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Spark.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Spark.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Snakeman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Snake.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Snake.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Snake.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Snake.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Snake.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Needleman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Needle.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Needle.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Needle.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Needle.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Needle.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Hardman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Hard.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Hard.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Hard.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Hard.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Hard.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Topman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Top.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Top.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Top.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Top.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Top.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Geminiman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Gemini.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Magnetman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Magnet.pop(0)
                            ROM.write(Value)
                        elif pos[x][0] == "Shadowman":
                            Pointer3 = Pointer[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                            Pointer3 = Pointer2[x]
                            Seek = ROM.seek(Pointer3,0)
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                            Pointer3 +=1
                            Value = Shadow.pop(0)
                            ROM.write(Value)
                        
#Stage select text and animation writing if random boss
    if MM2 == True: #!
        if randomboss == True:
            for x in range(8): #Writes values to each different address as ? with no text
                Pointer3 = Pointer[x]
                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[0])
                
                Pointer3 += 1
                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[1])

                Pointer3 = Pointer2[x]
                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[2])
                Pointer3 += 1
                
                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[3])
                Pointer3 += 1

                Seek = ROM.seek(Pointer3,0)
                ROM.write(Random[4])
    
    
#Weakness writing section

    #!Initializing values for what weapons break the crash or hard walls
    Pointer = 0x6F543 
    Seek = ROM.seek(Pointer, 0)
    ROM.write(b'\x81')

    Pointer = 0x6F734
    Seek = ROM.seek(Pointer, 0)
    ROM.write(b'\x81')

    Crashwall = [0x6F52C,0x6F52E,0x6F52F,0x6F530,0x6F532,0x6F533,0x6F534,0x6F535,0x6F537,
                0x6F539,0x6F53A,0x6F53B,0x6F53C,0x6F53D,0x6F53E,0x6F53F,0x6F540,0x6F543]
    
    Crashwallheat = [0x6F531,0x6F541,0x6F542]
    
    Hardwall =[0x6F724,0x6F726,0x6F727,0x6F728,0x6F72A,0x6F72B,0x6F72C,0x6F72D,0x6F72F,
                0x6F731,0x6F732,0x6F733,0x6F734,0x6F735,0x6F736,0x6F737,0x6F738,0x6F73B]

    Hardwallheat = [0x6F729,0x6F739,0x6F740]

    TrapWall = [0x6ED84,0x6ED86,0x6ED87,0x6ED88,0x6ED8A,0x6ED8B,0x6ED8C,
                0x6ED8D,0x6ED8F,0x6ED90,0x6ED91,0x6ED92,0x6ED93,0x6ED94,0x6ED95,0x6ED96,
                 0x6ED97,0x6ED98]
    
    Trapheat = [0x6ED89,0x6ED99,0x6ED9A]
    Weak = []
        
    Retry = True
    Pointer = 0x85807
    for y in range(3):
        if Retry == True:#Grabs randomly generated weapon to smash walls
            Seek = ROM.seek(Pointer,0)
            Value = ROM.read(1)
            Value2 = int.from_bytes(Value, "big")
            Value2 -= 1
            Pointer += 1
            if Vanilla == True:
                for x in range(8):
                    if pos[x][1] == Value2:
                        if pos[x][0] == "Cutman": #If an acceptable weapon is found, gets offset and Breaks loops
                            Offset = 2 
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Gutsman":# if this is not an acceptable weapon, breaks loop and retrys to grab next value
                            break
                        elif pos[x][0] == "Iceman":
                            Offset = 1
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Bombman":
                            break
                        elif pos[x][0] == "Fireman":
                            Offset = 3
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Elecman":
                            Offset = 0
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Bubbleman":
                            Offset = 6
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Airman":
                            Offset = 4
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Quickman":
                            Offset = 7
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Heatman":
                            Heat = True
                            Retry = False
                            break
                        elif pos[x][0] == "Woodman":
                            Offset = 5
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Metalman":
                            Offset = 8
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Crashman":
                            Offset = 17
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Flashman":
                            break
                        elif pos[x][0] == "Sparkman":
                            Offset = 15
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Snakeman":
                            Offset = 14
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Needleman":
                            Offset = 9
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Hardman":
                            Offset = 12
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Topman":
                            Offset = 13
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Geminiman":
                            Offset = 11
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Magnetman":
                            Offset = 10
                            Weak.append(Offset)
                            Retry = False
                            break
                        elif pos[x][0] == "Shadowman":
                            Offset = 16
                            Weak.append(Offset)
                            Retry = False
                            break
                        
            if randomboss == True:
                if randomweapons == False:
                    for x in range(8):
                        if posB[x][1] == Value2:
                            if posB[x][0] == "Cutman": #If an acceptable weapon is found, gets offset and Breaks loops
                                Offset = 2 
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Gutsman": # If this is not an acceptable weapon, breaks loop and retrys to grab next value
                                break
                            elif posB[x][0] == "Iceman":
                                Offset = 1
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Bombman":
                                break
                            elif posB[x][0] == "Fireman":
                                Offset = 3
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Elecman":
                                Offset = 0
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Bubbleman":
                                Offset = 6
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Airman":
                                Offset = 4
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Quickman":
                                Offset = 7
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Heatman":
                                Heat = True
                                Retry = False
                                break
                            elif posB[x][0] == "Woodman":
                                Offset = 5
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Metalman":
                                Offset = 8
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Crashman":
                                Offset = 17
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Flashman":
                                break
                            elif posB[x][0] == "Sparkman":
                                Offset = 15
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Snakeman":
                                Offset = 14
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Needleman":
                                Offset = 9
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Hardman":
                                Offset = 12
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Topman":
                                Offset = 13
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Geminiman":
                                Offset = 11
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Magnetman":
                                Offset = 10
                                Weak.append(Offset)
                                Retry = False
                                break
                            elif posB[x][0] == "Shadowman":
                                Offset = 16
                                Weak.append(Offset)
                                Retry = False
                                break
                        
            if randomweapons == True:
                    if weapons[Value2] == Cutbyte:
                        Offset = 2 
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Icebyte:
                        Offset = 1
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Firebyte:
                        Offset = 3
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Elecbyte:
                        Offset = 0
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Bubblebyte:
                        Offset = 6
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Airbyte:
                        Offset = 4
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Quickbyte:
                        Offset = 7
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Heatbyte:
                        Heat = True
                        Retry = False
                    elif weapons[Value2] == Woodbyte:
                        Offset = 5
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Metalbyte:
                        Offset = 8
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Crashbyte:
                        Offset = 17
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Sparkbyte:
                        Offset = 15
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Snakebyte:
                        Offset = 14
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Needlebyte:
                        Offset = 9
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Hardbyte:
                        Offset = 12
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Topbyte:
                        Offset = 13
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Geminibyte:
                        Offset = 11
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Magnetbyte:
                        Offset = 10
                        Weak.append(Offset)
                        Retry = False
                    elif weapons[Value2] == Shadowbyte:
                        Offset = 16
                        Weak.append(Offset)
                        Retry = False
                    else:
                        Retry == True
                
        
    if Heat == True: 
        for x in range(3):
            Pointer = Crashwallheat[x] #Writes 1 for each address if Atomic Heat is selected
            Seek = ROM.seek(Pointer, 0)
            ROM.write(b'\x01')

            if MM2 == True:
                Trap1 = Value2
                
            Pointer = Hardwallheat[x]
            Seek = ROM.seek(Pointer, 0)
            ROM.write(b'\x01')
    else:
        Pointer = Crashwall[Offset] #Otherwise, writes a 1 at the address offset
        Seek = ROM.seek(Pointer, 0)
        ROM.write(b'\x01')

        if MM2 == True:
            Trap1 = Value2
            
        Pointer = Hardwall[Offset]
        Seek = ROM.seek(Pointer, 0)
        ROM.write(b'\x01')
        
    Cutweak = [0x6E7D3,0x6E7D4,0x6E7D5,0x6E7D6,0x6E7D7,0x6E7D8,0x6E7D9,0x6E7DA,0x6E7DB,0x6E7DC,
               0x6E7DD,0x6E7DE,0x6E7DF,0x6E7E0,0x6E7E1,0x6E7E2,0x6E7E3,0x6E7E4,0x6E7E5,0x6E7E6,
                0x6E7E7,0x6E7E8,0x6E7E9]
    
    Gutsweak = [0x6E7EF,0x6E7F0,0x6E7F1,0x6E7F2,0x6E7F3,0x6E7F4,0x6E7F5,0x6E7F6,0x6E7F7,0x6E7F8,
                0x6E7F9,0x6E7FA,0x6E7FB,0x6E7FC,0x6E7FD,0x6E7FE,0x6E7FF,0x6E800,0x6E801,0x6E802,
                0x6E803,0x6E804,0x6E805]
    
    Iceweak = [0x6E763,0x6E764,0x6E765,0x6E766,0x6E767,0x6E768,0x6E769,0x6E76A,0x6E76B,0x6E76C,
               0x6E76D,0x6E76E,0x6E76F,0x6E770,0x6E771,0x6E772,0x6E773,0x6E774,0x6E775,0x6E776,
                0x6E777,0x6E778,0x6E779]
    
    Bombweak = [0x6E77F,0x6E780,0x6E781,0x6E782,0x6E783,0x6E784,0x6E785,0x6E786,0x6E787,0x6E788,
                0x6E789,0x6E78A,0x6E78B,0x6E78C,0x6E78D,0x6E78E,0x6E78F,0x6E78F,0x6E790,0x6E791,
                0x6E792,0x6E793,0x6E794]
    
    Fireweak = [0x6E79B,0x6E79C,0x6E79D,0x6E79E,0x6E79F,0x6E7A0,0x6E7A1,0x6E7A2,0x6E7A3,0x6E7A4,
                0x6E7A5,0x6E7A6,0x6E7A7,0x6E7A8,0x6E7A9,0x6E7AA,0x6E7AB,0x6E7AC,0x6E7AD,0x6E7AE,
                0x6E7AF,0x6E7B0,0x6E7B1]
    
    Elecweak = [0x6E7B7,0x6E7B8,0x6E7B9,0x6E7BA,0x6E7BB,0x6E7BC,0x6E7BD,0x6E7BE,0x6E7BF,0x6E7C0,
                0x6E7C1,0x6E7C2,0x6E7C3,0x6E7C4,0x6E7C5,0x6E7C6,0x6E7C7,0x6E7C8,0x6E7C9,0x6E7CA,
                0x6E7CB,0x6E7CC,0x6E7CC]
    

    Bubbleweak = [0x6ECF7,0x6ECF8,0x6ECF9,0x6ECFA,0x6ECFB,0x6ECFC,0x6ECFD,0x6ECFE,0x6ECFF,0x6ED00,
                  0x6ED01,0x6ED02,0x6ED03,0x6ED04,0x6ED05,0x6ED06,0x6ED07,0x6ED08,0x6ED09,0x6ED0A,
                  0x6ED0B,0x6ED0C,0x6ED0D]
    
    Airweak = [0x6EC4F,0x6EC50,0x6EC51,0x6EC52,0x6EC53,0x6EC54,0x6EC55,0x6EC56,0x6EC57,0x6EC58,
               0x6EC59,0x6EC5A,0x6EC5B,0x6EC5C,0x6EC5D,0x6EC5E,0x6EC5F,0x6EC60,0x6EC61,0x6EC62,
               0x6EC63,0x6EC64,0x6EC65]
    
    Quickweak = [0x6ECDB,0x6ECDC,0x6ECDD,0x6ECDE,0x6ECDF,0x6ECE0,0x6ECE1,0x6ECE2,0x6ECE3,0x6ECE4,
                 0x6ECE5,0x6ECE6,0x6ECE7,0x6ECE8,0x6ECE9,0x6ECEA,0x6ECEB,0x6ECEC,0x6ECED,0x6ECEE,
                 0x6ECEF,0x6ECF0,0x6ECF1]
    
    Heatweak = [0x6ED13,0x6ED14,0x6ED15,0x6ED16,0x6ED17,0x6ED18,0x6ED19,0x6ED1A,0x6ED1B,0x6ED1C,
                0x6ED1D,0x6ED1E,0x6ED1F,0x6ED20,0x6ED21,0x6ED22,0x6ED23,0x6ED24,0x6ED25,0x6ED26,
                0x6ED27,0x6ED28,0x6ED29]
    
    Woodweak = [0x6ECA3,0x6ECA4,0x6ECA5,0x6ECA6,0x6ECA7,0x6ECA8,0x6ECA9,0x6ECAA,0x6ECAB,0x6ECAC,
                0x6ECAD,0x6ECAE,0x6ECAF,0x6ECB0,0x6ECB1,0x6ECB2,0x6ECB3,0x6ECB4,0x6ECB5,0x6ECB6,
                0x6ECB7,0x6ECB8,0x6ECB9]
    
    Metalweak = [0x6EC87,0x6EC88,0x6EC89,0x6EC8A,0x6EC8B,0x6EC8C,0x6EC8D,0x6EC8E,0x6EC8F,0x6EC90,
                 0x6EC91,0x6EC92,0x6EC93,0x6EC94,0x6EC95,0x6EC96,0x6EC97,0x6EC98,0x6EC99,0x6EC9A,
                 0x6EC9B,0x6EC9C,0x6EC9D]
    
    Flashweak = [0x6ECBF,0x6ECC0,0x6ECC1,0x6ECC2,0x6ECC3,0x6ECC4,0x6ECC5,0x6ECC6,0x6ECC7,0x6ECC8,
                 0x6ECC9,0x6ECCA,0x6ECCB,0x6ECCC,0x6ECCD,0x6ECCE,0x6ECCF,0x6ECD0,0x6ECD1,0x6ECD2,
                 0x6ECD3,0x6ECD4,0x6ECD5]
    
    Crashweak = [0x6EC6B,0x6EC6C,0x6EC6D,0x6EC6E,0x6EC6F,0x6EC70,0x6EC71,0x6EC72,0x6EC73,0x6EC74,
                 0x6EC75,0x6EC76,0x6EC77,0x6EC78,0x6EC79,0x6EC7A,0x6EC7B,0x6EC7C,0x6EC7D,0x6EC7E,
                 0x6EC7F,0x6EC80,0x6EC81]
    

    Sparkweak = [0x6F253,0x6F254,0x6F255,0x6F256,0x6F257,0x6F258,0x6F259,0x6F25A,0x6F25B,0x6F25C,
                 0x6F25D,0x6F25E,0x6F25F,0x6F260,0x6F261,0x6F262,0x6F263,0x6F264,0x6F265,0x6F266,
                 0x6F267,0x6F268,0x6F269]
    
    Snakeweak = [0x6F21B,0x6F21C,0x6F21D,0x6F21E,0x6F21F,0x6F220,0x6F221,0x6F222,0x6F223,0x6F224,
                 0x6F225,0x6F226,0x6F227,0x6F228,0x6F229,0x6F22A,0x6F22B,0x6F22C,0x6F22D,0x6F22E,
                 0x6F22F,0x6F230,0x6F231]
    
    Needleweak = [0x6F28B,0x6F28C,0x6F28D,0x6F28E,0x6F28F,0x6F290,0x6F291,0x6F292,0x6F293,0x6F294,
                  0x6F295,0x6F296,0x6F297,0x6F298,0x6F299,0x6F29A,0x6F29B,0x6F29C,0x6F29D,0x6F29E,
                  0x6F29F,0x6F2A0,0x6F2A1]
    
    Hardweak = [0x6F1E3,0x6F1E4,0x6F1E5,0x6F1E6,0x6F1E7,0x6F1E8,0x6F1E9,0x6F1EA,0x6F1EB,0x6F1EC,
                0x6F1ED,0x6F1EE,0x6F1EF,0x6F1F0,0x6F1F1,0x6F1F2,0x6F1F3,0x6F1F4,0x6F1F5,0x6F1F6,
                0x6F1F7,0x6F1F8,0x6F1F9]
    
    Topweak = [0x6F1FF,0x6F200,0x6F201,0x6F202,0x6F203,0x6F204,0x6F205,0x6F206,0x6F207,0x6F208,
               0x6F209,0x6F20A,0x6F20B,0x6F20C,0x6F20D,0x6F20E,0x6F20F,0x6F210,0x6F211,0x6F212,
               0x6F213,0x6F214,0x6F215]
    
    Geminiweak = [0x6F2A7,0x6F2A8,0x6F2A9,0x6F2AA,0x6F2AB,0x6F2AC,0x6F2AD,0x6F2AE,0x6F2AF,0x6F2B0,
                  0x6F2B1,0x6F2B2,0x6F2B3,0x6F2B4,0x6F2B5,0x6F2B6,0x6F2B7,0x6F2B8,0x6F2B9,0x6F2BA,
                  0x6F2BB,0x6F2BC,0x6F2BD]
    
    Magnetweak = [0x6F237,0x6F238,0x6F239,0x6F23A,0x6F23B,0x6F23C,0x6F23D,0x6F23E,0x6F23F,0x6F240,
                  0x6F241,0x6F242,0x6F243,0x6F244,0x6F245,0x6F246,0x6F247,0x6F248,0x6F249,0x6F24A,
                  0x6F24B,0x6F24C,0x6F24D]
    
    Shadowweak = [0x6F26F,0x6F270,0x6F271,0x6F272,0x6F273,0x6F274,0x6F275,0x6F276,0x6F277,0x6F278,
                  0x6F279,0x6F27A,0x6F27B,0x6F27C,0x6F27D,0x6F27E,0x6F27F,0x6F280,0x6F281,0x6F282,
                  0x6F283,0x6F284,0x6F285]
    

    DocMWeak = [0x6F2C3,0x6F2C4,0x6F2C5,0x6F2C6,0x6F2C7,0x6F2C8,0x6F2C9,0x6F2CA,0x6F2CB,0x6F2CC,
                0x6F2CD,0x6F2CE,0x6F2CF,0x6F2D0,0x6F2D1,0x6F2D2,0x6F2D3,0x6F2D4,0x6F2D5,0x6F2D6,
                0x6F2D7,0x6F2D8,0x6F2D9] 
     
    DocHWeak = [0x6F777,0x6F778,0x6F779,0x6F77A,0x6F77B,0x6F77C,0x6F77D,0x6F77E,0x6F77F,0x6F780,
                0x6F781,0x6F782,0x6F783,0x6F784,0x6F785,0x6F786,0x6F787,0x6F788,0x6F789,0x6F78A,
                0x6F78B,0x6F78C,0x6F78D]
    
    DocQWeak = [0x6F793,0x6F794,0x6F795,0x6F796,0x6F797,0x6F798,0x6F799,0x6F79A,0x6F79B,0x6F79C,
                0x6F79D,0x6F79E,0x6F79F,0x6F7A0,0x6F7A1,0x6F7A2,0x6F7A3,0x6F7A4,0x6F7A5,0x6F7A6,
                0x6F7A7,0x6F7A8,0x6F7A9]
    
    DocAWeak = [0x6F7AF,0x6F7B0,0x6F7B1,0x6F7B2,0x6F7B3,0x6F7B4,0x6F7B5,0x6F7B6,0x6F7B7,0x6F7B8,
                0x6F7B9,0x6F7BA,0x6F7BB,0x6F7BC,0x6F7BD,0x6F7BE,0x6F7BF,0x6F7C0,0x6F7C1,0x6F7C2,
                0x6F7C3,0x6F7C4,0x6F7C5]
    
    DocCWeak = [0x6F7CB,0x6F7CC,0x6F7CD,0x6F7CE,0x6F7CF,0x6F7D0,0x6F7D1,0x6F7D2,0x6F7D3,0x6F7D4,
                0x6F7D5,0x6F7D6,0x6F7D7,0x6F7D8,0x6F7D9,0x6F7DA,0x6F7DB,0x6F7DC,0x6F7DD,0x6F7DE,
                0x6F7DF,0x6F7E0,0x6F7E1]
    
    DocFWeak = [0x6F7E7,0x6F7E8,0x6F7E9,0x6F7EA,0x6F7EB,0x6F7EC,0x6F7ED,0x6F7EE,0x6F7EF,0x6F7F0,
                0x6F7F1,0x6F7F2,0x6F7F3,0x6F7F4,0x6F7F5,0x6F7F6,0x6F7F7,0x6F7F8,0x6F7F9,0x6F7FA,
                0x6F7FB,0x6F7FC,0x6F7FD]
    
    DocBWeak = [0x6F803,0x6F804,0x6F805,0x6F806,0x6F807,0x6F808,0x6F809,0x6F80A,0x6F80B,0x6F80C,
                0x6F80D,0x6F80E,0x6F80F,0x6F810,0x6F811,0x6F812,0x6F813,0x6F814,0x6F815,0x6F816,
                0x6F817,0x6F818,0x6F819]

    DocWWeak = [0x6F81F,0x6F820,0x6F821,0x6F822,0x6F823,0x6F824,0x6F825,0x6F826,0x6F827,0x6F828,
                0x6F829,0x6F82A,0x6F82B,0x6F82C,0x6F82D,0x6F82E,0x6F82F,0x6F830,0x6F831,0x6F832,
                0x6F833,0x6F834,0x6F835]
    

    KameWeak = [0x6FD43,0x6FD44,0x6FD45,0x6FD46,0x6FD47,0x6FD48,0x6FD49,0x6FD4A,0x6FD4B,0x6FD4C,
                0x6FD4D,0x6FD4E,0x6FD4F,0x6FD50,0x6FD51,0x6FD52,0x6FD53,0x6FD54,0x6FD55,0x6FD56,
                0x6FD57,0x6FD58,0x6FD59]
    
    YellowWeak = [0x6F317,0x6F318,0x6F319,0x6F31A,0x6F31B,0x6F31C,0x6F31D,0x6F31E,0x6F31F,0x6F320,
                    0x6F321,0x6F322,0x6F323,0x6F324,0x6F325,0x6F326,0x6F327,0x6F328,0x6F329,0x6F32A,
                  0x6F32B,0x6F32C,0x6F32D]
    
    MegaWeak = [0x6F75B,0x6F75C,0x6F75D,0x6F75E,0x6F75F,0x6F760,0x6F761,0x6F762,0x6F763,0x6F764,
                0x6F765,0x6F766,0x6F767,0x6F768,0x6F769,0x6F76A,0x6F76B,0x6F76C,0x6F76D,0x6F76E,
                0x6F76F,0x6F770,0x6F771]
    
    Wily31Weak = [0x6F333,0x6F334,0x6F335,0x6F336,0x6F337,0x6F338,0x6F339,0x6F33A,0x6F33B,0x6F33C,
                0x6F33D,0x6F33E,0x6F33F,0x6F340,0x6F341,0x6F342,0x6F343,0x6F344,0x6F345,0x6F346,
                 0x6F347,0x6F348,0x6F349]
    
    Wily32Weak = [0x6F873,0x6F874,0x6F875,0x6F876,0x6F877,0x6F878,0x6F879,0x6F87A,0x6F87B,0x6F87C,
                0x6F87D,0x6F87E,0x6F87F,0x6F880,0x6F881,0x6F882,0x6F883,0x6F884,0x6F885,0x6F886,
                 0x6F887,0x6F888,0x6F889]
    
    Gamma1Weak = [0x6F34F,0x6F350,0x6F351,0x6F352,0x6F353,0x6F354,0x6F355,0x6F356,0x6F357,0x6F358,
                    0x6F359,0x6F35A,0x6F35B,0x6F35C,0x6F35D,0x6F35E,0x6F35F,0x6F360,0x6F361,0x6F362,
                  0x6F363,0x6F364,0x6F365]
    
    Gamma2Weak = [0x6FA6B,0x6FA6C,0x6FA6D,0x6FA6E,0x6FA6F,0x6FA70,0x6FA71,0x6FA72,0x6FA73,0x6FA74,
                    0x6FA75,0x6FA76,0x6FA77,0x6FA78,0x6FA79,0x6FA7A,0x6FA7B,0x6FA7C,0x6FA7D,0x6FA7E,
                  0x6FA7F,0x6FA80,0x6FA81]
    
    BreakmanWeak = [0x6F2DF,0x6F2DE,0x6F2DF,0x6F2E0,0x6F2E1,0x6F2E2,0x6F2E3,0x6F2E4,0x6F2E5,0x6F2E6,
                    0x6F2E7,0x6F2E8,0x6F2E9,0x6F2EA,0x6F2EB,0x6F2EC,0x6F2ED,0x6F2EE,0x6F2EF,0x6F2F0,
                  0x6F2F1,0x6F2F2,0x6F2F3]
    
    MechaDWeak = [0x6ED2F,0x6ED30,0x6ED31,0x6ED32,0x6ED33,0x6ED34,0x6ED35,0x6ED36,0x6ED37,0x6ED38,
                    0x6ED39,0x6ED3A,0x6ED3B,0x6ED3C,0x6ED3D,0x6ED3E,0x6ED3F,0x6ED40,0x6ED41,0x6ED42,
                  0x6ED43,0x6ED44,0x6ED45]
    
    PicoWeak = [0x6FD0B,0x6FD0C,0x6FD0D,0x6FD0E,0x6FD0F,0x6FD10,0x6FD11,0x6FD12,0x6FD13,
                0x6FD14,0x6FD15,0x6FD16,0x6FD17,0x6FD18,0x6FD19,0x6FD1A,0x6FD1B,0x6FD1C,0x6FD1D,
                0x6FD1E,0x6FD1F,0x6FD20,0x6FD21]
    
    GutsTankWeak = [0x6ED67,0x6ED68,0x6ED69,0x6ED6A,0x6ED6B,0x6ED6C,0x6ED6D,0x6ED6E,0x6ED6F,0x6ED70,
                0x6ED71,0x6ED72,0x6ED73,0x6ED74,0x6ED75,0x6ED76,0x6ED77,0x6ED78,0x6ED79,0x6ED7A,
                 0x6ED7B,0x6ED7C,0x6ED7D]

    TrapWeak = [0x6ED83,0x6ED84,0x6ED85,0x6ED86,0x6ED87,0x6ED88,0x6ED89,0x6ED8A,0x6ED8B,0x6ED8C,
                0x6ED8D,0x6ED8E,0x6ED8F,0x6ED90,0x6ED91,0x6ED92,0x6ED93,0x6ED94,0x6ED95,0x6ED96,
                 0x6ED97,0x6ED98,0x6ED99]
    
    Wily21Weak = [0x6ED9F,0x6EDA0,0x6EDA1,0x6EDA2,0x6EDA3,0x6EDA4,0x6EDA5,0x6EDA6,0x6EDA7,0x6EDA8,
                    0x6EDA9,0x6EDAA,0x6EDAB,0x6EDAC,0x6EDAD,0x6EDAE,0x6EDAF,0x6EDB0,0x6EDB1,0x6EDB2,
                  0x6EDB3,0x6EDB4,0x6EDB5]
    
    AlienWeak = [0x6EDBB,0x6EDBC,0x6EDBD,0x6EDBE,0x6EDBF,0x6EDC0,0x6EDC1,0x6EDC2,0x6EDC3,
                    0x6EDC4,0x6EDC5,0x6EDC6,0x6EDC7,0x6EDC8,0x6EDC9,0x6EDCA,0x6EDCB,0x6EDCC,0x6EDCD,
                  0x6EDCE,0x6EDCF,0x6EDD0,0x6EDD1]

    Pointers = [0x85810,0x85820,0x85830,0x85840,0x85850,0x85860,0x85870,0x85880,
                0x85890,0x858A0,0x858B0,0x858C0,0x858D0,0x858E0,0x858F0,0x85900,
                0x85910,0x85920,0x85930,0x85940,0x85950,0x85960,0x85970,0x85A20,0x85A28]

    Boss = []
    Weak2 = []
    Atomic = 9
    Crash = 9
    Flash = 9
    Weak.clear()
    if Vanilla == True: #!
       for x in range(8):
            if pos[x][1] == x: #Seeing which boss is encountered
                if pos[x][0] == "Bombman":
                    Offset = 0
                    Weak.append(Offset)
                    Weak2.append(Bombweak)
                elif pos[x][0] == "Elecman":
                    Offset = 1
                    Weak.append(Offset)
                    Weak2.append(Elecweak)
                elif pos[x][0] == "Gutsman":
                    Offset = 2
                    Weak.append(Offset)
                    Weak2.append(Gutsweak)
                elif pos[x][0] == "Iceman":
                    Offset = 3
                    Weak.append(Offset)
                    Weak2.append(Iceweak)
                elif pos[x][0] == "Cutman":
                    Offset = 4
                    Weak.append(Offset)
                    Weak2.append(Cutweak)
                elif pos[x][0] == "Fireman":
                    Offset = 5
                    Weak.append(Offset)
                    Weak2.append(Fireweak)
                elif pos[x][0] == "Heatman":
                    Offset = 6
                    Weak.append(Offset)
                    Weak2.append(Heatweak)
                    Atomic = x
                elif pos[x][0] == "Airman":
                    Offset = 7
                    Weak.append(Offset)
                    Weak2.append(Airweak)
                elif pos[x][0] == "Woodman":
                    Offset = 8
                    Weak.append(Offset)
                    Weak2.append(Woodweak)
                elif pos[x][0] == "Bubbleman":
                    Offset = 9
                    Weak.append(Offset)
                    Weak2.append(Bubbleweak)
                elif pos[x][0] == "Quickman":
                    Offset = 10
                    Weak.append(Offset)
                    Weak2.append(Quickweak)
                elif pos[x][0] == "Flashman":
                    Flash = x
                    Offset = 11
                    Weak.append(Offset)
                    Weak2.append(Flashweak)
                elif pos[x][0] == "Metalman":
                    Offset = 12
                    Weak.append(Offset)
                    Weak2.append(Metalweak)
                elif pos[x][0] == "Crashman":
                    Offset = 13
                    Weak.append(Offset)
                    Weak2.append(Crashweak)
                    Crash = x
                elif pos[x][0] == "Needleman":
                    Offset = 14
                    Weak.append(Offset)
                    Weak2.append(Needleweak)
                elif pos[x][0] == "Magnetman":
                    Offset = 15
                    Weak.append(Offset)
                    Weak2.append(Magnetweak)
                elif pos[x][0] == "Geminiman":
                    Offset = 16
                    Weak.append(Offset)
                    Weak2.append(Geminiweak)
                elif pos[x][0] == "Hardman":
                    Offset = 17
                    Weak.append(Offset)
                    Weak2.append(Hardweak)
                elif pos[x][0] == "Topman":
                    Offset = 18
                    Weak.append(Offset)
                    Weak2.append(Topweak)
                elif pos[x][0] == "Snakeman":
                    Offset = 19
                    Weak.append(Offset)
                    Weak2.append(Snakeweak)
                elif pos[x][0] == "Sparkman":
                    Offset = 20
                    Weak.append(Offset)
                    Weak2.append(Sparkweak)
                elif pos[x][0] == "Shadowman":
                    Offset = 21
                    Weak.append(Offset)
                    Weak2.append(Shadowweak)

    if randomboss == True:  #!             
        for x in range(8):
            if posB[x][1] == x: #Seeing which boss is encountered
                if posB[x][0] == "Bombman":
                    Offset = 0
                    Weak.append(Offset)
                    Weak2.append(Bombweak)
                elif posB[x][0] == "Elecman":
                    Offset = 1
                    Weak.append(Offset)
                    Weak2.append(Elecweak)
                elif posB[x][0] == "Gutsman":
                    Offset = 2
                    Weak.append(Offset)
                    Weak2.append(Gutsweak)
                elif posB[x][0] == "Iceman":
                    Offset = 3
                    Weak.append(Offset)
                    Weak2.append(Iceweak)
                elif posB[x][0] == "Cutman":
                    Offset = 4
                    Weak.append(Offset)
                    Weak2.append(Cutweak)
                elif posB[x][0] == "Fireman":
                    Offset = 5
                    Weak.append(Offset)
                    Weak2.append(Fireweak)
                elif posB[x][0] == "Heatman":
                    Offset = 6
                    Weak.append(Offset)
                    Weak2.append(Heatweak)
                    Atomic = x
                elif posB[x][0] == "Airman":
                    Offset = 7
                    Weak.append(Offset)
                    Weak2.append(Airweak)
                elif posB[x][0] == "Woodman":
                    Offset = 8
                    Weak.append(Offset)
                    Weak2.append(Woodweak)
                elif posB[x][0] == "Bubbleman":
                    Offset = 9
                    Weak.append(Offset)
                    Weak2.append(Bubbleweak)
                elif posB[x][0] == "Quickman":
                    Offset = 10
                    Weak.append(Offset)
                    Weak2.append(Quickweak)
                elif posB[x][0] == "Flashman":
                    Flash = x
                    Offset = 11
                    Weak.append(Offset)
                    Weak2.append(Flashweak)
                elif posB[x][0] == "Metalman":
                    Offset = 12
                    Weak.append(Offset)
                    Weak2.append(Metalweak)
                elif posB[x][0] == "Crashman":
                    Offset = 13
                    Weak.append(Offset)
                    Weak2.append(Crashweak)
                    Crash = x
                elif posB[x][0] == "Needleman":
                    Offset = 14
                    Weak.append(Offset)
                    Weak2.append(Needleweak)
                elif posB[x][0] == "Magnetman":
                    Offset = 15
                    Weak.append(Offset)
                    Weak2.append(Magnetweak)
                elif posB[x][0] == "Geminiman":
                    Offset = 16
                    Weak.append(Offset)
                    Weak2.append(Geminiweak)
                elif posB[x][0] == "Hardman":
                    Offset = 17
                    Weak.append(Offset)
                    Weak2.append(Hardweak)
                elif posB[x][0] == "Topman":
                    Offset = 18
                    Weak.append(Offset)
                    Weak2.append(Topweak)
                elif posB[x][0] == "Snakeman":
                    Offset = 19
                    Weak.append(Offset)
                    Weak2.append(Snakeweak)
                elif posB[x][0] == "Sparkman":
                    Offset = 20
                    Weak.append(Offset)
                    Weak2.append(Sparkweak)
                elif posB[x][0] == "Shadowman":
                    Offset = 21
                    Weak.append(Offset)
                    Weak2.append(Shadowweak)
                    
    if randomweapons == True: #!
        Weak.clear()
        #Selects which weapons were randomly generated and assigns an offset
        for x in range(8):
            if weapons[x] == Bombbyte:
                Offset = 0
                Weak.append(Offset)
            elif weapons[x] == Elecbyte:
                Offset = 1
                Weak.append(Offset)
            elif weapons[x] == Gutsbyte:
                Offset = 2
                Weak.append(Offset)
            elif weapons[x] == Icebyte:
                Offset = 3
                Weak.append(Offset)
            elif weapons[x] == Cutbyte:
                Offset = 4
                Weak.append(Offset)
            elif weapons[x] == Firebyte:
                Offset = 5
                Weak.append(Offset)
            elif weapons[x] == Heatbyte:
                Offset = 6
                Weak.append(Offset)
                Atomic = x
            elif weapons[x] == Airbyte:
                Offset = 7
                Weak.append(Offset)
            elif weapons[x] == Woodbyte:
                Offset = 8
                Weak.append(Offset)
            elif weapons[x] == Bubblebyte:
                Offset = 9
                Weak.append(Offset)
            elif weapons[x] == Quickbyte:
                Offset = 10
                Weak.append(Offset)
            elif weapons[x] == Flashbyte:
                Flash = x
                Offset = 11
                Weak.append(Offset)
            elif weapons[x] == Metalbyte:
                Offset = 12
                Weak.append(Offset)
            elif weapons[x] == Crashbyte:
                Offset = 13
                Weak.append(Offset)
                Crash = x
            elif weapons[x] == Needlebyte:
                Offset = 14
                Weak.append(Offset)
            elif weapons[x] == Magnetbyte:
                Offset = 15
                Weak.append(Offset)
            elif weapons[x] == Geminibyte:
                Offset = 16
                Weak.append(Offset)
            elif weapons[x] == Hardbyte:
                Offset = 17
                Weak.append(Offset)
            elif weapons[x] == Topbyte:
                Offset = 18
                Weak.append(Offset)
            elif weapons[x] == Snakebyte:
                Offset = 19
                Weak.append(Offset)
            elif weapons[x] == Sparkbyte:
                Offset = 20
                Weak.append(Offset)
            elif weapons[x] == Shadowbyte:
                Offset = 21
                Weak.append(Offset)
                
#Seeing which boss is encountered
        if randomboss == False:
            for x in range(8):
               if pos[x][1] == x: 
                    if pos[x][0] == "Bombman":
                        Weak2.append(Bombweak)
                    elif pos[x][0] == "Elecman":
                        Weak2.append(Elecweak)
                    elif pos[x][0] == "Gutsman":
                        Weak2.append(Gutsweak)
                    elif pos[x][0] == "Iceman":
                        Weak2.append(Iceweak)
                    elif pos[x][0] == "Cutman":
                        Weak2.append(Cutweak)
                    elif pos[x][0] == "Fireman":
                        Weak2.append(Fireweak)
                    elif pos[x][0] == "Heatman":
                        Weak2.append(Heatweak)
                    elif pos[x][0] == "Airman":
                        Weak2.append(Airweak)
                    elif pos[x][0] == "Woodman":
                        Weak2.append(Woodweak)
                    elif pos[x][0] == "Bubbleman":
                        Weak2.append(Bubbleweak)
                    elif pos[x][0] == "Quickman":
                        Weak2.append(Quickweak)
                    elif pos[x][0] == "Flashman":
                        Weak2.append(Flashweak)
                    elif pos[x][0] == "Metalman":
                        Weak2.append(Metalweak)
                    elif pos[x][0] == "Crashman":
                        Weak2.append(Crashweak)
                    elif pos[x][0] == "Needleman":
                        Weak2.append(Needleweak)
                    elif pos[x][0] == "Magnetman":
                        Weak2.append(Magnetweak)
                    elif pos[x][0] == "Geminiman":
                        Weak2.append(Geminiweak)
                    elif pos[x][0] == "Hardman":
                        Weak2.append(Hardweak)
                    elif pos[x][0] == "Topman":
                        Weak2.append(Topweak)
                    elif pos[x][0] == "Snakeman":
                        Weak2.append(Snakeweak)
                    elif pos[x][0] == "Sparkman":
                        Weak2.append(Sparkweak)
                    elif pos[x][0] == "Shadowman":
                        Weak2.append(Shadowweak)
                        
    if MM3 == True:                    
        Weak2.append(DocMWeak)
        Weak2.append(DocHWeak)
        Weak2.append(DocQWeak)
        Weak2.append(DocAWeak)
        Weak2.append(DocCWeak)
        Weak2.append(DocFWeak)
        Weak2.append(DocBWeak)
        Weak2.append(DocWWeak)

        Weak2.append(KameWeak)
        Weak2.append(YellowWeak)
        Weak2.append(MegaWeak)
        Weak2.append(Wily31Weak)
        Weak2.append(Wily32Weak)
        Weak2.append(Gamma1Weak)
        Weak2.append(Gamma2Weak)

    elif MM2 == True:
        Weak2.append(MechaDWeak)
        Weak2.append(PicoWeak)
        Weak2.append(GutsTankWeak)
        Weak2.append(TrapWeak)
        Weak2.append(Wily21Weak)
        Weak2.append(AlienWeak)

    #!Writing weakness values for Trap and Alien bosses
        Pointer = 0x85981 #Gets random value from addresses
        Seek = ROM.seek(Pointer,0)
        Weakness2 = ROM.read(1)
        Pointer+=1
        Weakness3 = ROM.read(1)
        Pointer+=1
        Weakness4 = ROM.read(1)
        Trap2 = int.from_bytes(Weakness2, "big")
        Alien1 = int.from_bytes(Weakness3, "big")
        Alien2 = int.from_bytes(Weakness4, "big")
        Trap2 -= 1 #Offset to change 1-8 from randomizer to 0-7 for pos
        Alien1 -= 1
        Alien2 -= 1
        FlagW = b'\x06'
        FlagW2 = b'\x02'
        EFlag = b'\x82'
        if Trap1 == Trap2: #If values are same, assign different random number
            if Trap1 == 3:
                Trap2 += 2
            elif Trap1 != 3:
                Trap2 = 3
        if Alien1 == Alien2:
            if Alien1 == 5:
                Alien2 = 1
            elif Alien1 != 5:
                Alien2 = 5
        if Vanilla == True: #Checking to see if Values correspond to Time Stopper
            if pos[Trap2][0] == "Flashman":
                Trap2 += 1
                if Trap1 == Trap2:
                    if Trap1 != 7:
                        Trap2 += 1
                    elif Trap1 == 7:
                        Trap2 -= 2
            if pos[Alien1][0] == "Flashman":
                Alien1 += 1
                if Alien1 == Alien2:
                    if Alien2 != 7:
                        Alien1 += 1
                    elif Alien2 == 7:
                        Alien1 -= 2
            if pos[Alien2][0] == "Flashman":
                Alien2 += 1
                if Alien1 == Alien2:
                    if Alien1 != 7:
                        Alien2 += 1
                    elif Alien1 == 7:
                        Alien2 -= 2    
        elif randomweapons == True:
            if Trap2 == TimeS:
                Trap2 += 1
                if Trap1 == Trap2:
                    if Trap1 != 7:
                        Trap2 += 1
                    elif Trap1 == 7:
                        Trap2 -= 2
            if Alien1 == TimeS:
                Alien1 += 1
                if Alien1 == Alien2:
                    if Alien2 != 7:
                        Alien1 += 1
                    elif Alien2 == 7:
                        Alien1 -= 2
            if Alien2 == TimeS:
                Alien2 += 1
                if Alien1 == Alien2:
                    if Alien1 != 7:
                        Alien2 += 1
                    elif Alien1 == 7:
                        Alien2 -= 2
                        
        Pointer = 0x6EDC4 #Set initial weakness values to null
        Seek = ROM.seek(Pointer,0)
        ROM.write(b'\x82')
        Pointer = 0x6ED90
        Seek = ROM.seek(Pointer,0)
        ROM.write(b'\x82')
        Pointer += 11
        Seek = ROM.seek(Pointer,0)
        ROM.write(b'\x82')
        
        Pointer = 0x85A20 #Write values to ROM based on random values
        Seek = ROM.seek(Pointer,0)
        for x in range(8):
            if x == Trap1:
                ROM.write(FlagW)
            elif x == Trap2:
                ROM.write(FlagW)
            else:
                ROM.write(EFlag)
            Pointer += 1
        for x in range(8):
            if x == Alien1:
                ROM.write(FlagW2)
            elif x == Alien2:
                ROM.write(FlagW2)
            else:
                ROM.write(EFlag)
            Pointer += 1             
        
    CByte = b'\x07'
    FByte = b'\x83'
    TimeS2 = 9
    if MM3 == True:
        z = 23
    elif MM2 == True:
        z = 14
    for y in range(z): #!
        #Getting randomly generated weakness values
        Pointer = Pointers[y]
        if MM2 == True:
            if y == 8:
                Pointer = Pointers[22]# Mecha Dragon uses Gamma 2 weakness
            if y == 9:
                Pointer = Pointers[16] # Pico uses Kamegoro weakness
            elif y == 10:
                Pointer = Pointers[8] # GutsTank uses Doc 1/Metal weakness
            elif y == 11:
                Pointer = Pointers[23] # Trap uses custom weakness
            elif y == 12:
                Pointer = Pointers[9] # Wily Machine 2 uses Doc2/Heat weakness
            elif y == 13:
                Pointer = Pointers[24] # Alien uses custom weakness
        for x in range(8):
                Seek = ROM.seek(Pointer,0)
                Byte = ROM.read(1)
                Boss.append(Byte)
                Pointer += 1
                
        if Flashman == True:
            for x in range(8):
                if pos[x][0] == "Flashman":
                    TimeS2 = x
                    break
                    
        Check = Boss.count(7)
        for x in range(8): 
                Order = Weak[x] #Checks to see if boss is weak to its own weapon. If so, trades the value with another weapon
                if Check == 1:
                    if Boss[x] == CByte:
                        Boss.pop(x)
                        if x == 5:
                            Boss.insert(4, CByte)
                        else:
                            Boss.insert(5, CByte)
                            
                if randomweapons == True: #Finds which position flashman's weapon is in if he is a boss. If so, swaps the value the randomizer produces for the correct value.    
                    if TimeS == x:
                        Boss.pop(x)
                        Boss.insert(x, FByte)

                if Vanilla == True:
                    if TimeS2 == x:
                        Boss.pop(x)
                        Boss.insert(x, FByte)
                    
                Value = Boss[x]
                if Atomic == x:
                    FlagA = b'\x82' #No damage, (1:2:4), 2:4:7, or 4:6:9 are possible values to write
                    FlagA2 = b'\x01'
                    FlagC = b'\x02'
                    FlagC2 = b'\x04'
                    FlagD = b'\x07'
                    PointerB = Weak2[y][22]
                    if Value == FlagA:
                        Value2 = b'\x82'
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)
                        PointerB += 1
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)

                    elif Value == FlagA2:
                        Value = b'\x82'
                        Value2 = b'\x82'
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)
                        PointerB += 1
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)

                    elif Value == FlagC:
                        Value = b'\x02'
                        Value2 = b'\x04'
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)
                        PointerB += 1
                        Value2 = b'\x07'
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)

                    elif Value == FlagC2:
                        Value = b'\x02'
                        Value2 = b'\x04'
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)
                        PointerB += 1
                        Value2 = b'\x07'
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)

                    elif Value == FlagD:
                        Value = b'\x04'
                        Value2 = b'\x06'
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)
                        PointerB += 1
                        Value2 = b'\x09'
                        Seek = ROM.seek(PointerB,0)
                        ROM.write(Value2)
                        
                PointerB = Weak2[y][Order]
                Seek = ROM.seek(PointerB,0)
                ROM.write(Value) #Writes value from Boss
                if Crash == x:
                    Offset = Weak2[y][22] #Writes same value if position is correct for Crash bomb
                    PointerB = Offset + 2
                    Seek = ROM.seek(PointerB, 0)
                    ROM.write(Value)
                
        Boss.clear()

    busters = [] #!If user wants random buster damage, write values generated to address
    if randombuster == True:
        Pointer = 0x859C0
        Seek = ROM.seek(Pointer, 0)
        for x in range(8):
            Value = ROM.read(1)
            busters.append(Value)
            Pointer += 1
    
        if Vanilla == True:
            for x in range(8):
                if pos[x][0] == "Cutman":
                    Pointer = 0x6E7D2
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Gutsman":
                    Pointer = 0x6E7EE
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Iceman":
                    Pointer = 0x6E762
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Bombman":
                    Pointer = 0x6E77E
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Fireman":
                    Pointer = 0x6E79A
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Elecman":
                    Pointer = 0x6E7B6
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Bubbleman":
                    Pointer = 0x6ECF6
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Airman":
                    Pointer = 0x6EC4E
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Quickman":
                    Pointer = 0x6ECDA
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Heatman":
                    Pointer = 0x6ED12
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Woodman":
                    Pointer = 0x6ECA2
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Metalman":
                    Pointer = 0x6EC86
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Flashman":
                    Pointer = 0x6ECBE
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Crashman":
                    Pointer = 0x6EC6A
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Sparkman":
                    Pointer = 0x6F252
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Snakeman":
                    Pointer = 0x6F21A
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Needleman":
                    Pointer = 0x6F28A
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Hardman":
                    Pointer = 0x6F1E2
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Topman":
                    Pointer = 0x6F1FE
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Geminiman":
                    Pointer = 0x6F2A6
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Magnetman":
                    Pointer = 0x6F236
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif pos[x][0] == "Shadowman":
                    Pointer = 0x6F26E
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                    
        elif randomboss == True:
            for x in range(8):
                if posB[x][0] == "Cutman":
                    Pointer = 0x6E7D2
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Gutsman":
                    Pointer = 0x6E7EE
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Iceman":
                    Pointer = 0x6E762
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Bombman":
                    Pointer = 0x6E77E
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Fireman":
                    Pointer = 0x6E79A
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Elecman":
                    Pointer = 0x6E7B6
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Bubbleman":
                    Pointer = 0x6ECF6
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Airman":
                    Pointer = 0x6EC4E
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Quickman":
                    Pointer = 0x6ECDA
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Heatman":
                    Pointer = 0x6ED12
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Woodman":
                    Pointer = 0x6ECA2
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Metalman":
                    Pointer = 0x6EC86
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Flashman":
                    Pointer = 0x6ECBE
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Crashman":
                    Pointer = 0x6EC6A
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Sparkman":
                    Pointer = 0x6F252
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Snakeman":
                    Pointer = 0x6F21A
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Needleman":
                    Pointer = 0x6F28A
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Hardman":
                    Pointer = 0x6F1E2
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Topman":
                    Pointer = 0x6F1FE
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Geminiman":
                    Pointer = 0x6F2A6
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Magnetman":
                    Pointer = 0x6F236
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                elif posB[x][0] == "Shadowman":
                    Pointer = 0x6F26E
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(busters[x])
                    
    collision = []
    collision2 = []
    collision2a = [0x6F2C1,0x6F775,0x6F791,0x6F7AD,0x6F7C9,0x6F7E5,0x6F801,0x6F81D,0x6F2DD,0x6FD41,
                   0x6F315,0x6F759,0x6F331,0x6F871]
    collision2b = [0x6FD09,0x6ED65,0x6ED9D,0x6EDB9]
    weapondamage = []
    weapondamage2 = []
    weapondamage3 = []
    weapondamage3a = [0x7E85,0x70265,0x5693F,0x705AD]
    weapondamage3b = [0x7022D,0x70051,0x6ED81,0x70265,0x70281,0x7029D]
    if randomdamage == True: #! If user wants random damage, write values to address
        Pointer = 0x859D0
        Seek = ROM.seek(Pointer, 0)
        for x in range(8):
            Value = ROM.read(1)
            collision.append(Value)
            Pointer += 1
        for x in range(14):
            Value = ROM.read(1)
            collision2.append(Value)
            Pointer += 1
            
        Pointer = 0x859F0
        Seek = ROM.seek(Pointer, 0)
        for x in range(8):
            Value = ROM.read(1)
            weapondamage.append(Value)
            Pointer += 1
        if MM3 == True:
            for x in range(7):
                Value = ROM.read(1)
                weapondamage2.append(Value)
                Pointer += 1
            x = 4
        if MM2 == True:
            Pointer = 0x85A03
            Seek = ROM.seek(Pointer,0)
            x = 6
        for x in range(x):
            Value = ROM.read(1)
            weapondamage3.append(Value)
            Pointer += 1
        if Vanilla == True: #Writing values on if boss collides into megaman
            for x in range(8):
                if pos[x][0] == "Cutman":
                    Pointer = 0x6E7D1
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Gutsman":
                    Pointer = 0x6E7ED
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Iceman":
                    Pointer = 0x6E761
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Bombman":
                    Pointer = 0x6E77D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Fireman":
                    Pointer = 0x6E799
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Elecman":
                    Pointer = 0x6E7B5
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Bubbleman":
                    Pointer = 0x6ECF5
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Airman":
                    Pointer = 0x6EC4D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Quickman":
                    Pointer = 0x6ECD9
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Heatman":
                    Pointer = 0x6ED11
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Woodman":
                    Pointer = 0x6ECA1
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Metalman":
                    Pointer = 0x6EC85
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Flashman":
                    Pointer = 0x6ECBD
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Crashman":
                    Pointer = 0x6EC6B
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Sparkman":
                    Pointer = 0x6F251
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Snakeman":
                    Pointer = 0x6F219
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Needleman":
                    Pointer = 0x6F289
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Hardman":
                    Pointer = 0x6F1E1
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Topman":
                    Pointer = 0x6F1FD
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Geminiman":
                    Pointer = 0x6F2A5
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Magnetman":
                    Pointer = 0x6F235
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif pos[x][0] == "Shadowman":
                    Pointer = 0x6F26D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                    
        elif randomboss == True:
            for x in range(8):
                if posB[x][0] == "Cutman":
                    Pointer = 0x6E7D1
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Gutsman":
                    Pointer = 0x6E7ED
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Iceman":
                    Pointer = 0x6E761
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Bombman":
                    Pointer = 0x6E77D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Fireman":
                    Pointer = 0x6E799
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Elecman":
                    Pointer = 0x6E7B5
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Bubbleman":
                    Pointer = 0x6ECF5
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Airman":
                    Pointer = 0x6EC4D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Quickman":
                    Pointer = 0x6ECD9
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Heatman":
                    Pointer = 0x6ED11
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Woodman":
                    Pointer = 0x6ECA1
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Metalman":
                    Pointer = 0x6EC85
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Flashman":
                    Pointer = 0x6ECBD
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Crashman":
                    Pointer = 0x6EC69
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Sparkman":
                    Pointer = 0x6F251
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Snakeman":
                    Pointer = 0x6F219
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Needleman":
                    Pointer = 0x6F289
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Hardman":
                    Pointer = 0x6F1E1
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Topman":
                    Pointer = 0x6F1FD
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Geminiman":
                    Pointer = 0x6F2A5
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Magnetman":
                    Pointer = 0x6F235
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                elif posB[x][0] == "Shadowman":
                    Pointer = 0x6F26D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(collision[x])
                    
        if MM3 == True:            
            for x in range(14):
               Pointer = collision2a[x]
               Seek = ROM.seek(Pointer, 0)
               ROM.write(collision2[x])

        if MM2 == True:
            Pointer = collision2b[0] # Pico uses Doc Metal collision
            Seek = ROM.seek(Pointer, 0)
            ROM.write(collision2[0])

            Pointer = collision2b[1] # Guts Tank uses Holograph Megamans
            Seek = ROM.seek(Pointer, 0)
            ROM.write(collision2[11])

            Pointer = collision2b[2] # Wily Machine 2 uses Wily Machine 3
            Seek = ROM.seek(Pointer, 0)
            ROM.write(collision2[12])

            Pointer = collision2b[3] # Alien uses Yellow Devil
            Seek = ROM.seek(Pointer, 0)
            ROM.write(collision2[10])
           
        skipA = False
        skipB = False
        skipQ = False
        skipH = False
        skipW = False
        skipM = False
        skipC = False
        if Vanilla == True: #!Writing values to weapon boss uses against megaman
            for x in range(8):
                if pos[x][0] == "Cutman":
                    Pointer = 0x6FFFD
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Gutsman":
                    Pointer = 0x6F679
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Iceman":
                    Pointer = 0x6FF71
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Bombman":
                    Pointer = 0x6FF8D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Fireman":
                    Pointer = 0x6FFA9
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Elecman":
                    Pointer = 0x6FFE1
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Bubbleman":
                    Pointer = 0x701D9
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipB = True
                elif pos[x][0] == "Airman":
                    Pointer = 0x70115
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipA = True
                elif pos[x][0] == "Quickman":
                    Pointer = 0x701BD
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipQ = True
                elif pos[x][0] == "Heatman":
                    Pointer = 0x70211
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipH = True
                elif pos[x][0] == "Woodman":
                    Pointer = 0x70185 #Leaf Shield Damage only
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipW = True
                elif pos[x][0] == "Metalman":
                    Pointer = 0x70169
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipM = True
                elif pos[x][0] == "Flashman":
                    Pointer = 0x85A04 #Flashman, Breakman, and Holographs all share same damage value
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Crashman":
                    Pointer = 0x70131
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipC = True
                elif pos[x][0] == "Sparkman":
                    Pointer = 0x703D0
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Snakeman":
                    Pointer = 0x70399
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Needleman":
                    Pointer = 0x70425
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Hardman":
                    Pointer = 0x70345
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Topman":
                    Pointer = 0x7037D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Geminiman":
                    Pointer = 0x7045D #Gemini Laser only
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Magnetman":
                    Pointer = 0x703B5
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif pos[x][0] == "Shadowman":
                    Pointer = 0x70409
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    
        elif randomboss == True:
            for x in range(8):
                if posB[x][0] == "Cutman":
                    Pointer = 0x6FFFD
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Gutsman":
                    Pointer = 0x6F679
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Iceman":
                    Pointer = 0x6FF71
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Bombman":
                    Pointer = 0x6FF8D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Fireman":
                    Pointer = 0x6FFA9
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Elecman":
                    Pointer = 0x6FFE1
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Bubbleman":
                    Pointer = 0x701D9
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipB = True
                elif posB[x][0] == "Airman":
                    Pointer = 0x70115
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipA = True
                elif posB[x][0] == "Quickman":
                    Pointer = 0x701BD
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipQ = True
                elif posB[x][0] == "Heatman":
                    Pointer = 0x70211
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipH = True
                elif posB[x][0] == "Woodman":
                    Pointer = 0x70185
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipW = True
                elif posB[x][0] == "Metalman":
                    Pointer = 0x70169
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipM = True
                elif posB[x][0] == "Flashman":
                    Pointer = 0x85A05
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Crashman":
                    Pointer = 0x70131
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                    skipC = True
                elif posB[x][0] == "Sparkman":
                    Pointer = 0x703D0
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Snakeman":
                    Pointer = 0x70399
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Needleman":
                    Pointer = 0x70425
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Hardman":
                    Pointer = 0x70345
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Topman":
                    Pointer = 0x7037D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Geminiman":
                    Pointer = 0x7045D
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Magnetman":
                    Pointer = 0x703B5
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
                elif posB[x][0] == "Shadowman":
                    Pointer = 0x70409
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(weapondamage[x])
        if MM3 == True:           
            if skipB == False:
                Pointer = 0x701D9
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage2[5])
                
            if skipA == False:
                Pointer = 0x70115
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage2[3])
                
            if skipQ == False:
                Pointer = 0x701BD
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage2[2])
                
            if skipH == False:
                Pointer = 0x70211
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage2[1])
                
            if skipW == False:
                Pointer = 0x70185
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage2[6])
                
            if skipM == False:
                Pointer = 0x70169
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage2[0])
                
            if skipC == False:
                Pointer = 0x70131
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage2[4])

            for x in range(4):
                Pointer = weapondamage3a[x]
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage3[x])

        if MM2 == True:
            for x in range(6):
                Pointer = weapondamage3b[x]
                Seek = ROM.seek(Pointer, 0)
                ROM.write(weapondamage3[x])
                
            
    #!Start of Arena modification section
    FlatF = False
    FlatQ = False
    FlatSp = False
    FlatSn = False
    ElecS = False
    Adjust = False
    ValueF = 8
    ValueQ = 8
    ValueSp = 8
    ValueSn = 8
    ValueE = 8
    FlatFPointer = [0x123B9B,0x123BA3,0x123BA4,0x123BA9,0x123BAA,0x123BAB,0x123BB1,0x123BB2,0x123BB3,0x123BB4,
                    0x123BB7,0x123BB8,0x123BB9,0x123BBA,0x123BBB,0x123BBD,0x123BBE,0x123BBF,0x123BC0,0x123BC1,
                    0x123BC2,0x123BC3,0x123BC4,0x123BC8,0x123BCA,0x123BCB,0x123BCE,0x123BCF,0x79C9F]
    FlatFValue = [b'\x05',b'\x00',b'\x00',b'\x26',b'\x4D',b'\x13',b'\x26',b'\x69',b'\x00',b'\x00',b'\x26',b'\x69',
                  b'\x00',b'\x67',b'\x14',b'\x11',b'\x03',b'\x02',b'\x02',b'\x12',b'\x11',b'\x11',b'\x05',b'\x11',
                  b'\x11',b'\x06',b'\x12',b'\x05',b'\xA4']
    FlatQPointer = [0x114A33,0x114A34,0x114A37,0x114A38,0x114A39,0x114A3A,0x114A3E,0x114A3F,0x114A40,0x114A41,
                    0x114A42,0x114A43,0x114A44,0x114A47,0x114A48,0x114A49,0x114A4A,0x114A4B,0x114A4C,0x114A4D,
                    0x114A4E,0x114A4F,0x114A50,0x114A51,0x114A54,0x114A57,0x114A5A,0x114A5B,0x114A5C,0x114A5D]
    FlatQValue = [b'\xD5',b'\xBF',b'\xBD',b'\xC0',b'\xBE',b'\xBF',b'\x60',b'\x61',b'\x61',b'\x61',b'\x61',b'\x61',
                  b'\x44',b'\x43',b'\x61',b'\x61',b'\x61',b'\x61',b'\x61',b'\x62',b'\x51',b'\x51',b'\x51',b'\x51',
                  b'\x60',b'\x62',b'\x51',b'\x51',b'\x51',b'\x51']
    FlatSpPointer = [0x1434F7,0x1434F8,0x143507,0x143508,0x143515,0x143516,0x143517,0x143518,0x143519,0x14351A,
                     0x143525,0x14352A,0x14352B,0x14352C,0x14352D,0x14352E,0x14352F,0x14353A,0x14353B,0x14353C,
                     0x14353D,0x14353E,0x14353F,0x14354C,0x14354D,0x14354E,0x14354F,0x14355D,0x14355E]
    FlatSpValue = [b'\x65',b'\x65',b'\x65',b'\x65',b'\x65',b'\x65',b'\x65',b'\x65',b'\x65',b'\x65',b'\x1B',b'\x1B',b'\x1B',b'\x1B'
                  b'\x1B',b'\x1B',b'\x1B',b'\x35',b'\x2A',b'\x39',b'\x47',b'\x48',b'\x49',b'\x4A',b'\x2F',b'\x12',b'\x13',
                  b'\x32',b'\x52',b'\x53']
    FlatSnPointer = [0x148847,0x148848,0x148857,0x148858,0x148865,0x148866,0x148867,0x148868,0x148869,0x14886A,
                     0x148875,0x148877,0x148878,0x14887A,0x148885,0x148887,0x14888A]
    FlatSnValue = [b'\x00',b'\x00',b'\x00',b'\x00',b'\x3A',b'\x1A',b'\x1A',b'\x1A',b'\x1A',b'\x3B',b'\x19',b'\x09',b'\x09',
                  b'\x19',b'\x19',b'\x18',b'\x19']
    ElecSPointer = [0xF604C,0xF604D,0xF604F,0xF605C,0xF605D,0xF605F,0xF606C,0xF606D,0xF606F,]
    ElecSValue = [b'\x29',b'\x2A',b'\x2C',b'\x2D',b'\x44',b'\x3D',b'\x39',b'\x3A',b'\x3C']
    if randomboss == True:
        for x in range(8):
            if pos[x][0] == "Flashman": #Sees if Flashman, Quickman, Sparkman, or Snakeman are a chosen stage
               ValueF = x
            elif pos[x][0] == "Quickman":
               ValueQ = x
            elif pos[x][0] == "Sparkman":
               ValueSp = x
            elif pos[x][0] == "Snakeman":
               ValueSn = x
            elif pos[x][0] == "Elecman":
                ValueE = x

        if ValueF <= 7: 
            if posB[ValueF][0] == "Iceman":
                FlatF = True
            elif posB[ValueF][0] == "Bombman":
                FlatF = True
            elif posB[ValueF][0] == "Fireman":
                FlatF = True 
            elif posB[ValueF][0] == "Elecman":
                FlatF = True
            elif posB[ValueF][0] == "Airman":
                FlatF = True
            elif posB[ValueF][0] == "Woodman":
                FlatF = True
            elif posB[ValueF][0] == "Bubbleman":
                FlatF = True
            elif posB[ValueF][0] == "Heatman":
                FlatF = True
            elif posB[ValueF][0] == "Hardman":
                FlatF = True
            elif posB[ValueF][0] == "Topman":
                FlatF = True
            elif posB[ValueF][0] == "Magnetman":
                FlatF = True
            elif posB[ValueF][0] == "Needleman":
                FlatF = True
            elif posB[ValueF][0] == "Geminiman":
                FlatF = True

        if ValueQ <= 7: 
            if posB[ValueQ][0] == "Iceman":
                FlatQ = True
                Adjust = True
            elif posB[ValueQ][0] == "Bombman":
                FlatQ = True
                Adjust = True
            elif posB[ValueQ][0] == "Fireman":
                FlatQ = True
                Adjust = True
            elif posB[ValueQ][0] == "Elecman":
                FlatQ = True
                Adjust = True
            elif posB[ValueQ][0] == "Crashman":
                FlatQ = True 
            elif posB[ValueQ][0] == "Woodman":
                FlatQ = True
            elif posB[ValueQ][0] == "Bubbleman":
                FlatQ = True
            elif posB[ValueQ][0] == "Heatman":
                FlatQ = True
            elif posB[ValueQ][0] == "Hardman":
                FlatQ = True
            elif posB[ValueQ][0] == "Topman":
                FlatQ = True
            elif posB[ValueQ][0] == "Magnetman":
                FlatQ = True
            elif posB[ValueQ][0] == "Needleman":
                FlatQ = True
            elif posB[ValueQ][0] == "Geminiman":
                FlatQ = True

        if ValueSp <= 7: 
            if posB[ValueSp][0] == "Iceman":
                FlatSp = True
            elif posB[ValueSp][0] == "Bombman":
                FlatSp = True
            elif posB[ValueSp][0] == "Fireman":
                FlatSp = True 
            elif posB[ValueSp][0] == "Elecman":
                FlatSp = True
            elif posB[ValueSp][0] == "Crashman":
                FlatSp = True 
            elif posB[ValueSp][0] == "Woodman":
                FlatSp = True
            elif posB[ValueSp][0] == "Metalman":
                FlatSp = True
            elif posB[ValueSp][0] == "Bubbleman":
                FlatSp = True
            elif posB[ValueSp][0] == "Heatman":
                FlatSp = True
            elif posB[ValueSp][0] == "Hardman":
                FlatSp = True
            elif posB[ValueSp][0] == "Topman":
                FlatSp = True
            elif posB[ValueSp][0] == "Magnetman":
                FlatSp = True
            elif posB[ValueSp][0] == "Needleman":
                FlatSp = True
            elif posB[ValueSp][0] == "Geminiman":
                FlatSp = True

        if ValueSn <= 7: 
            if posB[ValueSn][0] == "Iceman":
                FlatSn = True
            elif posB[ValueSn][0] == "Fireman":
                FlatSn = True 
            elif posB[ValueSn][0] == "Elecman":
                FlatSn = True
            elif posB[ValueSn][0] == "Crashman":
                FlatSn = True
            elif posB[ValueSn][0] == "Flashman":
                FlatSn = True 
            elif posB[ValueSn][0] == "Woodman":
                FlatSn = True
            elif posB[ValueSn][0] == "Bubbleman":
                FlatSn = True
            elif posB[ValueSn][0] == "Heatman":
                FlatSn = True
            elif posB[ValueSn][0] == "Hardman":
                FlatSn = True
            elif posB[ValueSn][0] == "Topman":
                FlatSn = True
            elif posB[ValueSn][0] == "Magnetman":
                FlatSn = True
            elif posB[ValueSn][0] == "Needleman":
                FlatSn = True
            elif posB[ValueSn][0] == "Geminiman":
                FlatSn = True

        if ValueE <= 7:
            if posB[ValueE][0] == "Iceman":
                ElecS = True
            if posB[ValueE][0] == "Airman":
                ElecS = True
            if posB[ValueE][0] == "Magnetman":
                ElecS = True
        
        if FlatF == True: #If Boss is on specific stage, write values to change arena to flat version
            for x in range(28):
                Pointer = FlatFPointer[x]
                Seek = ROM.seek(Pointer, 0)
                ROM.write(FlatFValue[x])
            
        if FlatQ == True:
            for x in range(30):
                Pointer = FlatQPointer[x]
                Seek = ROM.seek(Pointer, 0)
                ROM.write(FlatQValue[x])

            if Adjust == True:
                Pointer = 0x79593
                Seek = ROM.seek(Pointer, 0)
                ROM.write(b'\xA5')

        if FlatSp == True:
            for x in range(28):
                Pointer = FlatSpPointer[x]
                Seek = ROM.seek(Pointer, 0)
                ROM.write(FlatSpValue[x])
                
            Pointer = 0x7A7EF #Moves Robot master up to compensate for layout change
            Seek = ROM.seek(Pointer, 0)
            ROM.write(b'\xA4')

        if FlatSn == True:
            for x in range(17):
                Pointer = FlatSnPointer[x]
                Seek = ROM.seek(Pointer, 0)
                ROM.write(FlatSnValue[x])

        if ElecS == True:
            for x in range(9):
                Pointer = ElecSPointer[x]
                Seek = ROM.seek(Pointer, 0)
                ROM.write(ElecSValue[x])

        
                
#!Start of Boss Unmirroring condition section
    FlipG = False
    FlipB = False
    FlipF = False
    ValueG = 8
    ValueB = 8
    ValueF = 8
    if randomboss == True:
        for x in range(8):
            if pos[x][0] == "Gutsman": #Sees if Guts, Bomb, or Fire are Stages
                ValueG = x
            elif pos[x][0] == "Bombman":
                ValueB = x
            elif pos[x][0] == "Fireman":
                ValueF = x

#If so, if the boss there isn't the respective boss, will set to set the boss to unmirror
        if ValueG <= 7:        
            if Bosses[ValueG] != Gutsmanboss: 
                FlipG = True
                
        if ValueB <= 7:        
            if Bosses[ValueB] != Bombmanboss:
                FlipB = True

        if ValueF <= 7:        
            if Bosses[ValueF] != Firemanboss:
                FlipF = True
                
#Writes to unmirror the boss sprite
        if FlipG == True: 
            Pointer = 0x77FBE
            Value = b'\x00'
            Seek = ROM.seek(Pointer, 0)
            ROM.write(Value)
        
        if FlipB == True:
            Pointer = 0x783DE
            Value = b'\x00'
            Seek = ROM.seek(Pointer, 0)
            ROM.write(Value)
            
        if FlipF == True:
            Pointer = 0x7860E
            Value = b'\x00'
            Seek = ROM.seek(Pointer, 0)
            ROM.write(Value)
            
#!Weapon received writing if randomboss
    Weaponget = []
    if Vanilla == False:
        for x in range(8): #Finds what stages have been written and writes an address based on the stage
            if pos[x][0] == "Cutman":
               Pointer = 0x664B2
               Weaponget.append(Pointer)
            elif pos[x][0] == "Gutsman":
               Pointer = 0x664B4
               Weaponget.append(Pointer)
            elif pos[x][0] == "Iceman":
               Pointer = 0x664B6
               Weaponget.append(Pointer)
            elif pos[x][0] == "Bombman":
               Pointer = 0x664B8
               Weaponget.append(Pointer)
            elif pos[x][0] == "Fireman":
               Pointer = 0x664BA
               Weaponget.append(Pointer)
            elif pos[x][0] == "Elecman":
               Pointer = 0x664BC
               Weaponget.append(Pointer)
            elif pos[x][0] == "Bubbleman":
               Pointer = 0x664DA
               Weaponget.append(Pointer)
            elif pos[x][0] == "Airman":
               Pointer = 0x664DC
               Weaponget.append(Pointer)
            elif pos[x][0] == "Quickman":
               Pointer = 0x664DE
               Weaponget.append(Pointer)
            elif pos[x][0] == "Heatman":
               Pointer = 0x664E0
               Weaponget.append(Pointer)
            elif pos[x][0] == "Woodman":
               Pointer = 0x664E2
               Weaponget.append(Pointer)
            elif pos[x][0] == "Metalman":
               Pointer = 0x664E4
               Weaponget.append(Pointer)
            elif pos[x][0] == "Flashman":
               Pointer = 0x664E6
               Weaponget.append(Pointer)
            elif pos[x][0] == "Crashman":
               Pointer = 0x664E8
               Weaponget.append(Pointer)
            elif pos[x][0] == "Sparkman":
               Pointer = 0x66502
               Weaponget.append(Pointer)
            elif pos[x][0] == "Snakeman":
               Pointer = 0x66504
               Weaponget.append(Pointer)
            elif pos[x][0] == "Needleman":
               Pointer = 0x66506
               Weaponget.append(Pointer)
            elif pos[x][0] == "Hardman":
               Pointer = 0x66508
               Weaponget.append(Pointer)
            elif pos[x][0] == "Topman":
               Pointer = 0x6650A
               Weaponget.append(Pointer)
            elif pos[x][0] == "Geminiman":
               Pointer = 0x6650C
               Weaponget.append(Pointer)
            elif pos[x][0] == "Magnetman":
               Pointer = 0x6650E
               Weaponget.append(Pointer)
            elif pos[x][0] == "Shadowman":
               Pointer = 0x66510
               Weaponget.append(Pointer)
               
        if randomweapons == False: #! 
            for x in range(8):
                if posB[x][0] == "Cutman": #If boss is present, write it's weapon value based on it's position
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x05')
                elif posB[x][0] == "Gutsman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x03')
                elif posB[x][0] == "Iceman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x04')
                elif posB[x][0] == "Bombman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x01')
                elif posB[x][0] == "Fireman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x06')
                elif posB[x][0] == "Elecman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x02')
                elif posB[x][0] == "Bubbleman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x0B')
                elif posB[x][0] == "Airman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x09')
                elif posB[x][0] == "Quickman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x0C')
                elif posB[x][0] == "Heatman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x08')
                elif posB[x][0] == "Woodman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x0A')
                elif posB[x][0] == "Metalman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x0F')
                elif posB[x][0] == "Flashman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x0E')
                elif posB[x][0] == "Crashman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x10')
                elif posB[x][0] == "Sparkman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x1A')
                elif posB[x][0] == "Snakeman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x19')
                elif posB[x][0] == "Needleman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x14')
                elif posB[x][0] == "Hardman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x17')
                elif posB[x][0] == "Topman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x18')
                elif posB[x][0] == "Geminiman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x16')
                elif posB[x][0] == "Magnetman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x15')
                elif posB[x][0] == "Shadowman":
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(b'\x1B')

        if randomweapons == True: #!
            for x in range(8):
                if weapons[x] == Cutbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Cutbyte)
                elif weapons[x] == Gutsbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Gutsbyte)
                elif weapons[x] == Icebyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Icebyte)
                elif weapons[x] == Bombbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Bombbyte)
                elif weapons[x] == Firebyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Firebyte)
                elif weapons[x] == Elecbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Elecbyte)
                elif weapons[x] == Bubblebyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Bubblebyte)
                elif weapons[x] == Airbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Airbyte)
                elif weapons[x] == Quickbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Quickbyte)
                elif weapons[x] == Heatbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Heatbyte)
                elif weapons[x] == Woodbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Woodbyte)
                elif weapons[x] == Metalbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Metalbyte)
                elif weapons[x] == Flashbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Flashbyte)
                elif weapons[x] == Crashbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Crashbyte)
                elif weapons[x] == Sparkbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Sparkbyte)
                elif weapons[x] == Snakebyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Snakebyte)
                elif weapons[x] == Needlebyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Needlebyte)
                elif weapons[x] == Hardbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Hardbyte)
                elif weapons[x] == Topbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Topbyte)
                elif weapons[x] == Geminibyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Geminibyte)
                elif weapons[x] == Magnetbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Magnetbyte)
                elif weapons[x] == Shadowbyte:
                    Pointer = Weaponget[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Shadowbyte)
                    
    #!Writes FF to Weapon Received address if MM3 stage is not a stage in MM3 mode and if MM2 stage is not a stage in MM2 mode
    Stage3 = ["Sparkman", "Snakeman", "Needleman", "Hardman", "Topman", "Geminiman", "Magnetman", "Shadowman"]
    Address3 = [0x66502,0x66504,0x66506,0x66508,0x6650A,0x6650C,0x6650E,0x66510]
    Stage3b = ["Bubbleman", "Airman", "Quickman", "Heatman", "Woodman", "Metalman", "Flashman", "Crashman"]
    Address3b = [0x664DB,0x664DD,0x664DF,0x664E0,0x664E2,0x664E4,0x664E6,0x664E8]
    Blank = b'\xFF'
    Value = 0
    if MM3 == True:
        for x in range(8):
            Value = 0
            for y in range(8):
                if pos[x][0] != Stage3[y]:
                    Value += 1
                if Value == 8:
                    Pointer = Address3[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Blank)
    if MM2 == True:
        for x in range(8):
            Value = 0
            for y in range(8):
                if pos[x][0] != Stage3b[y]:
                    Value += 1
                if Value == 8:
                    Pointer = Address3b[x]
                    Seek = ROM.seek(Pointer, 0)
                    ROM.write(Blank)

#Randomized ammo usage section
    ammoval = []
    FlagA = b'\n'
    FlagB = b'\x0B'
    FlagC = b'\x0C'
    FlagA1 = b'\x00'
    FlagA2 = b'\x20'
    FlagB2 = b'\x40'
    FlagC2 = b'\x80'
    Flag1 = b'\x01'
    Flag2 = b'\x02'
    Flag3 = b'\x03'
    Flag4 = b'\x04'
    if randomammo == True: #!
        Pointer = 0x85A10
        Seek = ROM.seek(Pointer, 0)
        for x in range(8):
            Value = ROM.read(1)
            ammoval.append(Value)
            Pointer += 1
            
        if Vanilla == True:
            for x in range(8):
                if pos[x][0] == "Cutman":
                    Pointer = 0x6AA1E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Gutsman":
                    Pointer = 0x6AA0E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Iceman":
                    Pointer = 0x6AA16
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Bombman":
                    Pointer = 0x6A9FE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Fireman":
                    Pointer = 0x6AA26
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Elecman":
                    Pointer = 0x6AA06
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Bubbleman":
                    Pointer = 0x6AA4E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Airman":
                    Pointer = 0x6AA3E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Quickman":
                    Pointer = 0x6AA56
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Heatman": #Current values are .2:2:4, .4:3:5, .8:4:6, 1:5:9, 2:6:10, 3:7:11
                    Pointer = 0x6AA36
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag2)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag4)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag3)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x05')
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag4)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x06')
                    elif ammoval[x] == Flag1:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x05')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x09')
                    elif ammoval[x] == Flag2:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x06')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x10')
                    elif ammoval[x] == Flag3:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x07')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x11')
                    elif ammoval[x] == Flag4:
                        ROM.write(Flag3)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x07')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x11')
                elif pos[x][0] == "Woodman":
                    Pointer = 0x6AA46
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Metalman":
                    Pointer = 0x6AA6E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Flashman":
                    Pointer = 0x325D2
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(b'\x01')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\x20')
                    elif ammoval[x] == FlagB:
                        ROM.write(b'\x00')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    elif ammoval[x] == Flag2:
                        ROM.write(b'\x01')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\x20')
                    elif ammoval[x] == Flag3:
                        ROM.write(b'\x00')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                    elif ammoval[x] == Flag4:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Crashman":
                    Pointer = 0x6AA76
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Sparkman":
                    Pointer = 0x6AAC6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Snakeman":
                    Pointer = 0x6AABE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Needleman":
                    Pointer = 0x6AA96
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Hardman":
                    Pointer = 0x6AAAE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Topman":
                    Pointer = 0x6AAB6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Geminiman":
                    Pointer = 0x6AAA6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Magnetman":
                    Pointer = 0x6AA9E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif pos[x][0] == "Shadowman":
                    Pointer = 0x6AACE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                    
        if randomweapons == False: #!
            for x in range(8):
                if posB[x][0] == "Cutman":
                    Pointer = 0x6AA1E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Gutsman":
                    Pointer = 0x6AA0E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Iceman":
                    Pointer = 0x6AA16
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Bombman":
                    Pointer = 0x6A9FE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Fireman":
                    Pointer = 0x6AA26
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Elecman":
                    Pointer = 0x6AA06
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Bubbleman":
                    Pointer = 0x6AA4E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Airman":
                    Pointer = 0x6AA3E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Quickman":
                    Pointer = 0x6AA56
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Heatman":
                    Pointer = 0x6AA36
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag2)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag4)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag3)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x05')
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag4)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x06')
                    elif ammoval[x] == Flag1:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x05')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x09')
                    elif ammoval[x] == Flag2:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x06')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x10')
                    elif ammoval[x] == Flag3:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x07')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x11')
                    elif ammoval[x] == Flag4:
                        ROM.write(Flag3)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x07')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x11')
                elif posB[x][0] == "Woodman":
                    Pointer = 0x6AA46
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Metalman":
                    Pointer = 0x6AA6E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Flashman":
                    Pointer = 0x325D2
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(b'\x01')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\x20')
                    elif ammoval[x] == FlagB:
                        ROM.write(b'\x00')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    elif ammoval[x] == Flag2:
                        ROM.write(b'\x01')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\x20')
                    elif ammoval[x] == Flag3:
                        ROM.write(b'\x00')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                    elif ammoval[x] == Flag4:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Crashman":
                    Pointer = 0x6AA76
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Sparkman":
                    Pointer = 0x6AAC6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Snakeman":
                    Pointer = 0x6AABE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Needleman":
                    Pointer = 0x6AA96
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Hardman":
                    Pointer = 0x6AAAE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Topman":
                    Pointer = 0x6AAB6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Geminiman":
                    Pointer = 0x6AAA6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Magnetman":
                    Pointer = 0x6AA9E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif posB[x][0] == "Shadowman":
                    Pointer = 0x6AACE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                    
        if randomweapons == True: #!
            for x in range(8):
                if weapons[x] == Cutbyte:
                    Pointer = 0x6AA1E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Gutsbyte:
                    Pointer = 0x6AA0E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Icebyte:
                    Pointer = 0x6AA16
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Bombbyte:
                    Pointer = 0x6A9FE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Firebyte:
                    Pointer = 0x6AA26
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Elecbyte:
                    Pointer = 0x6AA06
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Bubblebyte:
                    Pointer = 0x6AA4E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Airbyte:
                    Pointer = 0x6AA3E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Quickbyte:
                    Pointer = 0x6AA56
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Heatbyte:
                    Pointer = 0x6AA36
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag2)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag4)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag3)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x05')
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(Flag4)
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x06')
                    elif ammoval[x] == Flag1:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x05')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x09')
                    elif ammoval[x] == Flag2:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x06')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x10')
                    elif ammoval[x] == Flag3:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x07')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x11')
                    elif ammoval[x] == Flag4:
                        ROM.write(Flag3)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x3152E
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x07')
                        Pointer = 0x315AC
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(b'\x11')
                elif weapons[x] == Woodbyte:
                    Pointer = 0x6AA46
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        Pointer = 0x31D5C
                        Seek = ROM.seek(Pointer,0)
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Metalbyte:
                    Pointer = 0x6AA6E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Flashbyte:
                    Pointer = 0x325D2
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(b'\x01')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\x20')
                    elif ammoval[x] == FlagB:
                        ROM.write(b'\x00')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    elif ammoval[x] == Flag2:
                        ROM.write(b'\x01')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\x20')
                    elif ammoval[x] == Flag3:
                        ROM.write(b'\x00')
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(b'\xC0')
                    elif ammoval[x] == Flag4:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Crashbyte:
                    Pointer = 0x6AA76
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Sparkbyte:
                    Pointer = 0x6AAC6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Snakebyte:
                    Pointer = 0x6AABE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Needlebyte:
                    Pointer = 0x6AA96
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Hardbyte:
                    Pointer = 0x6AAAE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Topbyte:
                    Pointer = 0x6AAB6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Geminibyte:
                    Pointer = 0x6AAA6
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Magnetbyte:
                    Pointer = 0x6AA9E
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                elif weapons[x] == Shadowbyte:
                    Pointer = 0x6AACE
                    Seek = ROM.seek(Pointer, 0)
                    if ammoval[x] == FlagA:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA2)
                    elif ammoval[x] == FlagB:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagB2)
                    elif ammoval[x] == FlagC:
                        ROM.write(FlagA1)
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagC2)
                    else:
                        ROM.write(ammoval[x])
                        Pointer += 1
                        Seek = ROM.seek(Pointer, 0)
                        ROM.write(FlagA1)
                        
#MM2 mode specific writing

    if MM2 == True: #!
        Pointer = 0x85624 # Writing proper values for custom code
        Seek = ROM.seek(Pointer,0)
        ROM.write(b'\x2C')
        Pointer += 1
        ROM.write(b'\x2D')
        Pointer += 1
        ROM.write(b'\x2E')
        Pointer += 1
        ROM.write(b'\x2F')
        Pointer += 1
        ROM.write(b'\xFF')
        
        Ladder = False #Give Hardman stage a ladder
        for x in range(8):
            if pos[x][0] == "Hardman":
                Ladder = True
        if Ladder == True:
            Pointer = 0x153304 
            Seek = ROM.seek(Pointer,0)
            ROM.write(b'\x10')
            Pointer += 16
            Seek = ROM.seek(Pointer,0)
            ROM.write(b'\x10')
            Pointer += 16
            Seek = ROM.seek(Pointer,0)
            ROM.write(b'\x10')

        Pointer = 0x64408 #Writing inital MM2 Get Weapon screen to show MM2 screen instead of MM3
        Seek = ROM.seek(Pointer,0)
        for x in range(8):
            ROM.write(b'\x02')
            Pointer += 1

        for x in range(8): # Writing appropriate Get Weapon game screen values
            if pos[x][0] == "Cutman":
                Pointer = 0x643F4
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Gutsman":
                Pointer = 0x643F5
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Iceman":
                Pointer = 0x643F6
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Bombman":
                Pointer = 0x643F7
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Fireman":
                Pointer = 0x643F8
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Elecman":
                Pointer = 0x643F9
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Sparkman":
                Pointer = 0x6441C
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Snakeman":
                Pointer = 0x6441D
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Needleman":
                Pointer = 0x6441E
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Hardman":
                Pointer = 0x6441F
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Topman":
                Pointer = 0x64420
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Geminiman":
                Pointer = 0x64421
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Magnetman":
                Pointer = 0x64422
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')
            if pos[x][0] == "Shadowman":
                Pointer = 0x64423
                Seek = ROM.seek(Pointer,0)
                ROM.write(b'\x02')

        Pointer=0x2DE47 # Modifying slide check code to check if it is a MM3 stage instead of game mode
        Seek=ROM.seek(Pointer,0)
        ROM.write(b'\x28')
        Pointer+=4
        Seek=ROM.seek(Pointer,0)
        ROM.write(b'\x78')
 
    ROM.close()
    
print("Ready to Rock and Roll.")
time.sleep(3)
