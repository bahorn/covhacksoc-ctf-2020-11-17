"""
Highly Secure Flag Storage
"""

import os
from flask import Flask, request

app = Flask(__name__)

PASSWORD = os.environ['PASSWORD']


authFailedMsg = """
BAD PASSWORD
"""

style = """
body {
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}
"""

homeTemplate = """
<html>
    <head>
        <title>Secure Flag Storage</title>
        <style>
        {}
        </style>
        <link rel="stylesheet" href="https://markdowncss.github.io/retro/css/retro.css">
    </head>
    <body>
        <h1><!-- in -->Secure Flag Storage</h1>
        <br />
        <b>{}</b>
        <br />
        <br />
        <form action="/" method="GET">
            <label for="fname">Password:</label>
            <input type="text" id="password" name="password">
            <input type="submit" value="Validate">
        </form>
    </body>
</html>
"""


def strcmp(s1, s2):
    """
    Compare two strings!
    """
    for a, b in zip(s1, s2):
        if a != b:
            return False
    return True


def auth(password):
    """
    Check the provided username and password.
    """

    # type check
    if (not isinstance(password, str)) or (len(password) == 0):
        return False

    return strcmp(PASSWORD, password)


def read_flag():
    """
    Reads the flag!
    """
    f = open('flag.txt')
    flag = f.read()
    f.close()
    return flag

@app.route('/')
def get_flag():
    """
    Homepage!
    """
    args = request.args
    msg = ""
    if 'password' in args:
        if auth(args.get('password')):
            msg = "congratz, here is your flag: " + read_flag()
        else:
            msg = authFailedMsg

    return homeTemplate.format(style, msg)

if __name__ == "__main__":
    pass
