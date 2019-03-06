'''
Reads videos from a folder and generate frames for the videos

'''

import cv2 
import os
from os import listdir
from os.path import isfile, join


def getFramesFromVideos(videoFilesDirPath, framesDir):
    videos = [join(videoFilesDirPath, f) for f in listdir(videoFilesDirPath) if isfile(join(videoFilesDirPath, f))]
    
    for video in videos:
        captureFrames(video, framesDir)
        
        
def captureFrames(path, framesDir): 

    # counter to create new file name for each frame 
    count = 0    
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
    # checks whether frames were extracted 
    success = 1
    while success: 
        success, image = vidObj.read()
        videoName = path.split("/")[-1].split(".")[0]
        frameoutput = str(os.path.join(framesDir, videoName))
        cv2.imwrite(framesDir + "/" + videoName + "-%d.jpg" % count, image) 
        count += 1


if __name__ == '__main__': 
    
    getFramesFromVideos("/Users/srinivas/supervisely/train", "/Users/srinivas/supervisely/train/frames")
     
