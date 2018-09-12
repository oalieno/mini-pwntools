# remote

**python2**

Simple wrapper of socket library, replacement of `remote` class in `pwntools`

Useful when `pwntools` failed to be installed ( ex: sagemath )

## install

```
python setup.py install
```

or

```
pip install git+https://github.com/OAlienO/remote.git
```

## example

```
r = remote('127.0.0.1', 20000)
r.recvuntil('hello')
r.recvline()
r.recvlines(3)
r.send('hello')
r.sendline('hello')
r.sendafter('hello', 'world')
r.sendlineafter('hello', 'world')
```
