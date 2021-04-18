__author__ = 'peter'

from DEMutil import GenerateImage
import os
import sys
import logging
import threading
import time

logging.basicConfig(filename = 'output.log', level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

class ThreadManager(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
        self.maxThreads = 5
        self.hillShade = 0
        self.colorRelief = 0
        self.merge = 0
        self.trans = 0
        self.totalThreads = 0

    def increment(self, que):
        logging.info('Waiting for lock')
        self.lock.acquire()
        try:
            if que == 'hillShade':
                if self.hillShade <= 2:
                    logging.info('Acquired hill lock hillshade')
                    self.hillShade = self.hillShade + 1
                    self.totalThreads = self.totalThreads + 1
                    print(self.hillShade, self.totalThreads)
            if que == 'colorRelief':
                if self.colorRelief <=2:
                    logging.info('Acquired hill lock color')
                    logging.info('Acquired color lock')
                    self.colorRelief = self.colorRelief +1
                    self.totalThreads = self.totalThreads + 1
            else:
                pass
        finally:
            self.lock.release()



def main():

    #User input switches
    dir = sys.argv[1]
    fileExtension = sys.argv[2]
    outputLocation = sys.argv[3]
    filesList = os.listdir(dir)

    logging.info("Input Location" + dir)
    logging.info("Output Location" + outputLocation)

    #Generating list of jobs for jobsTable
    jobsTable = {}
    tiffList = []
    for file in filesList:
        if file.endswith(fileExtension):
            jobsTable[file]={'hill':'p', 'color':'p','merge':'w', 'trans':'w', 'completed':'n'}
            tiffList.append(file)


    #Creating workers for jobs
    threadManager = ThreadManager()
    threadList = {}
    jobsDone = False

    #worker = GenerateImage(k, fileExtension, dir)
    #worker = threading.Thread( name=worker, target = worker.generateHillShade, args=(outputLocation,))

    #Outputting Jobs table to the logs


    for k,v in threadList.items():

    logging.info('Completed processing all files')
    logging.info('Active Threads: ' + str(threading.active_count()))




if __name__ == '__main__':
    main()

