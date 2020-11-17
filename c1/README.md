## Solution

The string comparsion function doesn't ensure the user input and the password
have the same length.

So if the password is 'uwu' and the user provides 'u', it will validate as
zip('uwu', 'u') will return ('u', 'u')
