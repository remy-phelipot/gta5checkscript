# Set this to the file that will be repaired.
# Do not include the file extension
repairFile = 'x64s'

bufferSize = 1 # in bytes. do not change

# Open the three files that will be used for parity comparison
with open('Grand Theft Auto V\\%s - Copy.rpf' % repairFile, 'rb') as file1:
  with open('Grand Theft Auto V\\%s - Copy (2).rpf' % repairFile, 'rb') as file2:
    with open('Grand Theft Auto V\\%s - Copy (3).rpf' % repairFile, 'rb') as file3:
    
      # Open the target file to repair
      with open('%s.rpf' % repairFile, 'wb') as target:

        file1byte = file1.read(bufferSize)
        file2byte = file2.read(bufferSize)
        file3byte = file3.read(bufferSize)

        while len(file1byte) > 0 and len(file2byte) > 0 and len(file3byte) > 0:
          if file1byte == file2byte == file3byte:
            target.write(file1byte)
          elif file1byte == file2byte:
            target.write(file1byte)
          elif file1byte == file3byte:
            target.write(file1byte)
          elif file2byte == file3byte:
            target.write(file2byte)
          elif file1byte != file2byte != file3byte:
            print 'No good byte. Using file 1'
            target.write(file1byte)

          file1byte = file1.read(bufferSize)
          file2byte = file2.read(bufferSize)
          file3byte = file3.read(bufferSize)

# TODO: Insert hashing utility function here
