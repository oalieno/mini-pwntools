import socket

class remote:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.buffer = ""
    def recvuntil(self, text):
        while text not in self.buffer:
            self.buffer += self.s.recv(1024)
        index = self.buffer.find(text) + len(text)
        ans, self.buffer = self.buffer[:index], self.buffer[index:]
        return ans
    def recvline(self):
        return self.recvuntil('\n')
    def recvlines(self, n):
        lines = []
        for _ in range(n):
            lines.append(self.recvline())
        return lines
    def send(self, text):
        self.s.sendall(text)
    def sendline(self, text):
        self.s.sendall(text + '\n')
    def sendafter(self, prefix, text):
        self.recvuntil(prefix)
        self.send(text)
    def sendlineafter(self, prefix, text):
        self.recvuntil(prefix)
        self.sendline(text)
