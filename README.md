# mini-pwntools

Minimum pwntools features, including `remote` class and `p64, u64, flat, ...`

Useful when `pwntools` failed to be installed ( ex: sagemath )

## install

```
python setup.py install
```

or

```
pip install git+https://github.com/OAlienO/mini-pwntools.git
```

## example

```
from minipwn import *

r = remote('127.0.0.1', 20000)
r.recvuntil('hello')
r.recvline()
r.recvlines(3)
r.send('hello')
r.sendline('hello')
r.sendafter('hello', 'world')
r.sendlineafter('hello', 'world')
```
