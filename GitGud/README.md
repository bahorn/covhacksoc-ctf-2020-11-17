# GitGud

Hey! Check out this fancy encryption tool i made!

See if you can unlock flag.txt!

## Files Provided

* ctf.zip
* flag.txt.fernet

## Solution

* Essentially, the player is given a git repo with version 2 checked out.
* This version removed a `.env` file containing the key.
* By checking out an older revision, you can use the code to decrypt the provided flag file.
