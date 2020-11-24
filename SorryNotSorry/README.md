## Solution

First, replace the exec with a `print` to get the content of the encoded line:

```python3
import random
import hashlib
import zlib
exec(zlib.decompress(base64.b64decode(''.join(magic.replace('.','').split('\n')).split('_ _ _')[0])))
fun()
```

So this extracts code from magic, and executes it.

We repeat the process again, and get the contents of `fun()`:

```python3
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
```


Then, if we print the value of `sec` we get the flag.

Basically the flag was xored with `key`, which is the reason `packed` had to be base64'd
to be in the code as it contains non-ascii symbols.

To see the code steps i made to solve it, check `./solution`
