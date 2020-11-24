# Comparison

Check out my cool flag storage service! It's avaliable here: http://<IP>:5123

It requires a password to get the flag!

## Files Provided

* app.py
* requiremennts.txt

## Solution

* The string comparsion function doesn't ensure the user input and the password have the same length.
* So if the password is 'uwu' and the user provides 'u', it will validate as zip('uwu', 'u') will return ('u', 'u')
* In production, `!d0ntgu3ssm3` was used so people didn't just accidentally solve it by pressing a random key.
