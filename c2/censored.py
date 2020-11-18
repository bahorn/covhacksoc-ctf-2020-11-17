from twisted.internet import protocol, reactor, endpoints
from twisted.protocols import basic

import random

# First triangle number after 1024 :)
PORT = 1035
HEADER = """
---
Hello! You will receive lines in the form:

P1 P2 P3 C

Where P1,P2,P3 are positive integers that form a triangle.
You need to check if C is in it, sending 1 if yes, 0 if no. (ascii)a

You will receive over 100 points, so go write code :))

e.g:
S > (1,1) (3,3) (3,1) (2,2)
C > 1
S > (1,1) (3,3) (3,1) (5,5)
C > 0

---
"""


def pointInTriangle(a, b, c, p):
    return True

def randomPoint():
    return (random.randint(0, 1024), random.randint(0, 1024))

def generateProblem():
    a = randomPoint()
    b = randomPoint()
    c = randomPoint()
    d = randomPoint()
    sol = pointInTriangle(a, b, c, d)
    return [sol, a, b, c, d]
    
def inToBool(b):
    if b == b'1':
        return True
    else:
        return False

def get_flag():
    f = open('flag.txt')
    flag = f.read()
    f.close()
    return flag

class Triangle(basic.LineReceiver):
    delimiter = '\n'.encode('ascii')
    def __init__(self):
        self.count = 0
        pass

    def sendProblem(self):
        if self.count < 100:
            self.problem = generateProblem()
            self.sendLine(" ".join(map(str, self.problem[1::])).encode('ascii'))
            self.count += 1
        else:
            self.sendLine(get_flag().encode('ascii'))
            self.transport.loseConnection()

            
    def connectionMade(self):
        self.sendLine(HEADER.encode('ascii'))
        self.sendProblem()

    def lineReceived(self, line):
        if self.problem[0] == inToBool(line):
            self.sendProblem()
        else:
            self.transport.loseConnection()


class TriangleFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Triangle()


if __name__ == "__main__":
    endpoints.serverFromString(reactor, "tcp:{}".format(PORT)).listen(TriangleFactory())
    reactor.run()
