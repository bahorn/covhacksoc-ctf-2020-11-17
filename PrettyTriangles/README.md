# PrettyTriangles


Now for something different!

I'm running a service at <IP>:1035 where it prompts you tell if a point in in a triangle!

Check out the censored source code if you want to get an idea how it works.


## Files Provided

* censored.py

## Solution

* You connect to a tcp server
* Skip the header
* Read each line give, run a basic formula to determine if it's in a triangle.
* Solve 100 of these, you get the flag.

See `./solution.py` for an implementation.
