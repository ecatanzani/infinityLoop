import os
import sys, getopt
import subprocess
import time
from termcolor import colored

def evalProcesses(processName):
    tTemplate = "{command:s}{process:s}"
    dTemplate = tTemplate.format(command="pgrep -x",process=processName)
    return len(myList=os.system(dTemplate))

def main(argv):

    pName = "Decode"
    tInterval = 600

    try:
      opts, args = getopt.getopt(argv,"hv:l:p:c:m",["verbose=","list=","process=","clusterize=","maxprocess="])
    except getopt.GetoptError:
      print(colored('pyParallel.py -v <True/False> -l <path_to_file_list> -p <process_name> -c <clusterize> -m <max_processes>','red'))
      sys.exit(2)

    for opt, arg in opts:
      if opt == '-h':
         print(colored('pyParallel.py -v <True/False> -l <path_to_file_list> -p <process_name> -c <True/False> -m <max_processes>','yellow'))
         sys.exit()
      elif opt in ("-v", "--verbose"):
         if arg == "True":
            verbose = True
      elif opt in ("-l", "--list"):
            listPath = arg
      elif opt in ("-p", "--process"):
            pName = arg
      elif opt in ("-c", "--clusterize")
            if arg == "True":
                doCluster = True
            else:
                doCluster = False
      elif opt in ("-m", "--maxprocess"):
            maxProc = arg  

    
    with open(listPath) as fileList:
        files = fileList.read().splitlines()

    for fIdx in files:
        singleJobDone = False
        tTemplate = "{command:s}{options:s}{fileName:s}"
        dTemplate = tTemplate.format(command="./Decode",option=" -c ",fileName=fIdx)
        while !singleJobDone:
            if evalProcesses(pName) < maxProc :
                os.system(dTemplate)
                singleJobDone = True
            else:
                time.sleep(tInterval)
        


if __name__ == "__main__":
   main(sys.argv[1:])