import socket


HOST = '35.214.13.199'
PORT = 1035

def side(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)


def pointInTriangle(a, b, c, p):
    A = side(p, a, b)
    B = side(p, b, c)
    C = side(p, c, a)
    
    neg = (A < 0) or (B < 0) or (C < 0)
    pos = (A > 0) or (B > 0) or (C > 0)

    return not (neg and pos)

def solve(line):
    print(line)
    l = line.replace('(', '').replace(')', '').replace(',','').split(' ')
    k = list(map(int, l))

    a = k[0::2]
    b = k[1::2]
    (a, b, c, d) = list(zip(a, b))
    print(a,b,c,d)
    res = pointInTriangle(a, b, c, d)
    print(res)
    if res:
        return b'1\n'
    else:
        return b'0\n'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    first = data.decode('ascii').split('\n')[-2:-1][0]
    r = solve(first)
    s.send(r)
    while True:
        data = s.recv(1024)
        line = data.decode('ascii').split('\n')[0]
        r = solve(line)
        s.send(r)
