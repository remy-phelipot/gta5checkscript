import hashlib
import os
import time
import sys

startTime = time.time()

# Configure this to the name of the install directory
gtaDirectory = 'Grand Theft Auto V'

# Initialize a list of files to ignore based on the install directory
ignoreFiles = ['commandline.txt',
               'GTAVLauncher.exe',
               'PlayGTAV.exe',
               'ReadMe\\Chinese\\ReadMe.txt',
               'ReadMe\\English\\ReadMe.txt',
               'ReadMe\\French\\ReadMe.txt',
               'ReadMe\\German\\ReadMe.txt',
               'ReadMe\\Italian\\ReadMe.txt',
               'ReadMe\\Japanese\\ReadMe.txt',
               'ReadMe\\Korean\\ReadMe.txt',
               'ReadMe\\Mexican\\Readme.txt',
               'ReadMe\\Polish\\ReadMe.txt',
               'ReadMe\\Portuguese\\ReadMe.txt',
               'ReadMe\\Russian\\ReadMe.txt',
               'ReadMe\\Spanish\\ReadMe.txt',
               'installscript.vdf',
               'steam_api64.dll']
ignoreList = []
for ignoreFile in ignoreFiles:
  ignoreList.append(os.path.join(gtaDirectory, ignoreFile))

# Initialize the log file, or clear it if it's present
logFile = os.path.expanduser('~\\checkGta.log')
print('Logging all output to: %s' % logFile)
with open(logFile, 'w') as log:
  log.write('')

# Adapt hash file if we're using Steam
hashFileName = 'hashes.txt'
if len(sys.argv) > 1 and sys.argv[1] == '-steam':
  hashFileName = 'steam_hashes.txt'

# Ingest the master hash list
print('Loading hash file: %s' % hashFileName)
hashList = {}
with open(hashFileName, 'r') as hashFile:
  lineType = 0
  fileName = ''
  for line in hashFile:
    # Find the new line, if present
    newLineIndex = line.find('\n')
    if lineType == 0:
      # This line should be the file name, including subdirectories
      if newLineIndex > -1:
        fileName = os.path.join(gtaDirectory, line[:newLineIndex])
      else:
        fileName = os.path.join(gtaDirectory, line)
      lineType += 1
      #print(fileName) #diagnostic
    elif lineType == 1:
      # Skip this line, only used for notes
      lineType += 1
    elif lineType == 2:
      # This line should be the file hash
      fileHash = -1
      if newLineIndex > -1:
        fileHash = line[:newLineIndex]
      else:
        fileHash = line
      hashList[fileName] = fileHash
      lineType = 0

# Setup some buckets for counting
okayFiles = 0
badFiles = 0
unknownFiles = 0


# Walk through all files in the install directory
for dirpath, dirnames, filenames in os.walk(gtaDirectory):
  for filename in filenames:
    gtaFile = os.path.join(dirpath, filename)

    if gtaFile in hashList:
      # Hash this file
      BLOCKSIZE = 50120*1024
      hasher = hashlib.new('sha256')
      with open(gtaFile, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
          hasher.update(buf)
          buf = afile.read(BLOCKSIZE)
      gtaHash = hasher.hexdigest()
      #print('%s %s' % (gtaFile, gtaHash)) #diagnostics

      # Pull the hash for this file
      fileHash = hashList[gtaFile]
      if fileHash == gtaHash:

        status = '%s OK!' % gtaFile
        with open(logFile, 'a') as log:
          log.write(status + '\n')
        print(status)
        okayFiles += 1

      else:
        status = '%s HASH MISMATCH!' % gtaFile
        expected = 'Expected \'%s\' but found \'%s\'' % (fileHash, gtaHash)
        with open(logFile, 'a') as log:
          log.write(status + '\n')
          log.write(expected + '\n')
        print(status)
        print(expected)
        badFiles += 1

    elif gtaFile not in ignoreList and gtaFile.find('.part') == -1 and gtaFile.find('.hash') == -1 and gtaFile.find('.lnk') == -1 and gtaFile.find('_CommonRedist') == -1 and gtaFile.find('Installers') == -1:
      # Not sure about this file, output for inspection
      status = 'UNKNOWN file: %s' % gtaFile
      with open(logFile, 'a') as log:
        log.write(status + '\n')
      print(status)
      unknownFiles += 1

# All files processed, output results
print('%s files OK, %s HASH MISMATCHES, %s files UNKNOWN' % (okayFiles, badFiles, unknownFiles))

endTime = time.time()
duration = endTime - startTime
minutes, seconds = divmod(duration, 60)
print('Analysis completed in %sm %ss' % (minutes, seconds))

# Pause for the folks that double-click
try:
  input('Press ENTER to complete the script...')
except:
  # It will always produce an error, so Gotta Catch 'Em All!
  print('Script complete.')
