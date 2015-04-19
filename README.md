# Overview of gta5checkscript

This project is a collection of scripts that I wrote to help validate and/or repair my Grand Theft Auto V PC installation. The scripts available are

* `checkGta.py`: This script will validate the SHA256 hashes of all files in the game directory and report if the files are 'OK', 'CORRUPT', or 'Unknown'. This script is developed for Python 2.x.
* `checkGta3.py`: This script is the same as `checkGta.py` but is developed for Python 3.x.
* `repairGta.py`: This script will use three corrupt files and attempt to construct a single valid file by comparing the three at the binary level. This script is developed for use in both Python 2.x and 3.x.

The `hashes.txt` file is a master list of all expected files in the game directory, and their hashes.

No script will modify any files inside the game directory, or remove corrupt files.

# Contents

* How to use `checkGta.py` and `checkGta3.py`
* How to handle corrupt files
* How to handle unknown files
* How to use `repairGta.py`

# How to use `checkGta.py` and `checkGta3.py`

If you are using Python 2.x then where is says `script` you should use `checkGta.py`. If you are using Python 3.x, then where it says `script` you should use `checkGta3.py`.

Place the `script` in the directory above your GTA V install.

For example, if you have it installed in

`C:\Program Files\Rockstar Games\Grand Theft Auto V\`

then you need to run the script from

`C:\Program Files\Rockstar Games\`

Execute using command prompt and Python. You may need to run as Administrator.

*Note:* If you renamed the install directory, then you will need to modify the `script` where it says

    gtaDirectory = 'Grand Theft Auto V'

and change it so that your directory name appears within the single quotes.

# How to handle corrupt files

If the `script` reports that your file is corrupt, *DO NOT* delete it.

1. Make sure the GTA V Launcher is closed.
2. Rename the file
3. Start the launcher

You must ensure that the download process does not get interrupted so that the launcher will properly verify the file when it's completed the download. If the file fails verification, the launcher should repeat the process until the file is valid. I recommend only renaming one or two files at a time to make sure the launcher has time to fully download and verify the files. It may require repeated attempts.

Once all files are downloaded, run the script once more to verify the results. The launcher does not verify files on launch, it only checks that a file exists and that it's the proper size. However, all files are pre-allocated before download, so if the update process is interrupted then the launcher will never check if the file has a valid hash or not.

# How to handle unknown files

Tell me about them. The script should handle all files in the directory by either hashing them or ignoring them. If a game file is being reported as an unknown, give me the full path to the file so that I can work with it.

Check the Issues section for bugs that report an unknown file. If no bug report exists, please create one so that I can handle it appropriately.

# How to use `repairGta.py`

Okay, this one is a little tricky so make sure to read and understand the instructions entirely. If for any reason something in here doesn't make sense, please create an issue under Feedback so I can get the process as clear as humanly possible.

**First:** The `repairGta.py` script should be run in the same location as `checkGta.py`, or `checkGta3.py`, from above. Read the _How to use `checkGta.py` and `checkGta3.py`_ above if you're not sure.

**Second:** You are going to need 3 copies of the file you want to repair. This is the tricky part.

1. Rename or remove the file you want to repair
2. Start the launcher
3. Wait for the launcher to finish the download and delete the `.hash` and `.part` files
4. *QUICKLY* click on the finished file and hit `CTRL + C` and then `CTRL + V`

If you moved fast enough, you should now have a copy in the folder. For example, if you copied `x64a.rpf` then there should be `x64a - Copy.rpf` in the folder.

*REPEAT* steps 1 through 4 above to get two more copies. When you're done, you will have three files that look something like

* `x64a - Copy.rpf`
* `x64a - Copy (2).rpf`
* `x64a - Copy (3).rpf`
 
**Third:** Now we're ready to configure `repairGta.py`

Inside the script there are two variables that need to be updated before you run the script. Look for variables `repairFile` and `gtaDirectory`. *READ THE COMMENTS* about how to properly configure these variables.

**Fourth:** Run the script.

While you wait, here's what's going to happen.

The script opens the three files for reference, and looks at the binary data within each file. It compares every byte in the three files to see if at least 2 of the files have the same byte of information. If 2 of the 3 have the same byte of data, then we assume that it's the correct data and save it into a target file.

**Fifth:** After the script is done.

When the file is finished, it will be in the same directory as `repairGta.py`. The script will calculate the hash of the new file. Look for this hash inside of `hashes.txt`.

If the hash is correct, celebrate because I do every time. :)

Then, remove any files in the game directory that are copies of the new file. You don't need them anymore. Then, move the new file into the correct location.

If the hash is incorrect, this stinks and it can happen.

Pick one of the three copies that you created earlier, and delete it. Then, go through steps 1 to 4 above again to get a new copy of the file. Re-run the script, and hopefully the file comes out correct this time. So far, I've only had to do this once, but it could happen more often than that depending on your network integrity.

Again, if at any point the above steps do not make sense, please let me know so I can help clear up any confusion. Good luck with the repair.
