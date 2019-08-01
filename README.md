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

```python
from minipwn import *

r = remote('127.0.0.1', 20000)
r.recvuntil('hello')
r.recvline()
r.recvlines(3)
r.send('hello')
r.sendline('hello')
r.sendafter('hello', 'world')
r.sendlineafter('hello', 'world')

p64(0x4006c0)
# b'\xc0\x06@\x00\x00\x00\x00\x00'

u64(b'\xc0\x06@\x00\x00\x00\x00\x00')
# 4196032

flat(0, 1, 2)
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'
```
