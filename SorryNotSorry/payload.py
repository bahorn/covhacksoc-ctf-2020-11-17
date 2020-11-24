def fun():
    key = b'5LE2JE5VFMJN8ZGCN9OQLQHQY7JEMCUI'
    packed = 'dgQ+Sy82agkyJSM9Zy0mMBFWOTQ+OiE9NWg5Kj8xLDQ='

    def encrypt1(var, key):
        return bytes(a ^ b for a, b in zip(var, key))

    print("Hello There!")
    print("If you can successfully get the source of this program, you can get the key!")

    m = hashlib.sha256()
    sec = encrypt1(key, base64.b64decode(packed))
    m.update(sec)
    m.update(str(random.randint(0,2*32)).encode('ascii'))

    print(base64.b64encode(m.hexdigest().encode('ascii')).decode('ascii'))
