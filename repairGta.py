import hashlib
import os
import time

startTime = time.time()

# Set this to the file that will be repaired.
# Do not include the file extension
#
# If the file is nested, such as x64\metadata.dat
# then the file path should look like x64\\metadata.dat
# The double-backslash is required in paths
repairFile = 'x64o'

# Change this only if you've installed GTA using a non-standard directory name
gtaDirectory = 'Grand Theft Auto V'

# Comparison buffer in bytes. Do not change or you could exceed memory limits
bufferSize = 50*1024*1024

print('Attempting to repair %s.rpf' % repairFile)

# Open the three files that will be used for parity comparison
with open('%s\\%s - Copy.rpf' % (gtaDirectory, repairFile), 'rb') as file1:
  with open('%s\\%s - Copy (2).rpf' % (gtaDirectory, repairFile), 'rb') as file2:
    with open('%s\\%s - Copy (3).rpf' % (gtaDirectory, repairFile), 'rb') as file3:

      # Open the target file to repair
      with open('%s.rpf' % repairFile, 'wb') as target:

        targetSize = os.path.getsize('%s\\%s - Copy.rpf' % (gtaDirectory, repairFile))
        print('Target file size: %s' % targetSize)
        bytesWritten = 0
        progressInterval = targetSize / 10
        nextProgressPoint = progressInterval

        file1buffer = file1.read(bufferSize)
        file2buffer = file2.read(bufferSize)
        file3buffer = file3.read(bufferSize)

        # Continue working until EOF
        while len(file1buffer) > 0 and len(file2buffer) > 0 and len(file3buffer) > 0:
          # Iterate through the buffer one byte at a time
          # We start by assuming file 1 is a good start
          writeBuffer = list(file1buffer)
          for byteIndex in range(0,len(file1buffer)):

            file1byte = file1buffer[byteIndex]
            file2byte = file2buffer[byteIndex]
            file3byte = file3buffer[byteIndex]

            if file2byte == file3byte:
              # In this case file 1 may have an error
              writeBuffer[byteIndex] = file2byte

          target.write(''.join(writeBuffer))
          bytesWritten += len(writeBuffer)
          if bytesWritten >= nextProgressPoint:
            print('%s/%s written' % (bytesWritten, targetSize))
            nextProgressPoint += progressInterval

          file1buffer = file1.read(bufferSize)
          file2buffer = file2.read(bufferSize)
          file3buffer = file3.read(bufferSize)

endTime = time.time()
duration = endTime - startTime
minutes, seconds = divmod(duration, 60)
print 'File repair complete in %sm %ss' % (minutes, seconds)

print('Hashing new file...')

# Hash this file
BLOCKSIZE = 64*1024
hasher = hashlib.new('sha256')
with open('%s.rpf' % repairFile, 'rb') as afile:
  buf = afile.read(BLOCKSIZE)
  while len(buf) > 0:
    hasher.update(buf)
    buf = afile.read(BLOCKSIZE)
gtaHash = hasher.hexdigest()
print(gtaHash)
