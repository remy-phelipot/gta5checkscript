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

TODO: Write a how-to here. Coming soon^(TM).
