__author__ = 'Peter LeBlanc'

''' This is a util for manuliplating DEM data
currently a work in progress new functionality
can be added upon request
'''

#External Libraries

import os
import subprocess
import logging

class GenerateImage(object):
    'An toolkit for generating GeoTiffs from DEM data'

    version = '0.1'     #class variable

    def __init__(self, fileName, fileExt, filePath):
        self.fileName = fileName
        self.fileExt = fileExt
        self.filePath = filePath
        self.absPath = filePath + '/' + fileName



    def generateColorRamp(self, rampSelection):
        'Generates a color ramp file'

        if rampSelection == 'Earth Tones':
            rampFile = open('ramp.txt', 'wt')
            type(rampFile)
            rampFile.write('0 255 255 255\n')
            rampFile.write('1 49 120 181\n')
            rampFile.write('5 93 159 217\n')
            rampFile.write('10 150 131 98\n')
            rampFile.write('15 117 102 77\n')
            rampFile.write('30 185 156 107\n')
            rampFile.write('60 219 202 105\n')
            rampFile.write('300 189 208 156\n')
            rampFile.write('600 102 141 60\n')
            rampFile.write('1000 64 79 36\n')
            rampFile.write('1400 213 117 0\n')
            rampFile.write('2000 97 51 24\n')
            rampFile.write('2400 169 161 140\n')
            rampFile.write('2800 129 108 91\n')
            rampFile.write('3100 73 56 41\n')
            rampFile.write('3600 36 24 0\n')
            rampFile.write('4000 192 212 216\n')
            rampFile.close()
        else:
            print('No color ramp specified')



    def generateHillShade(self, outputFolder):
        'Generates Hillshade relief'
        modTiff=subprocess.Popen(['gdaldem','hillshade',self.absPath, outputFolder + '/hillShade_' + self.fileName, '-z','5','-s','111120'])
        checkOutput = modTiff.communicate()
        return checkOutput

    def generateColorRelief(self, outputFolder):
        'Generates Color relief'
        modTiff=subprocess.Popen(['gdaldem', 'color-relief', self.absPath, 'ramp.txt', outputFolder + '/colorRelief_' + self.fileName])
        checkOutput = modTiff.communicate()
        return checkOutput

    def mergeGeneratedImages(self, outputFolder):
        'Merges the hillshade and color relief'
        modTiff=subprocess.Popen(['./hsv_merge.py', outputFolder + '/colorRelief_' + self.fileName, outputFolder + '/hillShade_' + self.fileName, outputFolder + '/merge_'+ self.fileName])
        checkOutput = modTiff.communicate()
        return checkOutput

    def performTransparancys(self, outputFolder):
        'Makes no data and 255 Transparent'
        modTiff=subprocess.Popen(['gdalwarp', '-dstalpha', '-srcnodata', '255', '-dstnodata', '0', outputFolder + '/merge_'+ self.fileName, outputFolder + '/trans_' + self.fileName])
        checkOutput = modTiff.communicate()
        return checkOutput

