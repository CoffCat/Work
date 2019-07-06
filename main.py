#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
import time

sourceDir = "/home/youngjune/projects"
targetDir = "/home/youngjune/projects/backup"
fileLists = "SkyNet"

sourceFL = os.path.join(sourceDir,fileLists)
targetFL = os.path.join(targetDir,fileLists)

'''
print("sourceFL: "+ sourceFL)
print("targetFL: "+ targetFL)
'''
def CopyFile(fdFull, fFull):
    print("Source File: "+fdFull)
    print("Target File: "+fFull)

    if not os.path.exists(fFull):
        shutil.copyfile(fdFull, fFull)
        print(fdFull+" copied!")
        return
    else:
        sfTime = os.path.getmtime(fdFull)
        tfTime = os.path.getmtime(fFull)
        if tfTime > sfTime:
            shutil.copyfile(fdFull, fFull)
            print(fdFull+" copied!")
        else:
            print(fdFull + " is not modified, pass!")
    return
        
def BackUp(sourceFL, targetFL):
    
    print("Backup: "+ sourceFL)
    print("To dir: "+ targetFL)
    '''
    if sourceFL == ".*":
        return
    '''
    if not os.path.exists(targetFL):
        os.makedirs(targetFL)

    subFL = os.listdir(sourceFL)#列出所有的文件夹和文件
    for ForD in subFL:#循环处理每个文件夹或文件       
        fdFull  = os.path.join(sourceFL, ForD)
        if os.path.isdir(fdFull):#如果是文件夹
            targetDFull = os.path.join(targetFL, ForD)
            BackUp(fdFull, targetDFull)
        elif os.path.isfile(fdFull):#如果是文件
            fFull = os.path.join(targetFL,ForD)
            CopyFile(fdFull,fFull)
        else:
            pass
    return

BackUp(sourceFL,targetFL)
