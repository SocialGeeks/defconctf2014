#!/usr/bin/env python2.7
import socket, struct
 
def decode_message(s):
    bf = s.recv(5)
    if not bf: return
    assert len(bf) == 5
    code1, length = struct.unpack('>cI', bf)
    bf = s.recv(length)
    assert len(bf) == length
    if length:
        code2, length = struct.unpack('>cB', bf[:2])
        assert len(bf) == length + 2
        return code1, code2, bf[2:]
    return code1,
 
def encode_message(code1, code2="", msg=""):
    inner_data = (struct.pack('>cB', code2, len(msg)) + msg) if code2 else ''
    return struct.pack('>ci', code1, len(inner_data)) + inner_data
 
def echo_message(msg):
    return "\x00\x00\x00\x00" + chr(len(msg)) + "\n" + msg
 
if __name__ == "__main__":
    s = socket.socket()
    s.connect(("fritas_91a318f87f384a080595696b3c73fc39.2014.shallweplayaga.me", 6908))
    hl = decode_message(s)
    print hl
    s.send(encode_message('\x00', '\n', hl[2]))
    s.send(encode_message('\x01', '\x0d', ''))
    print decode_message(s)

